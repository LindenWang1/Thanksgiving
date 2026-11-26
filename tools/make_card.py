#!/usr/bin/env python3
"""
make_card.py: build a private, single-file Thanksgiving card for one person.

Usage:
    python3 tools/make_card.py private/you/you.json
    python3 tools/make_card.py private/you/you.json -o ~/Desktop/you.html

The JSON file uses the same fields as the CONFIG block in index.html
(see people.example.json). Any local photo / music / gift-card / drink image paths
are read relative to the JSON file and embedded directly into the HTML, so
the output is ONE self-contained file you can text, email, or AirDrop.

Nothing is uploaded anywhere. Only the Python standard library is used.
"""
import argparse
import base64
import json
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "index.html"
START, END = "/* CONFIG START */", "/* CONFIG END */"
MAX_MB = 8  # warn above this per file


def to_data_uri(path_str: str, base: Path) -> str:
    if not path_str or re.match(r"^(https?:|data:)", path_str, re.I):
        return path_str
    p = (base / path_str).expanduser()
    if not p.is_file():
        print(f"  ! not found, skipped: {p}", file=sys.stderr)
        return ""
    size_mb = p.stat().st_size / 1e6
    if size_mb > MAX_MB:
        print(f"  ! {p.name} is {size_mb:.1f} MB; consider shrinking it", file=sys.stderr)
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    if p.suffix.lower() in (".heic", ".heif"):
        print(f"  ! {p.name}: HEIC photos don't show in most browsers; export as JPG", file=sys.stderr)
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    print(f"  + embedded {p.name} ({size_mb:.2f} MB)")
    return f"data:{mime};base64,{data}"


def make_private(html: str) -> str:
    """Same privacy steps the in-browser editor applies to a downloaded card:
    hide it from search engines, mark it as a personal card (opens as the card,
    not the sample), and drop the public "Create a Thank-You" bar + skip link."""
    html = re.sub(r'<meta name="robots"[^>]*>', '<meta name="robots" content="noindex,nofollow">', html, count=1, flags=re.I)

    body = re.search(r'<body([^>]*?)class="([^"]*)"', html)
    if body:
        parts = body.group(2).split()
        if "personal-card" not in parts:
            parts.append("personal-card")
        html = html[: body.start(2)] + " ".join(parts) + html[body.end(2):]
    # Only the real markup, never the copies of these strings inside the page's own script.
    main = html.find("<main")
    for pat in (r'<div class="create-bar"[^>]*>[\s\S]*?</div>\s*', r'<a class="skip-link"[^>]*>[\s\S]*?</a>\s*'):
        m = re.search(pat, html)
        if m and 0 <= m.start() < main:
            html = html[: m.start()] + html[m.end():]
    return html


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "card"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("person_json", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="output .html (default: next to the JSON)")
    args = ap.parse_args()

    cfg = json.loads(args.person_json.read_text(encoding="utf-8"))
    base = args.person_json.resolve().parent

    for item in cfg.get("photos", {}).get("items", []):
        item["src"] = to_data_uri(item.get("src", ""), base)
    if cfg.get("music", {}).get("src"):
        cfg["music"]["src"] = to_data_uri(cfg["music"]["src"], base)
    if cfg.get("cider", {}).get("image"):
        cfg["cider"]["image"] = to_data_uri(cfg["cider"]["image"], base)
    if cfg.get("giftcard", {}).get("image"):
        cfg["giftcard"]["image"] = to_data_uri(cfg["giftcard"]["image"], base)

    html = TEMPLATE.read_text(encoding="utf-8")
    i, j = html.find(START), html.find(END)
    if i < 0 or j < 0:
        sys.exit("CONFIG markers not found in index.html")
    blob = json.dumps(cfg, ensure_ascii=False, indent=2).replace("</", "<\\/")
    html = html[: i + len(START)] + "\nwindow.CARD = " + blob + ";\n" + html[j:]
    html = make_private(html)

    out = args.out or base / f"thanksgiving-{slugify(cfg.get('to', 'card'))}.html"
    out = out.expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"✓ wrote {out}  ({out.stat().st_size / 1e6:.2f} MB)")

    try:
        out.resolve().relative_to(ROOT)
        rel = out.resolve().relative_to(ROOT).as_posix()
        if not rel.startswith("private/"):
            print("  ! heads up: this file is inside the repo but not in private/, so git could pick it up.", file=sys.stderr)
    except ValueError:
        pass  # outside the repo: safest option


if __name__ == "__main__":
    main()

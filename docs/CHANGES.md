# What Changed

A unified **Create → Customize → Send** experience on top of the cozy desk card. Private by default: nothing
about a card is uploaded to a server. For how to use it, see the [README](../README.md).

## Update 7: Drink Pictures and Thankful-List Icons (Current)

- **Warm drink:** the desk keeps its cider mug, but the opened gift can now show **Iced Matcha**, **Coffee**,
  **Hot Cocoa**, **Tea**, or **Boba**, each drawn in the same soft style as the cider mug, or **your own photo**.
  Picking a drink suggests a matching title and message (for example "a matcha treat, on me") unless you've
  written your own.
- **Thankful list:** a line-by-line editor. Tap the leaf next to any line to give it a picture from the
  116-icon bank, or keep the leaf.
- Drink photos are embedded by downloads and `tools/make_card.py`; private links show the drawing instead, and
  the Send step says so.
- Older cards and links work unchanged: thankful lines can still be plain text.

## Update 6: Consistency Pass

- **Repo layout:** the site lives at the top of the repo again, so GitHub Pages (`main` / root) serves it at
  `lindenwang1.github.io/Thanksgiving/` and the existing `SITE_URL` and preview image stay correct. These notes and
  the screenshots moved to `docs/`.
- **New page theme and cover palette: Juniper** (soft teal with deep teal accents). Now 8 page themes and 12 cover
  palettes, with a matching new starter cover, **Fresh Air**. Chosen over a plum option because no other page
  theme is teal, and the autumn leaves stand out against it.
- **Icons:** removed four that didn't read clearly (Waffles, Gravy Boat, Gardening, Pottery), leaving **116**.
  The Brunch and Studio starter covers now use Croissant and Origami instead.
- **Privacy fix for `tools/make_card.py`:** scripted cards now get the same treatment as downloads from the
  editor: hidden from search engines, opened as a personal card, and no **Create a Thank-You** buttons.
- **Editor:**
  - Each step's title appears once, in the panel header, with a one-line description of the step.
  - The **Fully Private** note shows on Start and Send, where it matters.
  - **Send →** is now an outline button so **Continue →** is the clear next step.
  - Compact header on phones, leaving more room for the step itself.
- **Docs:** README rewritten to match the current card (themes, palettes, starter covers, all 116 icon names,
  layout, and hosting). Screenshots refreshed.

## Update 5: 120 Icons and Brighter Themes

- Added Mittens, Journal, Hot Cocoa, and Kite (120 icons at the time).
- Brightened the page themes toward light, warm, and pastel. Matching cover palettes; Lavender shows as
  **Petal** and Mist as **Soft Mist**. New **Petal** starter cover.

## Update 4: Icons and Themes

- **Captions:** rolled back the oversized gap from Update 3, keeping a small one (about 12px under each gift).
- **Icons:** added 16 (Yoga, Skiing, Waffles, Pretzel, Apple, Soup, Blocks, Darts, Flute, Gardening, Fishing,
  Pottery, Butterfly, Peace, Gravy Boat, Wheat), bringing the bank to 116.
- **Page themes:** Maple, Cider, and Mist added alongside Harvest (default), Cranberry, Sage, and Dusk, with
  matching cover palettes.
- **Starter covers:** Trail Day (Maple), Brunch (Cider), and Studio (Mist).

## Update 3: Shippable Polish

- Downloads are hardened: hidden from search engines, marked as a personal card, with the create bar and skip
  link removed. Cards opened from a private link are marked personal too.
- Send warns when the Cover path has no icons; cleaner private-link addresses; close-button focus ring;
  reduced-motion handling for the cover and captions.

## Update 2: Title Case and Polish

- Consistent Title Case on titles, step headings, buttons, sheet actions (**Open Me First**, **Open the Card →**,
  **See the Cover**), Send cards, and field labels. The letter, subtitles, and gift captions stay in sentence case.
- Quick Thank-You greeting fixed at **Happy Thanksgiving, You**; clearing the name falls back to it.
- Larger touch targets, step focus rings, scroll-to-top on step change, skip link, and labeled controls.

## Update 1: Create → Customize → Send

- **Guided steps** (Start → Write → Cover → Gifts → Send) replace one long editor.
- **Clear Send step:** download and private link side by side, in plain language.
- **Card Studio merged** into the Cover step: starter covers, the icon bank with categories and search,
  Surprise Me, and Re-Tilt.
- **Create buttons** on the public sample (**Create a Thank-You** / **Quick Default**), hidden on personal cards.
- Still one HTML file with no build step; `create.html` and `customize.html` are small entry pages.
- Body font changed to Source Sans 3, alongside Playfair Display and Caveat.

## Screenshots

| File | Shows |
|---|---|
| `media/tg-sample-desk.png` | Public sample with the create buttons |
| `media/tg-create-flow.png` | Step 1: choosing a path |
| `media/tg-write-step.png` | Step 2: Write |
| `media/tg-cover-step.png` | Step 3: starter covers |
| `media/tg-card-open.png` | The cover, as the recipient sees it |
| `media/tg-letter-open.png` | The letter after the cover flips |
| `media/tg-send-download.png` | Step 5: Send |
| `media/tg-private-card-open.png` | A downloaded personal card |
| `media/tg-create-send-demo.webm` | Create → download → open, recorded |

## Ideas for Later

1. **Sharing:** a QR code for the private link, the phone share sheet, and clearer photo-vs-link guidance on Send.
2. **New gift types:** a playlist or a short voice note, without breaking the one-file design.
3. **More icons** as friends ask for them (pets, cities, niche hobbies).

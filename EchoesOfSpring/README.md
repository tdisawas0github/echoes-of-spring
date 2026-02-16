# Echoes of Spring 🌸

A romance / slice-of-life visual novel built with **Ren'Py**.

## Story

You've just arrived in Hanamachi, a small town draped in cherry blossoms, to finish your final year of studies. Along the way you'll meet:

- **Sakura** — a warm, spirited barista and amateur painter at *Petal Brew*.
- **Akira** — a quiet, thoughtful bookshop owner at *Ink & Pages*.

Your choices shape your relationships across **4 chapters** and lead to one of **7 possible endings**:

| Route | Ending | Tone |
|-------|--------|------|
| Sakura | *Colours of Tomorrow* | Hopeful romance |
| Sakura | *Still Waters* | Bittersweet |
| Akira | *Between the Lines* | Tender romance |
| Akira | *Unfinished Pages* | Melancholy |
| Friendship | *Three Colours* | Warm friendship |
| Friendship | *Gentle Distance* | Reflective |
| Solo | *Open Road* | Independent |

## How to Run

1. **Download Ren'Py** from [https://www.renpy.org/](https://www.renpy.org/) (version 8.x recommended).
2. Install / extract Ren'Py to any folder.
3. Copy (or symlink) the **`EchoesOfSpring`** folder into Ren'Py's **projects directory** (shown in the Ren'Py launcher under *Preferences → Projects Directory*).
4. Open the **Ren'Py Launcher**, select **Echoes of Spring**, and click **Launch Project**.

> **Tip:** Ren'Py will auto-generate placeholder images for any missing backgrounds or character sprites so the game is fully playable out of the box.

## Adding Art & Music

Place assets in the `game/` folder:

| Type | Path | Format |
|------|------|--------|
| Backgrounds | `game/images/bg_town.png`, `bg_cafe.png`, etc. | PNG / JPG / WEBP |
| Characters | `game/images/sakura_happy.png`, `akira_neutral.png` | PNG (transparent) |
| Music | `game/audio/bgm_main.ogg` | OGG / MP3 |
| Sound FX | `game/audio/sfx_bell.ogg` | OGG / MP3 |
| GUI assets | `game/gui/textbox.png`, `gui/overlay/` | PNG |

Ren'Py auto-detects images whose filenames match the `show` statements in the script (e.g., `sakura happy` → `sakura_happy.png` or `sakura happy.png`).

## Project Structure

```
EchoesOfSpring/
├── game/
│   ├── script.rpy      # Main story — all dialogue, choices, and endings
│   ├── options.rpy      # Game metadata & build config
│   ├── gui.rpy          # Visual theme (colours, sizes, layout)
│   └── screens.rpy      # UI screens (menus, save/load, prefs, etc.)
└── README.md
```

## Customisation Ideas

- **Add character sprites** — draw or generate art for Sakura & Akira and drop PNGs into `game/images/`.
- **Add background music** — place `.ogg` files in `game/audio/` and add `play music "audio/bgm_main.ogg"` lines in the script.
- **Extend the story** — add new labels in `script.rpy` and branch with `menu:` / `jump`.
- **Translate** — Ren'Py has built-in i18n support; run *Generate Translations* from the launcher.

## License

This project is provided as a starter template. Feel free to modify and distribute.

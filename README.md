# Rubber Duck

## Goal

A tool that utilize the "Rubber Duck" method. This tool will acknowledge when you are saying. Does not matter what you are saying.

## MVP

- [x] Create shapes as models to interact with users.
- [x] Use 3D models (rubber duck, etc) to interact with users.
- [x] Menu to control the application.
- [x] Mic interaction with users' chat.
- [x] Application provide responses to chat.

## How to Use

1. Install the require libraries from requirements.txt
2. Run `pyinstaller --onefile --windowed --add-data "src/assets:assets" start.py`
3. Create a `settings.toml` inside the `dist` folder next to the `.exe` file
4. Copy and paste this into `settings.toml` file

```
[app]
name = "Rubber Duck"
debug = false

[window]
width = 400
height = 300

[paths]
assets = "assets"

[model]
shape = "sphere"
model = ""
shape_color_r = 1.0
shape_color_g = 1.0
shape_color_b = 1.0

[text]
size = 12
visibility = true
```

5. Run the `.exe` file inside the `dist` folder.

## Credits

[Font Awesome](fontawesome.com) - icons, svgs

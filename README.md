# 🎹 Piano

Piano is a Python application that automatically plays songs on the Virtual Piano website by simulating keyboard input.

The user simply pastes a Virtual Piano sheet, selects a delay, and the application performs the song automatically.

## Features

- 🎼 Supports Virtual Piano sheet notation
- 🎹 Plays single notes and chords
- ⚡ Adjustable playback delay
- 🖥️ Simple GUI built with PySide6
- 🌐 Automatically opens Virtual Piano
- ⌨️ Simulates keyboard input using PyAutoGUI

## How It Works

1. Paste a Virtual Piano sheet into the application.
2. Choose the playback delay.
3. Click **Start**.
4. The application opens Virtual Piano.
5. After a short countdown, the music starts playing automatically.

## Example

Input:

```text
[6eu] p s u p s
u p s u p s
[5wu] p s u p s
```

The application parses the notation and reproduces it on the Virtual Piano website.

## Built With

- Python
- PySide6
- PyAutoGUI

## Future Plans

The long-term goal of this project is to evolve from a simple auto-player into an AI-assisted music interpreter.

Future versions may include:

- AI-generated timing between notes
- Dynamic rhythm reproduction
- MIDI support
- Sheet music recognition
- Audio-to-sheet conversion
- Automatic tempo detection
- Intelligent playback that better matches the original performance

## License

MIT License

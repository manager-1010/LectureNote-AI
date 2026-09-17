# LectureNote AI

LectureNote AI is an open-source desktop tool designed to help students turn lecture recordings into readable transcripts.

The goal is to make lecture review faster and easier, especially for students who have long audio or video recordings and do not want to manually transcribe everything.

## Features

- Select MP3, WAV, M4A, or MP4 files
- Local speech-to-text transcription using faster-whisper
- Save transcripts as `_transcript.txt`
- Simple Windows desktop interface
- No account required
- No API key required

## Why I Built This

Students often record lectures but reviewing long recordings takes a lot of time.

LectureNote AI aims to create a simple workflow:

**Lecture recording → Transcript**

The project focuses on making this process easy to use, privacy-friendly, and accessible without requiring complicated technical setup.

## Current Status

LectureNote AI is currently under active development.

Planned improvements include:

- Better Cantonese and English mixed-language transcription
- Improved speaker detection
- Markdown export
- Custom output folder
- Easier installation
- Improved user interface

## Technology

The project currently uses:

- Python
- tkinter
- faster-whisper

## Installation

### Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- Internet connection for the first model download

### Setup

1. Download or clone this repository.

2. Open Command Prompt inside the project folder.

3. Install the required package:

```bash
pip install -r requirements.txt
```

4. Start LectureNote AI:

```bash
python app.py
```

The first time you run transcription, the Whisper model will be downloaded automatically.

## How to Use

1. Open LectureNote AI.
2. Click **Select Audio / Video File**.
3. Choose an MP3, WAV, M4A, or MP4 file.
4. Click **Transcribe**.
5. Wait for the transcription to finish.
6. A text file ending with `_transcript.txt` will be saved next to the original file.

## Privacy

LectureNote AI is designed to process transcription locally on your computer.

- No account is required.
- No API key is required.
- No password is required.
- Lecture files are not uploaded to an external server by this application.

The Whisper model may need to be downloaded from the internet the first time it is used.

## Open Source

This project is being developed as an open-source project.

Bug reports, suggestions, and contributions are welcome.

## Contributing

If you find a bug or have an idea for a new feature, please open an Issue on GitHub.

See `CONTRIBUTING.md` for contribution guidelines.

## License

This project is released under the MIT License.

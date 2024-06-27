# edge_tts_ai_voice_box

## Project Introduction

`edge_tts_ai_voice_box` is an open-source text-to-speech (TTS) tool developed based on the `edge-tts` library, providing users with a simple and easy-to-use graphical user interface (GUI). This tool supports multiple voice options, allowing users to customize text, pitch, and speech rate to generate personalized voice files. Additionally, it offers features such as random text generation, text pasting, text import, opening the archive directory, playing, and saving voice functions.

## Features

- **Multiple Voice Style Selection**: Offers a variety of preset voice styles, including voices with different genders, ages, and regional characteristics.
- **Pitch and Speech Rate Adjustment**: Users can adjust the pitch (Hz) and speech rate (%) of the voice according to their needs.
- **One-Click Speech Synthesis**: Conveniently convert text to speech and support saving as an MP3 file.
- **Random Text Generation**: Built-in random poetry and famous quotes generator, providing inspiration and convenience for users.
- **Convenient Text Operations**: Supports pasting text from the clipboard or importing text from files for speech synthesis.
- **Archive Directory Management**: Users can open and manage the directory where voice files are saved, making it easy to find and organize.
- **Instant Playback and Saving**: The synthesized voice can be played instantly and saved to the user-specified path.

## System Requirements

- Python 3.10 or above
- Operating System: Windows (main development environment), Linux (theoretically supported, not tested)

## Installation Guide

### Step 1: Install Python

Ensure that Python 3.x is installed on your computer. You can download and install it from the [Python official website](https://www.python.org/downloads/).

### Step 2: Clone the Project

Clone the `edge_tts_ai_voice_box` project to your local machine using Git.

```bash
git clone https://github.com/swordswind/edge_tts_ai_voice_box.git 
```

### Step 3: Install Dependencies

Navigate to the project directory and install the required dependencies.

```bash
pip install -r requirements.txt
```

### Step 4: Run the Program

Run the following command in the project's root directory to start the program. (If errors occur, create the missing folders according to the error path and fill in missing materials with any image)

```bash
python main.py
```

## Usage

1. Open the program, and you will see a GUI with a simple blue and white style.
2. Enter the text you want to convert to speech in the text input box.
3. Select a voice style from the drop-down menu.
4. Adjust the pitch and speech rate using the sliders.
5. Click the "One-Click Synthesis" button, and the program will generate a voice file.
6. Use other function buttons for text pasting, importing, playing, saving, and other operations.

## Contribution Guide

We warmly welcome your contributions. You can submit a Pull Request or create an Issue to help us improve the project.

## Open Source License

This project is licensed under the [GPL-3.0](LICENSE).

## Acknowledgements

- The `edge-tts` development team and Microsoft for providing strong backend support for text-to-speech.
- Developers of libraries such as `ttkbootstrap`, `Pillow`, `pyperclip`, `pygame`, for facilitating the construction of the GUI and functionality.

## About the Developers

This software is developed by the MVCH-AI Team, dedicated to creating free and open-source AI tools to promote the development and popularization of technology.

## Contact Us

If you have any questions or suggestions, please contact us through the following methods:

- [GitHub Issues](https://github.com/swordswind/edge_tts_ai_voice_box/issues)

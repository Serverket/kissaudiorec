# KISS Audio Rec &middot; [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://semver.org)

KISS Audio Rec is a simple and easy-to-use Python-based audio recording application.

## :star2: Main Features

- Record audio for preset durations (5 minutes, 10 minutes, 1 hour, 3 hours)
- Record audio until manually stopped
- Play back recorded audio files
- List all recordings in the designated directory
- Delete unwanted recordings
- Simple command-line interface

## :gear: Installation

1. Clone this repository:
   ```
   git clone https://github.com/Serverket/kissaudiorec.git
   cd kissaudiorec
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install sounddevice numpy simpleaudio
   ```

## :shipit: Usage

1. Run the script:
   ```
   python kissaudiorec.py
   ```

2. Follow the on-screen prompts to use the application:

   1. Record Audio for 5 minutes
   2. Record Audio for 10 minutes
   3. Record Audio for 1 hour
   4. Record Audio for 3 hours
   5. Record Audio until stopped
   6. Play Recording
   7. List Recordings
   8. Delete Recording
   9. Exit

3. When recording, you'll be prompted to enter a filename for your recording. The audio files will be saved in a `records` directory within the project folder.

## :brain: Acknowledgements

"Whoever loves discipline loves knowledge, but whoever hates correction is stupid."

## :scroll: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
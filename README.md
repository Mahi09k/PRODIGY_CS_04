# Simple Keylogger

## Overview
This project implements a basic keylogger in Python that captures keystrokes, groups them into words, and logs them to a local file. It is designed for educational purposes and should be used responsibly and ethically.

## Features
- Logs keystrokes to a file.
- Groups characters into words, logging each word on a new line when Enter is pressed.

## Requirements
- Python 3.x
- `pynput` library

## Installation
1. Clone this repository or download the script `keylogger.py`.
2. Install the required library using pip:
    ```sh
    pip install pynput
    ```

## Usage
1. **Run the keylogger script**:
    ```sh
    python keylogger.py
    ```
2. **Stopping the keylogger**: The keylogger will stop when the `Esc` key is pressed.

### Example Output
Keystrokes will be logged to `key_log.txt` with each word on a new line.

## Disclaimer
This keylogger example is provided for educational purposes only. Using keyloggers to monitor someone’s activity without their explicit permission is illegal and unethical. Always obtain proper consent and ensure compliance with local laws and regulations when using or developing such tools.


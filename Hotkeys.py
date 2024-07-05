import keyboard
import pyperclip

# Define a dictionary to hold custom hotkeys
custom_hotkeys = {
    'open_history': 'ctrl+shift+h',
    'save_clip': 'ctrl+shift+s'
}

# Register hotkeys
keyboard.add_hotkey(custom_hotkeys['open_history'], lambda: open_history())
keyboard.add_hotkey(custom_hotkeys['save_clip'], lambda: save_current_clip())

# Clipboard history list
clipboard_history = []

def open_history():
    # Function to open clipboard history
    print("Clipboard History:")
    if not clipboard_history:
        print("No clips saved yet.")
    else:
        for idx, clip in enumerate(clipboard_history):
            print(f"{idx + 1}: {clip}")

def save_current_clip():
    # Function to save the current clipboard content
    current_clip = pyperclip.paste()
    if current_clip and current_clip not in clipboard_history:
        clipboard_history.append(current_clip)
        print("Clip saved!")
    else:
        if not current_clip:
            print("Clipboard is empty.")
        else:
            print("Clip already exists in history.")

# Example to keep the script running for hotkeys to work
print("Press 'esc' to exit.")
keyboard.wait('esc')  # Press 'esc' to exit the script

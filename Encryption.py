import keyboard
import pyperclip
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Define a dictionary to hold custom hotkeys
custom_hotkeys = {
    'open_history': 'ctrl+shift+h',
    'save_clip': 'ctrl+shift+s'
}

# Register hotkeys
keyboard.add_hotkey(custom_hotkeys['open_history'], lambda: open_history())
keyboard.add_hotkey(custom_hotkeys['save_clip'], lambda: save_current_clip())

# Clipboard history list to store encrypted clips
clipboard_history = []

def encrypt_clip(content):
    """Encrypt the clipboard content."""
    encrypted_text = cipher_suite.encrypt(content.encode())
    return encrypted_text

def decrypt_clip(encrypted_content):
    """Decrypt the clipboard content."""
    decrypted_text = cipher_suite.decrypt(encrypted_content).decode()
    return decrypted_text

def open_history():
    """Function to open clipboard history."""
    print("Clipboard History:")
    if not clipboard_history:
        print("No clips saved yet.")
    else:
        for idx, encrypted_clip in enumerate(clipboard_history):
            decrypted_clip = decrypt_clip(encrypted_clip)
            print(f"{idx + 1}: {decrypted_clip}")

def save_current_clip():
    """Function to save the current clipboard content."""
    current_clip = pyperclip.paste()
    if current_clip:
        encrypted_clip = encrypt_clip(current_clip)
        if encrypted_clip not in clipboard_history:
            clipboard_history.append(encrypted_clip)
            print("Clip saved!")
        else:
            print("Clip already exists in history.")
    else:
        print("Clipboard is empty.")

# Example to keep the script running for hotkeys to work
print("Press 'esc' to exit.")
keyboard.wait('esc')  # Press 'esc' to exit the script

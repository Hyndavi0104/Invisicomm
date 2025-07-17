import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog, simpledialog
from aes import AES
from aes import unpad
from imagehide import encode
from imageextract import decode

# Define the uploads folder path
UPLOADS_FOLDER = "uploads"

# Function to show custom dialog with Yes/No options
def show_custom_dialog(title, message, icon="question", yes_command=None, no_command=None):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.configure(bg="#00796B")  # Teal background color
    dialog.geometry("300x150")
    dialog.resizable(False, False)

    # Icon and Message
    icon_label = tk.Label(dialog, text="?", font=("Arial", 24, "bold"), bg="#00796B", fg="white")
    icon_label.pack(side="left", padx=20, pady=20)

    message_label = tk.Label(dialog, text=message, bg="#00796B", fg="white", font=("Arial", 10))
    message_label.pack(side="left", padx=20)

    # Buttons Frame
    buttons_frame = tk.Frame(dialog, bg="#00796B")
    buttons_frame.pack(pady=10)

    # Yes Button
    yes_button = ttk.Button(buttons_frame, text="Yes", command=lambda: (dialog.destroy(), yes_command() if yes_command else None))
    yes_button.pack(side="left", padx=5)

    # No Button
    no_button = ttk.Button(buttons_frame, text="No", command=lambda: (dialog.destroy(), no_command() if no_command else None))
    no_button.pack(side="left", padx=5)

    # Make the dialog modal
    dialog.grab_set()
    dialog.transient(root)
    dialog.wait_window()

# Function to display error message
def show_error(message):
    show_custom_dialog("Error", message)

def encrypt_message():
    text = simpledialog.askstring("Input", "Enter the text to be encrypted:")
    key = get_key("encryption")
    iv = get_iv()
    if key and iv:
        obj = AES(key)
        cipher = obj.encrypt_cbc(text, iv)
        enctext = ''.join(chr(j) for i in cipher for j in i)
        show_custom_dialog("Encrypted Message", f"Here is your encrypted message: {enctext}")

def decrypt_message():
    show_custom_dialog("Note", "A list needs to be passed as encrypted text. Modify code accordingly.")
    key = get_key("decryption")
    iv = get_iv()
    if key and iv:
        cipher = [[82, 214, 73, 255, 189, 148, 31, 109, 36, 213, 241, 19, 240, 128, 113, 142],
                  [248, 241, 148, 140, 143, 63, 222, 195, 202, 210, 244, 74, 102, 0, 190, 200],
                  [29, 45, 179, 186, 183, 88, 115, 91, 115, 240, 60, 133, 170, 156, 139, 215]]
        obj = AES(key)
        try:
            msg = obj.decrypt_cbc(cipher, iv)
            msgstr = ''.join(chr(j) for i in msg for j in i)
            show_custom_dialog("Decrypted Message", f"Here is your decrypted message: {unpad(msgstr)}")
        except ValueError:
            show_error("Decryption failed! The key or IV may be incorrect.")

# Global variables to store key and IV for validation
stored_key = None
stored_iv = None

def encrypt_message_and_hide():
    global stored_key, stored_iv
    text = simpledialog.askstring("Input", "Enter the text to be encrypted:")
    key = get_key("encryption")
    iv = get_iv()
    if key and iv:
        stored_key = key  # Store the key for validation
        stored_iv = iv  # Store the IV for validation

        obj = AES(key)
        cipher = obj.encrypt_cbc(text, iv)
        img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.bmp")])

        if img_path:
            dialog = tk.Toplevel(root)
            dialog.title("Image Preview")
            dialog.geometry("400x300")

            img = Image.open(img_path)
            img_resized = img.resize((300, 200), Image.Resampling.LANCZOS)
            img_display = ImageTk.PhotoImage(img_resized)

            img_label = tk.Label(dialog, image=img_display)
            img_label.image = img_display
            img_label.pack(pady=10)

            def on_ok():
                dialog.destroy()
                img_filename = os.path.basename(img_path)
                saved_img_path = os.path.join(UPLOADS_FOLDER, img_filename)
                os.makedirs(UPLOADS_FOLDER, exist_ok=True)
                img.save(saved_img_path)

                encode(saved_img_path, cipher)
                show_custom_dialog("Success", f"Message encrypted and hidden in {saved_img_path}!")

            def on_cancel():
                dialog.destroy()

            button_ok = ttk.Button(dialog, text="OK", command=on_ok)
            button_ok.pack(side=tk.LEFT, padx=20, pady=10)
            button_cancel = ttk.Button(dialog, text="Cancel", command=on_cancel)
            button_cancel.pack(side=tk.RIGHT, padx=20, pady=10)

            dialog.grab_set()
            dialog.transient(root)

def decrypt_image():
    global stored_key, stored_iv
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.bmp")])

    if img_path:
        if "hidden.bmp" not in os.path.basename(img_path):
            show_error("Please enter the encrypted image.")
            return

        dialog = tk.Toplevel(root)
        dialog.title("Image Preview")
        dialog.geometry("400x300")

        img = Image.open(img_path)
        img_resized = img.resize((300, 200), Image.Resampling.LANCZOS)
        img_display = ImageTk.PhotoImage(img_resized)

        img_label = tk.Label(dialog, image=img_display)
        img_label.image = img_display
        img_label.pack(pady=10)

        def get_validated_key_iv():
            while True:
                key = get_key("decryption")
                if key is None:
                    return None, None
                if key == stored_key:
                    break
                else:
                    show_error("Incorrect key! Please enter the correct key used during encryption.")

            while True:
                iv = get_iv()
                if iv is None:
                    return None, None
                if iv == stored_iv:
                    break
                else:
                    show_error("Incorrect initialization vector! Please enter the correct IV used during encryption.")
            
            return key, iv

        def on_ok():
            dialog.destroy()
            rval = decode(img_path)
            nlist, tlist = [], []
            for i, item in enumerate(rval, 1):
                tlist.append(item)
                if i % 16 == 0:
                    nlist.append(list(tlist))
                    tlist.clear()

            key, iv = get_validated_key_iv()
            if key is None or iv is None:
                show_error("Decryption canceled.")
                return

            obj = AES(key)
            try:
                msg = obj.decrypt_cbc(nlist, iv)
                msgstr = ''.join(chr(j) for i in msg for j in i)
                show_custom_dialog("Decrypted Message", f"Here is your decrypted message: {unpad(msgstr)}")
            except ValueError:
                show_error("Decryption failed! The key or IV may be incorrect.")

        button_ok = ttk.Button(dialog, text="OK", command=on_ok)
        button_ok.pack(side=tk.LEFT, padx=20, pady=10)
        button_cancel = ttk.Button(dialog, text="Cancel", command=lambda: dialog.destroy())
        button_cancel.pack(side=tk.RIGHT, padx=20, pady=10)

        dialog.grab_set()
        dialog.transient(root)

def get_key(action):
    key = simpledialog.askstring("Input", f"Enter 16 bytes long {action} key:")
    if key is None:
        return None
    while key and (len(key) != 16):
        show_error(f"The length of the key needs to be 16 bytes. Please enter a valid {action} key:")
        key = simpledialog.askstring("Input", f"Enter 16 bytes long {action} key:")
        if key is None:
            return None
    return key

def get_iv():
    iv = simpledialog.askstring("Input", "Enter 16 bytes long initialization vector:")
    if iv is None:
        return None
    while iv and (len(iv) != 16):
        show_error("The length of the initialization vector needs to be 16 bytes. Please enter a valid IV:")
        iv = simpledialog.askstring("Input", "Enter 16 bytes long initialization vector:")
        if iv is None:
            return None
    return iv

# Main tkinter window
root = tk.Tk()
root.geometry("200x150")

# UI buttons
button_encrypt = ttk.Button(root, text="Encrypt and Hide", command=encrypt_message_and_hide)
button_encrypt.pack(pady=5)

button_decrypt = ttk.Button(root, text="Decrypt Image", command=decrypt_image)
button_decrypt.pack(pady=5)

button_message_encrypt = ttk.Button(root, text="Encrypt Message", command=encrypt_message)
button_message_encrypt.pack(pady=5)

button_message_decrypt = ttk.Button(root, text="Decrypt Message", command=decrypt_message)
button_message_decrypt.pack(pady=5)

root.mainloop()

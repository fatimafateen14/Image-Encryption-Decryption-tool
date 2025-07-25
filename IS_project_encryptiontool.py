# Complete Image Encryption and Decryption in Python with XOR Logic and GUI
import os
from tkinter import Tk, Label, Button, filedialog, messagebox, simpledialog

def select_file():
    filepath = filedialog.askopenfilename(title="Select an Image")
    return filepath

def encrypt_image():
    filepath = select_file()
    if not filepath:
        return

    try:
        key = simpledialog.askinteger("Encryption Key", "Enter Key for encryption of Image:")
        if key is None:
            return

        # Reading the image file
        with open(filepath, 'rb') as f:
            image = bytearray(f.read())

        # XOR operation for encryption
        for index, values in enumerate(image):
            image[index] = values ^ key

        encrypted_path = os.path.join(os.path.dirname(filepath), "encrypted_" + os.path.basename(filepath))

        # Writing the encrypted image back to file
        with open(encrypted_path, 'wb') as f:
            f.write(image)

        messagebox.showinfo("Success", f"Image encrypted and saved to {encrypted_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")

def decrypt_image():
    filepath = select_file()
    if not filepath:
        return

    try:
        key = simpledialog.askinteger("Decryption Key", "Enter Key for decryption of Image:")
        if key is None:
            return

        # Reading the encrypted image file
        with open(filepath, 'rb') as f:
            image = bytearray(f.read())

        # XOR operation for decryption
        for index, values in enumerate(image):
            image[index] = values ^ key

        decrypted_path = os.path.join(os.path.dirname(filepath), "decrypted_" + os.path.basename(filepath))

        # Writing the decrypted image back to file
        with open(decrypted_path, 'wb') as f:
            f.write(image)

        messagebox.showinfo("Success", f"Image decrypted and saved to {decrypted_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

# GUI Implementation
root = Tk()
root.title("Image Encryptor & Decryptor")
root.geometry("400x200")

Label(root, text="Image Encryption & Decryption", font=("Arial", 16)).pack(pady=10)

Button(root, text="Encrypt Image", command=encrypt_image, width=20).pack(pady=10)
Button(root, text="Decrypt Image", command=decrypt_image, width=20).pack(pady=10)

root.mainloop()

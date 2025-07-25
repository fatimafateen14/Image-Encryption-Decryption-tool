# Image-Crypt-Information-Security
Image encryption and decryption tool
  The aim of this project is to construct a Python-based tool for image encryption and decryption. This tool uses the XOR logic for both encryption and decryption, and it provides a user-friendly graphical user interface (GUI) developed with Tkinter. The encrypted images can be safely transferred to another user, who can then decrypt them with the same project, the ensuring secure image transmission between users.  The aim of this project is to construct a Python-based tool for image encryption and decryption. This tool uses the XOR logic for both encryption and decryption, and it provides a user-friendly graphical user interface (GUI) developed with Tkinter. The encrypted images can be safely transferred to another user, who can then decrypt them with the same project, the ensuring secure image transmission between users.
  . Key Features
•	Image Encryption and Decryption:
  The tool encrypts and decrypts pictures with XOR logic. The user enters a unique encryption and decryption key, ensuring that only users with the correct key can access the original image.
•	GUI for Easy Usage:
  The project has an easy-to-use graphical user interface (GUI) that allows users to encrypt and decrypt photos without the need for command-line interaction.
•	File Selection:
  Using a file dialog box, the tool enables users to choose which picture files to encrypt or decrypt, making the entire procedure straightforward.
•	Error Handling:
To handle standard issues like choosing the wrong file or using the wrong key to decrypt, the tool has error handling built in.
XOR Encryption Algorithm
          XOR (exclusive OR) is a simple binary operation used for encryption and decryption. In this project, XOR is used to modify the bytes of an image file, based on the provided key. The encryption and decryption process is the same because XOR is a reversible operation: applying the same XOR operation with the same key on an already XOR-ed byte results in the original value.
# 🛡️ Image-Crypt: Information Security Tool

**Image-Crypt** is a Python-based tool for secure **image encryption and decryption** using a simple yet effective **XOR-based encryption algorithm**. With a user-friendly **GUI built with Tkinter**, this tool allows users to securely encrypt image files and share them with confidence. Only those with the correct decryption key can retrieve the original image.

---

## 🔐 Key Features

- **🔏 Image Encryption & Decryption**  
  Encrypts and decrypts images using XOR logic and a user-provided key. Secure communication is ensured, as only the right key can recover the original image.

- **🖼️ GUI-Based Interface**  
  Built with **Tkinter**, allowing users to use the tool without needing to interact with the command line.

- **📁 File Selection Dialog**  
  Users can browse and select image files to encrypt or decrypt, improving ease of use.

- **❗ Error Handling**  
  Detects issues such as:
  - Invalid or unsupported files
  - Incorrect decryption keys
  - Missing selections

---

## 🔧 How XOR Encryption Works

The **XOR (exclusive OR)** operation is a basic binary function:
- `A ⊕ B = C`
- `C ⊕ B = A` (same key reverses it)

In this project:
- Each byte of the image file is XOR-ed with the user’s key during encryption.
- Decryption is performed by applying the same operation and key again.

---

## 📷 How It Works – Workflow

1. Launch the app.
2. Choose the image file to encrypt or decrypt.
3. Enter the secret key.
4. Click `Encrypt` or `Decrypt`.
5. The output file is saved and ready to use or share.

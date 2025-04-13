from cryptography.fernet import Fernet
import os

# Generate and save a secret key
def generate_key(file_name="secret.key"):
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    print(f"[+] Key generated and saved as {file_name}")
    return key
x
# Load existing key
def load_key(file_name="secret.key"):
    try:
        with open(file_name, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[!] Key file not found. Please generate a key first.")
        return None

# Encrypt file content
def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(output_file, "wb") as f:
            f.write(encrypted)
        print(f"[+] File encrypted and saved as {output_file}")
    except Exception as e:
        print(f"[!] Error during encryption: {e}")

# Decrypt file content
def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        with open(output_file, "wb") as f:
            f.write(decrypted)
        print(f"[+] File decrypted and saved as {output_file}")
    except Exception as e:
        print(f"[!] Error during decryption: {e}")

# Menu interface
def main():
    print("=== File Encryption/Decryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        generate_key()

    elif choice == '2':
        key = load_key()
        if key:
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the name for the encrypted output file: ")
            encrypt_file(input_file, output_file, key)

    elif choice == '3':
        key = load_key()
        if key:
            input_file = input("Enter the path of the encrypted file: ")
            output_file = input("Enter the name for the decrypted output file: ")
            decrypt_file(input_file, output_file, key)

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()

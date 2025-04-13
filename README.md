# 🔐 Ethical Hacking Tools Collection (Python)

A collection of Python-based tools developed for ethical hacking and cybersecurity tasks. Each tool is lightweight, CLI-based, and designed to help beginners and professionals understand fundamental cybersecurity concepts.

---

## 📦 Contents

1. [Password Strength Checker](#-1-password-strength-checker)
2. [Basic Port Scanner](#-2-basic-port-scanner)
3. [File Encryption/Decryption Tool](#-3-file-encryptiondecryption-tool)

---

## ✅ Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt


1. Password Strength Checker
✔️ Features
Evaluates password strength based on:

Length

Uppercase and lowercase letters

Numbers

Special characters

Provides strength rating: Weak, Moderate, or Strong

2. Basic Port Scanner (with Banner Grabber)
✔️ Features
Scans a target IP for open ports

Supports custom port ranges

Uses multithreading for faster scanning

Grabs basic service banners

Handles invalid IPs and ports gracefully

3. File Encryption/Decryption Tool (with Audit Logging)
✔️ Features
Encrypt/decrypt any file type

Uses password-protected key (AES/Fernet with PBKDF2HMAC)

Generates and stores protected_key.key

Stores logs in audit_log.csv with:

Timestamp

Username

Action (encrypt/decrypt)

Input/output filenames

Choose one of the following options:

Generate password-protected key

Encrypt a file

Decrypt a file

Author
Parveen Kumar
Cybersecurity Intern @Hack Secure

# 🔐 Password Security Analyzer

A Python and Flask-based web application that analyzes password strength using multiple security criteria and provides clear feedback to the user.

## 📌 Project Overview

The Password Security Analyzer evaluates a password based on its length, character types, character variety, and common-password patterns.

The application provides:

- Password strength classification
- Security score out of 7
- Individual security requirement checks
- Common-password and common-word detection
- Security recommendations
- Show/Hide password functionality
- Responsive cybersecurity-themed interface

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja2

## ⚙️ Features

### 1. Password Length Analysis

The application checks whether the password:

- Contains at least 8 characters
- Contains 12 or more characters

### 2. Character Requirements

The password is checked for:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

### 3. Character Variety

The application evaluates the variety of character types used in the password.

### 4. Security Score

The password receives a score from:

**0/7 to 7/7**

The score is based on the security requirements implemented in the application.

### 5. Strength Classification

Passwords are classified as:

- **Weak**
- **Medium**
- **Strong**

### 6. Common Password Detection

The application checks passwords against a list of commonly used words and passwords.

It can also detect common words appearing inside a password.

For example:

`Password123!`

can be detected because it contains the common word:

`password`

### 7. Security Recommendations

When a common password pattern is detected, the application recommends choosing a more unique password.

### 8. Show / Hide Password

Users can toggle password visibility using the eye button.

## 📁 Project Structure

```text
Password-Strength-Checker/
│
├── app.py
├── common_passwords.txt
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
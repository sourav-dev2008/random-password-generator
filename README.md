# 🔒 Random Password Generator

Python-based Random Password Generator which can create a random password depending upon the length inputted by the user.

This Python program uses a combination of upper case alphabets, lower case alphabets, numbers, and symbols for creating random passwords.

---

## 📍 About The Project

The **Random Password Generator** is an introductory level project in Python which randomly generates passwords.

The user specifies the number of characters that should be included in the password, and the generator randomly chooses those characters.

The generated password can contain:

- Uppercase alphabets (`A-Z`)
- Lowercase alphabets (`a-z`)
- Digits (`0-9`)
- Special characters (`!`, `@`, `#`, `$`, `%`, etc.)

This project uses Python's built-in `random` and `string` modules.

---

## 🔨 Technologies Used

- Python 3
- `random` module
- `string` module

### External Dependencies

No external Python packages are required.

Both `random` and `string` are part of Python's standard library and are automatically available in Python 3.

---

## 📁 Project Structure

```text
Random-Password-Generator/
│
├── random_password_generator.py
└── README.md
```
## ⚙️ Setup & Installation

### Step 1: Install Python 3
Check if Python is version 3 or not:

```bash
python --version
```

### Step 2: Run the Program
Open a terminal in the project folder and execute:

```bash
python password_generator.py
```

## 📤 Example Output
```text
Enter password length: 12
Your random password is: aG7@kP2#xQ9!
```
The password is different each time as the characters are chosen randomly.

## 🧠 Concepts Used

- Variables
- User input
- Type conversion
- Strings
- `for` loops
- Modules
- `random.choice()`
- String concatenation
- Python standard library

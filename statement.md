# 📝 Project Statement – Random Password Generator

**Author:** Sourav Paul
**Language:** Python 3

---

## 1. Problem Statement

Weak, short, and predictable passwords (such as names, birthdays, or "123456") are one of the most common reasons personal accounts get compromised. Many users find it difficult to come up with strong passwords on their own, and they often end up reusing simple ones across multiple accounts.

There is a need for a simple, lightweight tool that can instantly generate a random, hard-to-guess password made up of a mix of uppercase letters, lowercase letters, digits, and special symbols, with a length chosen by the user.

---

## 2. Scope of the Project

### In Scope

- Accepting the desired password length from the user through the command line.
- Building a character pool from uppercase letters, lowercase letters, digits, and punctuation symbols.
- Randomly selecting characters from the pool to build a password of the requested length.
- Displaying the generated password to the user.
- Using only Python's standard library (`random` and `string`), with no external dependencies.

### Out of Scope

- Graphical or web-based user interface.
- Storing, saving, or managing generated passwords (no database or password vault).
- Password strength checking or scoring.
- Cryptographically secure generation (the `random` module is used for learning purposes; the `secrets` module would be needed for production-grade security).
- User accounts, authentication, or network features.

---

## 3. Target Users

- **Beginners and students** learning Python fundamentals such as user input, loops, strings, and modules.
- **General users** who want a quick way to create a random password for a personal account.
- **Educators and reviewers** looking for a simple example of using Python's standard library.

---

## 4. High-Level Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Custom length input** | The user decides how many characters the password should contain. |
| 2 | **Mixed character set** | Passwords include uppercase, lowercase, digits, and special characters. |
| 3 | **Random generation** | Each character is chosen independently at random, so the password differs on every run. |
| 4 | **Instant output** | The generated password is printed immediately in the terminal. |
| 5 | **No dependencies** | Runs on any system with Python 3 installed, with nothing extra to install. |

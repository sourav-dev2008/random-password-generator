# 📝 Project Statement – Random Password Generator

---

## 1. Problem Statement

One of the most common causes of account vulnerabilities is the use of weak, short, and predictable passwords like names, dates of birth, or "123456". It is very challenging for users to create strong passwords, and thus they tend to reuse the same simple passwords in different accounts.

There is a need for the creation of an easy-to-use tool for generating a completely random, unpredictable password composed of a combination of upper-case letters, lower-case letters, numbers, and symbols of the user's choosing.

---

## 2. Scope of the Project

### In Scope

- Accepting the desired password length from the user through the command line.
- Building a character pool from uppercase letters, lowercase letters, digits, and punctuation symbols.
- Randomly selecting characters from the pool to build a password of the requested length.
- Displaying the generated password to the user.
- Using only Python's standard library (`random` and `string`), with no external dependencies.

### Out of Scope

- Graphical or Web-based user interface.
- Password storage, saving or management (without a database or a password manager).
- Password strength estimation.
- Cryptographically safe password generation (module `random` is used for educational purposes, while `secrets` should be used to ensure strong security).
- User accounts, authorization or networking.

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

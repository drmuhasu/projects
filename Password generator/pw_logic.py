import random
import string
import tkinter as tk


def display_password(password_length, include_letters, include_numbers, include_special_chars, main_window):
    # Generate password using function from password_generator.py
    password = generate_password(password_length, include_letters, include_numbers, include_special_chars)

    if not hasattr(main_window, 'password_label'):  # Check if the label has been created
        gen_pw_label = tk.Label(main_window, text="Generated Password:")
        gen_pw_label.grid(row=10, column=2)

        main_window.password_label = tk.Label(main_window, text="")
        main_window.password_label.grid(row=10, column=3)

    main_window.password_label.config(text=password)  # Update the generated password

    main_window.focus_set()
    return main_window


def generate_password(password_length, include_letters, include_numbers, include_special_chars):
    # Set the number of characters from each set to be included
    num_letters = 1 if include_letters else 0
    num_digits = 1 if include_numbers else 0
    num_special_chars = 1 if include_special_chars else 0

    if password_length < num_letters + num_digits + num_special_chars:
        raise ValueError()

    password = ''

    # Initialize the password with one character from each set
    if include_letters:
        password = random.choice(string.ascii_letters)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special_chars:
        password += random.choice(string.punctuation)

    # Randomly select the remaining characters for the password
    remaining_length = password_length - (num_letters + num_digits + num_special_chars)
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password += ''.join(random.choices(characters, k=remaining_length))

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

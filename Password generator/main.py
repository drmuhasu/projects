from pw_logic import *


def validate():
    try:
        password_length = int(entry.get())
        if 26 > password_length > 5:
            include_numbers = numbers_var.get()
            include_letters = letters_var.get()
            include_special_chars = special_chars_var.get()

            if include_numbers or include_letters or include_special_chars:
                invalid_validation.config(text="")
                invalid_validation.grid(row=0, column=2)
                display_password(password_length, include_letters, include_numbers, include_special_chars, main_win)
            else:
                invalid_validation.config(text="Invalid Value")
                invalid_validation.grid(row=0, column=2)
        else:
            invalid_validation.config(text="Invalid Value")
            invalid_validation.grid(row=0, column=2)
    except ValueError:
        invalid_validation.config(text="Invalid value")
        invalid_validation.grid(row=0, column=2)


# Creating a Main Window
main_win = tk.Tk()
main_win.title("Password Manager")
width = 350
height = 100
screen_width = main_win.winfo_screenwidth()
screen_height = main_win.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
main_win.geometry("%dx%d+%d+%d" % (width, height, x, y))


# Password length label and entry
pw_length_label = tk.Label(main_win, text="Password Length:")
pw_length_label.grid(row=0, column=0, padx=10, sticky="e")
entry = tk.Entry(main_win, width=2)
entry.grid(row=0, column=1, padx=5, sticky="w")
range_label = tk.Label(main_win, text="between 6-25")
range_label.grid(row=0, column=1, padx=25, sticky="e")

# Checkbox label and checkboxes
checkbox_label = tk.Label(main_win, text="Include:")
checkbox_label.grid(row=2, column=0, padx=10, sticky="w")

# Checkbox to include letters
letters_var = tk.BooleanVar(value=True)
letters_checkbox = tk.Checkbutton(main_win, text="letters", variable=letters_var)
letters_checkbox.grid(row=2, column=1, sticky="w")

# Checkbox to include numbers
numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(main_win, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=2, sticky="w")

# Checkbox to include special characters
special_chars_var = tk.BooleanVar(value=True)
special_chars_checkbox = tk.Checkbutton(main_win, text="Special", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=3, sticky="w", columnspan=2)


# Button to generate password
generate_button = tk.Button(main_win, text="Generate", command=validate)
generate_button.grid(row=5, column=1, padx=10)

# Label for length validation message
invalid_validation = tk.Label(main_win, text="", fg="red")
invalid_validation.grid(row=0, column=1, sticky="e")

# Run the main loop
main_win.mainloop()

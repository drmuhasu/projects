from pw_logic import *

def validate():
    try:
        password_length = int(entry.get())
        if 26 > password_length > 5:
            include_numbers = numbers_var.get()
            include_letters = letters_var.get()
            include_special_chars = special_chars_var.get()

            if include_numbers or include_letters or include_special_chars:
                range_and_validation_label.config(text="")
                range_and_validation_label.grid(row=0, column=3, sticky="e")
                display_password(password_length, include_letters, include_numbers, include_special_chars, main_win)
            else:
                range_and_validation_label.config(text="Invalid Value")
                range_and_validation_label.grid(row=0, column=3, sticky="e", fg="red")
        else:
            range_and_validation_label.config(text="Invalid Value")
            range_and_validation_label.grid(row=0, column=2, sticky="e", fg="red")
    except ValueError:
        range_and_validation_label.config(text="Invalid value", fg="red")
        range_and_validation_label.grid(row=0, column=2, sticky="e")


main_win = tk.Tk()
main_win.title("Password Manager")
width = 350
height = 100
screen_width = main_win.winfo_screenwidth()
screen_height = main_win.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
main_win.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Frame for password length
length_frame = tk.Frame(main_win)
length_frame.grid(row=0, column=0)

pw_length_label = tk.Label(length_frame, text="Password Length:")
pw_length_label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(length_frame, width=2)
entry.grid(row=0, column=1, sticky="w")

range_and_validation_label = tk.Label(length_frame, text="between 6-25")
range_and_validation_label.grid(row=0, column=2, sticky="e")

# Frame for checkboxes
checkbox_frame = tk.Frame(main_win)
checkbox_frame.grid(row=1, column=0)

checkbox_label = tk.Label(checkbox_frame, text="Include:")
checkbox_label.grid(row=0, column=1, sticky="w")

letters_var = tk.BooleanVar(value=True)
letters_checkbox = tk.Checkbutton(checkbox_frame, text="letters", variable=letters_var)
letters_checkbox.grid(row=2, column=1, sticky="w")

numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(checkbox_frame, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=2, sticky="w")

special_chars_var = tk.BooleanVar(value=True)
special_chars_checkbox = tk.Checkbutton(checkbox_frame, text="Special", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=3, sticky="w", columnspan=2)

# Frame for the Generate button
generate_frame = tk.Frame(main_win)
generate_frame.grid(row=2, column=0, columnspan=2)

generate_button = tk.Button(generate_frame, text="Generate", command=validate)
generate_button.grid(row=0, column=0, padx=10)

main_win.mainloop()

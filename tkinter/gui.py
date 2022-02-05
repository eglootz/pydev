import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print("Return key or button pressed.")
    root.quit()


def focus_button(event):
    exit_button.focus()


# root window
root = tk.Tk()
root.geometry("280x100")
root.title('Login')
root.resizable(1, 1)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
username_entry.bind('<Return>', focus_button)

username_entry.focus()


# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="E")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
password_entry.bind('<Return>', focus_button)

# login button
exit_button = ttk.Button(root, text="Exit", command=lambda: root.quit())
exit_button.grid(column=1, row=3, padx=5, pady=5)


# login button
login_button = ttk.Button(root, text="Login", command=lambda: root.quit())
login_button.grid(column=0, row=3, padx=5, pady=5)


root.bind('<Return>', return_pressed)

root.mainloop()

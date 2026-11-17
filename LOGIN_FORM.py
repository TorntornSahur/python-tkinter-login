import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")
root.resizable(False, False)


bg_image = tk.PhotoImage(
    file=r"C:\Users\USER\Downloads\images.png"
)


bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title_label = tk.Label(
    root,
    text="GATES OF HEAVEN",
    font=("Arial", 20, "bold"),
    bg="#f0f2f5",
    fg="black"
)
title_label.pack(pady=5)


instruction_label = tk.Label(
    root,
    text="To enter, you must know the password.",
    font=("Arial", 12, "italic"),
    bg="#f0f2f5",
    fg="black"
)
instruction_label.pack(pady=5)


username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 11),
    bg="#f0f2f5",
    fg="black"
)
username_label.pack(pady=5)


username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5)


password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#f0f2f5",
    fg="black"
)
password_label.pack(pady=5)


password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "JESUS CHRIST" and password == "JOHN_3:16":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome to the Gates of Heaven!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid! You cannot enter the Gates of Heaven."
        )


login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=20,
    command=login
)
login_button.pack(pady=20)

# Run the application
root.mainloop()

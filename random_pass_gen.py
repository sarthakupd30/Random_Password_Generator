import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(password_length.get())
    if length < 8:
        messagebox.showwarning("Password Length", "Password length should be at least 8 characters.")
        return

    special_chars = "!@#$%^&*()_-+=<>?/[]{},.:;"
    all_chars = string.ascii_letters + string.digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    generated_password = password_entry.get()
    if generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")

title_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 18))
title_label.pack(pady=10)

title_label = tk.Label(root, text="by Sarthak Upadhyay", font=("Helvetica", 18))
title_label.pack(pady=12)

password_length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
password_length_label.pack()

password_length = tk.StringVar()
password_length.set("12")

password_length_entry = tk.Entry(root, textvariable=password_length)
password_length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, font=("Helvetica", 14), bd=0, bg="#f0f0f0")
password_entry.pack(fill=tk.X, padx=20)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()

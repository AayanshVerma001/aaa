import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_label.config(text="Password too short!")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        result_label.config(text="Enter a valid number!")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)

result_label = tk.Label(root, text="Password:")
result_label.pack(pady=10)

root.mainloop()
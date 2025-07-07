import tkinter as tk
import re

def check_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

def on_check():
    pwd = entry.get()
    strength = check_strength(pwd)
    result_label.config(text=f"Password Strength: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=on_check)
check_btn.pack(pady=5)

result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=5)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        # Simple Interest
        simple_interest = (principal * time * rate) / 100

        # Compound Interest
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        result = f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}"
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Time Period (years):").grid(row=1, column=0, padx=10, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
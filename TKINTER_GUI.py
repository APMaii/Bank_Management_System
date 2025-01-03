
import tkinter as tk
from tkinter import messagebox
import requests  # To communicate with the Flask backend API
from tkinter import ttk

class BANK:
    def __init__(self, name, age, current, PIN):
        self.name = name
        self.age = age
        self.balance = current
        self.PIN = PIN
        self.wrong_attempt = 0

    def show_balance(self, entered_pin):
        if entered_pin == self.PIN:
            return self.balance
        else:
            self.wrong_attempt += 1
            return "Incorrect PIN"

    def deposit(self, entered_pin, amount):
        if entered_pin == self.PIN:
            self.balance += amount
            return f"Deposit successful. Current balance: {self.balance}"
        else:
            self.wrong_attempt += 1
            return "Incorrect PIN"

# Create a BANK instance (this is for testing)
bank = BANK("Alice", 30, 1000, 1234)

# Function to communicate with the Flask backend
def api_request(endpoint, method="GET", data=None):
    url = f"http://127.0.0.1:5000/{endpoint}"
    if method == "POST":
        response = requests.post(url, json=data)
    else:
        response = requests.get(url)
    return response.json()

# Tkinter GUI Functions
def show_welcome():
    messagebox.showinfo("Welcome", f"Hello {bank.name}, Welcome to Plutus Bank!")
    show_balance_window()

def show_balance_window():
    def get_balance():
        pin = pin_entry.get()
        response = api_request('show_currency', method="POST", data={"password": int(pin)})
        if response["message"] == "Incorrect PIN":
            messagebox.showerror("Error", "Incorrect PIN. Try again.")
        elif response["message"] == "Your card is blocked":
            messagebox.showerror("Error", "Your card is blocked due to multiple incorrect attempts.")
        else:
            messagebox.showinfo("Balance", f"Your balance is: {response['message']}")

    balance_window = tk.Toplevel(root)
    balance_window.title("Plutus Bank - Show Balance")
    balance_window.geometry("400x300")

    tk.Label(balance_window, text="Enter PIN to view balance", font=("Arial", 14)).pack(pady=20)
    pin_entry = tk.Entry(balance_window, font=("Arial", 14), show="*")
    pin_entry.pack(pady=10)
    tk.Button(balance_window, text="Show Balance", font=("Arial", 14), command=get_balance).pack(pady=20)

def deposit_window():
    def deposit_amount():
        pin = pin_entry.get()
        amount = amount_entry.get()
        if not amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        amount = float(amount)
        response = api_request('deposit', method="POST", data={"password": int(pin), "amount": amount})
        if response["message"] == "Incorrect PIN":
            messagebox.showerror("Error", "Incorrect PIN. Try again.")
        elif response["message"] == "Your card is blocked":
            messagebox.showerror("Error", "Your card is blocked due to multiple incorrect attempts.")
        else:
            messagebox.showinfo("Deposit", f"Deposit successful! New balance: {response['message']}")

    deposit_window = tk.Toplevel(root)
    deposit_window.title("Plutus Bank - Deposit")
    deposit_window.geometry("400x300")

    tk.Label(deposit_window, text="Enter PIN to deposit", font=("Arial", 14)).pack(pady=20)
    pin_entry = tk.Entry(deposit_window, font=("Arial", 14), show="*")
    pin_entry.pack(pady=10)

    tk.Label(deposit_window, text="Enter Deposit Amount", font=("Arial", 14)).pack(pady=10)
    amount_entry = tk.Entry(deposit_window, font=("Arial", 14))
    amount_entry.pack(pady=10)

    tk.Button(deposit_window, text="Deposit", font=("Arial", 14), command=deposit_amount).pack(pady=20)

# Root window (main app window)
root = tk.Tk()
root.title("Plutus Bank")
root.geometry("600x400")
root.configure(bg="#2c3e50")

# Title label
title_label = tk.Label(root, text="Plutus Bank", font=("Arial", 30, "bold"), fg="#ecf0f1", bg="#2c3e50")
title_label.pack(pady=20)

# Welcome button
welcome_button = tk.Button(root, text="Welcome", font=("Arial", 14), fg="#ffffff", bg="#3498db", width=15, height=2, command=show_welcome)
welcome_button.pack(pady=10)

# Show balance button
balance_button = tk.Button(root, text="Show Balance", font=("Arial", 14), fg="#ffffff", bg="#3498db", width=15, height=2, command=show_balance_window)
balance_button.pack(pady=10)

# Deposit button
deposit_button = tk.Button(root, text="Deposit", font=("Arial", 14), fg="#ffffff", bg="#3498db", width=15, height=2, command=deposit_window)
deposit_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), fg="#ffffff", bg="#e74c3c", width=15, height=2, command=root.quit)
exit_button.pack(pady=20)

# Start the main loop
root.mainloop()

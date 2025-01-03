
from flask import Flask, request, jsonify

app = Flask(__name__)
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
# Create a BANK instance
bank = BANK("Alice", 30, 1000, 1234)

@app.route('/welcome', methods=['GET'])
def welcome():
    bank.welcome()
    return jsonify({"message": f"Hello dear customer, {bank.name}, welcome to Plutus Bank"})

@app.route('/show_currency', methods=['POST'])
def show_currency():
    data = request.get_json()
    password = data.get("password")
    if password == bank.PIN:
        bank.wrong_attempt = 0
        if bank.balance - 100 >= 0:
            bank.balance -= 100
            return jsonify({"message": f"Your account balance is: {bank.balance}"})
        else:
            return jsonify({"message": "Insufficient balance"})
    else:
        bank.wrong_attempt += 1
        if bank.wrong_attempt == 3:
            return jsonify({"message": "Your card is blocked"})
        return jsonify({"message": "Incorrect PIN"})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    password = data.get("password")
    amount = data.get("amount")
    if password == bank.PIN:
        bank.wrong_attempt = 0
        bank.balance += amount
        bank.transfer_history.append(f'+ {amount}')
        return jsonify({"message": f"Deposit successful! Your new balance is: {bank.balance}"})
    else:
        bank.wrong_attempt += 1
        if bank.wrong_attempt == 3:
            return jsonify({"message": "Your card is blocked"})
        return jsonify({"message": "Incorrect PIN"})

if __name__ == '__main__':
    app.run(debug=True)

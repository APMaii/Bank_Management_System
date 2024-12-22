class CURRENCY_BANK(BANK):
    def __init__(self, name, age, current, PIN, currency_id):
        super().__init__(name, age, current, PIN)
        
        self.currency_id = currency_id
        self.currency_balance = 0  # Currency balance
        
    def welcome_english(self):
        '''
        Display a welcome message in English
        '''
        name = self.name
        print(f'Hello {name}, Welcome to our Bank, PLUTUS. We appreciate your opening an account.')
        
    # amount --> How much in local currency (e.g., toman) to convert to dollars
    def change_money(self, amount):
        '''
        Handles conversion of local currency to dollars
        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 
        
        password = int(input('Please enter your PIN:'))
        if password == self.PIN:
            self.wrong_attempt = 0

            if self.balance >= amount:
                self.balance -= amount

                # Retrieve today's exchange rate
                usd = 80000  # Example rate: 1 USD = 80,000 toman
                
                # Update dollar balance
                self.currency_balance = amount / usd + self.currency_balance
                
                print(f'Successfully converted {amount} toman to {amount / usd} dollars')
                print(f'Your current dollar balance is: {self.currency_balance} dollars')
            else:
                print('Unfortunately, the balance is insufficient')
        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

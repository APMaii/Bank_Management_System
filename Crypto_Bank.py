def crypto_update():
    return [96094, 3323.84, 182.73]
    
    
    
class CRYPTO_CURRENCY_BANK(CURRENCY_BANK):
    # Create a new class from the bank
    # name, age, current, PIN are the attributes required in the base class
    # Add any new attributes here
    # Existing attributes are initialized with super()
    
    def __init__(self, name, age, current, PIN, currency_id, crypto_id):
        super().__init__(name, age, current, PIN, currency_id)
        
        self.crypto_id = crypto_id
        self.crypto_balance = 0  # Cryptocurrency balance

    # amount --> How many units are to be converted to dollars
    # Converts to dollars
    
    def change_crypto(self, amount):
        '''
        Handles cryptocurrency conversion
        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 
        
        password = int(input('Please enter your PIN:'))
        if password == self.PIN:
            self.wrong_attempt = 0
            
            if self.currency_balance >= amount:
                crypto_type = input('Which cryptocurrency would you like to convert to? :')
                crypto_list = crypto_update()
                
                if crypto_type == 'bitcoin':
                    self.currency_balance -= amount
                    crypto_amount = crypto_list[0]
                    
                elif crypto_type == 'etherium':
                    self.currency_balance -= amount
                    crypto_amount = crypto_list[1]
                    
                elif crypto_type == 'solana':
                    self.currency_balance -= amount
                    crypto_amount = crypto_list[2]
                else:
                    print('The cryptocurrency is not available')
                    return
                
                # Update cryptocurrency balance
                self.crypto_balance = amount / crypto_amount + self.crypto_balance
                
                print(f'Successfully converted {amount} dollars to {amount / crypto_amount} {crypto_type}')
                print(f'Your cryptocurrency balance is: {self.crypto_balance} {crypto_type}')
            else:
                print('Unfortunately, the balance is insufficient')
        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')
            

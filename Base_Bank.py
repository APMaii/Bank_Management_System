ADMIN_PASSWORD=8000

class BANK:

    def __init__(self, name, age, current, PIN):
        self.name = name
        self.age = age
        self.balance = current
        self.PIN = PIN
        self.wrong_attempt = 0
        self.transfer_history = []

    def welcome(self):
        '''


        '''
        thisname = self.name
        print(f'Hello dear customer, {thisname}, welcome to Plutus Bank')

    def show_currency(self):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0
            if self.balance - 100 >= 0:
                self.balance = self.balance - 100
                current = self.balance
                print('Dear customer, your account balance is:')
                print(f'{current}')
            else:
                print('You do not have sufficient balance')
        else:
            self.wrong_attempt += 1
            print('Incorrect PIN')

    def deposit(self, amount):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0
            self.balance += amount

            self.transfer_history.append(f'+ {amount}')

            print('Deposit was successful')
            print(f'Your balance: {self.balance}')
        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

    def ATM(self, amount):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0
            if self.balance - amount >= 0:
                self.transfer_history.append(f'- {amount}')
                self.balance = self.balance - amount
                print('Your withdrawal was successful')
                print(f'Your balance after withdrawal: {self.balance}')
            else:
                print('Insufficient balance')
        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

    def change_password(self):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0
            new_password = input('Enter your new PIN: ')

            if len(new_password) == 4:
                new_new_password = input('Re-enter your new PIN for confirmation: ')

                if new_password == new_new_password:
                    self.PIN = int(new_password)
                    print('Your PIN was successfully changed')

                else:
                    print('The PINs do not match, please try again')

            else:
                print('Your PIN is more than 4 digits, please try again')

        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

    def show_history(self):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0

            if len(self.transfer_history) == 0:
                print('You have no transactions')
            else:
                print('=========================')
                print('-----Your Transactions-----')
                for i in self.transfer_history:
                    print(i)
                    print('----')
                print('=========================')

        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

    def calculation(self):
        '''


        '''
        if self.wrong_attempt == 3:
            print('Your card is blocked')
            return 

        password = int(input('Please enter your PIN: '))
        if password == self.PIN:
            self.wrong_attempt = 0

            positive_values = []
            negative_values = []

            for i in self.transfer_history:
                pos_or_neg = i[0]
                if pos_or_neg == '+':
                    positive_values.append(int(i[2:]))
                if pos_or_neg == '-':
                    negative_values.append(int(i[2:]))

            all_deposition = sum(positive_values)
            all_atm = sum(negative_values)

            print('------------')
            print('Total Deposits: ', all_deposition)
            print('------------')
            print('Total Withdrawals:', all_atm)

        else:
            self.wrong_attempt += 1
            print('The entered PIN is incorrect')

    def unblock(self):
        '''
        '''
        admin_password = int(input('Please enter the admin access password: '))

        if admin_password == ADMIN_PASSWORD:
            self.wrong_attempt = 0
            print('The requested account has been successfully unblocked')

        else:
            print('Incorrect password')

        
        
    






#========================================
#========================================
#========================================
#-----------EXAMPLE USAGE----------------
#========================================
#========================================
#========================================




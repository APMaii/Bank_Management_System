class CURRENCY_BANK(BANK):
    def __init__(self,name,age,current,PIN,currency_id):
        super().__init__(name,age,current,PIN)
        
        self.currency_id=currency_id
        
        self.currency_balance=0 #ppoole arzi
        
        
    def welcome_english(self):
        
        name=self.name
        print(f'Hello {name} Welcome to our Bank, PLUTUS, We appreciate your opening account')
        
    #amount-->chan  hezar toman mikhad b dolar tabdil kone
    def change_money(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0

            if self.balance>=amount:
                
                self.balance=self.balance - amount

                #---------tabe sedash mzine
                #hamoon rooz pole dollar ro dar miare
                
                usd=80000
                
                #----------
                self.currency_balance=amount/usd+self.currency_balance
                
                print(f'Ba moafaghiat {amount} toman b {amount/usd} dollar tabdil shod')
                print(f'mojodie arze shoma : {self.currency_balance} dollar')
                
            else:
                print('motasefane mojodi kafinemibashad')

            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')

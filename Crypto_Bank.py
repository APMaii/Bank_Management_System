def crypto_update():
    return [96094, 3323.84, 182.73]
    
    
    
class CRYPTO_CURRENCY_BANK(CURRENCY_BANK):
    #boro az bank yek class jadid bsaz
    #name,age,current,PIn chizae bode k too clas avali mikahste
    #behehs chizi ezafe koni
    #harchizi k hasto jadid mikhay ro too __init___
    #harchi kghadim boode ro to super()
    
    def __init__(self,name,age,current,PIN,currency_id,crypto_id):
        super().__init__(name,age,current,PIN,currency_id)
        
        self.crypto_id=crypto_id
        
        self.crypto_balance=0 #ppoole arzi
        

    #amount-->chan  hezar toman mikhad b dolar tabdil kone
    #b dollar
    
    def change_crypto(self,amount):
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            

            if self.currency_balance>=amount:

                
                crypto_type=input('Shoma mikhahid b che ramz arzi pool tbaidl konid? :')
                
                
                crypto_list=crypto_update()
                
                if crypto_type=='bitcoin':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[0]
                    
                elif crypto_type=='etherium':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[1]
                    
                elif crypto_type=='solana':
                    self.currency_balance=self.currency_balance - amount
                    crypto_amount=crypto_list[2]
                    
                    
                    
                #-------
                
                
                else:
                    print('ramz arz mojod nemibashad')
                    
                    
                
                #----------
                self.crypto_balance=amount/crypto_amount+self.crypto_balance
                
                print(f'Ba moafaghiat {amount} dollar b {amount/crypto_amount} bitcoin tabdil shod')
                print(f'mojodie arze shoma : {self.crypto_balance} bitcoin')
                
                    
 
            else:
                print('motasefane mojodi kafinemibashad')

            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            

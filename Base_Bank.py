ADMIN_PASSWORD=8000

class BANK:

    def __init__(self,name,age,current,PIN):
        self.name=name #name beriz tooye self.name
        self.age=age
        self.balance=current
        self.PIN=PIN
        self.wrong_attempt=0
        self.transfer_history=[]

    def welcome(self):
        '''


        '''

        thisname=self.name
        print(f'salam  moshtarie aziz , {thisname} khosh amadid b banke Plutus')

    def show_currency(self):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            if self.balance-100>=0:
                self.balance=self.balance-100
                current=self.balance
                print('Moshtarie aziz mojodie hesab shoma hast :')
                print(f'{current}')
            else:
                print('shoma moojodoi mojoodi ham nadarid')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramz doros nemibashad')
        
    def deposit(self,amount):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            self.balance=self.balance + amount
            
            self.transfer_history.append(f'+ {amount}')


            print('Variz ba moafaghiat anjam shod')
            print(f'Mojoodie shoma : {self.balance}')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vared shdoe doros nmiabshad')
        
    def ATM(self,amount):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            #if self.balance-amount>=5000:
            if self.balance-amount>=0:
                
                
                self.transfer_history.append(f'- {amount}')
                
                self.balance=self.balance-amount
                print('bardashte shoma ba moafaghiat anjam shod')
                print(f'mojodie shoam bad az bardahst hast:{self.balance} ')
            else:
                print('mojoodie shoma kafi nemibashad')
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
            
    def change_password(self):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN: 
            self.wrong_attempt=0
            new_password=input('ramze jadid ra vared konid:')
            
            if len(new_password)==4:
                new_new_password=input('ramze jadide khod ra baraye taeed dobare vared konid:')
                
                if new_password==new_new_password:
                    self.PIN=int(new_password)
                    print('ramze shoma ba moafaghiat taghir kard')
 
                else:
                    print('ramzha yeksna nis, mojadadan emtehan farmaeed')
                
            else:
                print('ramze shoam bish az 4 ragham hast, mojadad az aval emtehan konid')
  
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
    def show_history(self):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            
            
            if len(self.transfer_history)==0:
                print('shoma tarakoneshi nadashtid')
                
            else:
                print('=========================')
                print('----Tarakonesh haye shoma-----')
                
                for i in self.transfer_history:
                    print(i)
                    print('----')
                
                print('=========================')
                
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
    
    def calculation(self):
        '''


        '''
        
        if self.wrong_attempt==3:
            print('karte shoma masdood mibashad')
            return 
        password=int(input('Lotfan ramzetoon ro vared namaeed:'))
        if password==self.PIN:
            self.wrong_attempt=0
            

            positive_values=[]
            negative_values=[]

            for i in self.transfer_history:
                
                pos_or_neg=i[0]
                

                if pos_or_neg=='+':
                    positive_values.append(int(i[2:]))

                if pos_or_neg=='-':
                    negative_values.append(int(i[2:]))
                    

                    
            all_deposition=sum(positive_values)
            all_atm=sum(negative_values)
            
            
            print('------------')
            
            print('Majmooe varize shoma : ',all_deposition)
            
            print('------------')
            
            print('Majmooe bardashte shoma:',all_atm)
            
        else:
            self.wrong_attempt=self.wrong_attempt+1
            print('ramze vard shdoe doros nemibashad')
            
    def unblock(self):
        '''


        '''
        
        #------- if if if if 
        #local host
        #ip 
        #kodom computer
        #user pass
        admin_password=int(input('lotfan ramze dastressie kolie hesab haro vared namaeed:'))
        
        if admin_password==ADMIN_PASSWORD:
            self.wrong_attempt=0
            print('hesabe morede nazar ba moafaghiat az masdoodiat raha shod')

        else:
            print('ramz doros nemibashad')
        
        
    






#========================================
#========================================
#========================================
#-----------EXAMPLE USAGE----------------
#========================================
#========================================
#========================================




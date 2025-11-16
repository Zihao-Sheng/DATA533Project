class budgetfund: #this is the class for the whole budget of the family
    log_title=['action','amount','description','balance','status']
    
    def __init__(self,opening_balance,name=''):
        self.opening_balance=float(opening_balance)
        self.__balance=float(opening_balance)
        self.household_name=name
        self.__log=[]
        
    def validate(self,amount=0): #see if the balance is larger or equal to a certain amount,if no value entered, check if the account is in debt
        if self.__balance>=float(amount):
            return True
        return False
        
    def add(self,amount,desciption=''):
        self.__balance+=float(amount)
        self.__log.append(['add',amount,desciption,self.get(),'succeeded'])
        return True
        
    def sub(self,amount,desciption=''):
        if self.validate(amount):
            self.__balance-=float(amount)
            self.__log.append(['sub',amount,desciption,self.get(),'succeeded'])
            return True
        self.__log.append(['sub',amount,desciption,self.get(),'failed'])
        return False
            
    def get(self):
        return self.__balance
        
    def get_log(self):
        return [self.log_title,self.__log]
    
    def __str__(self):
        return('The family budget of '+ self.household_name +' is: '+ str(self.get()))
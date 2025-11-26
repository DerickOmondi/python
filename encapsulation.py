class BankAccount:
    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    
    def set_balance(self,balance):
        if balance >0:
            self.__balance = balance

        else:
            print('Your Account is Too low') 
    
BankAccount1 = BankAccount('Derick',50000)
BankAccount1.get_balance()

BankAccount1.set_balance(100000)
print(BankAccount1.get_balance())
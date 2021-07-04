class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
    	self.account_balance += amount	
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("User:" , self.name)
        print("Balance:" , self.account_balance)
    # def transfer(self, other_user, amount)
    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount

pete = User("Pete Dort" , "pete@python.com")
jim = User("Jim Dean", "jim@python.com")
george = User("George Morten", "george@python.com")

print(pete.name)
print(jim.name)
print(george.name)

pete.make_deposit(50)
pete.make_deposit(150)
pete.make_deposit(100)
pete.make_withdrawal(75)
print("Pete's Balance:" , pete.account_balance)

jim.make_deposit(200)
jim.make_deposit(10)
jim.make_withdrawal(85)
print("Jim's Balance:" , jim.account_balance)

george.make_deposit(400)
george.make_withdrawal(50)
george.make_withdrawal(5)
george.make_withdrawal(15)
print("George's Balance:" , george.account_balance)

pete.transfer_money(george, 100)
print("Pete's Balance:" , pete.account_balance)
print("George's Balance:" , george.account_balance)



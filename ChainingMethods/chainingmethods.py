class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self	
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User:" , self.name)
        print("Balance:" , self.account_balance)
        return self
    # def transfer(self, other_user, amount)
    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

pete = User("Pete Dort" , "pete@python.com")
jim = User("Jim Dean", "jim@python.com")
george = User("George Morten", "george@python.com")

print(pete.name)
print(jim.name)
print(george.name)

pete.make_deposit(50).make_deposit(150).make_deposit(100).make_withdrawal(75).display_user_balance()

jim.make_deposit(200).make_deposit(10).make_withdrawal(85).display_user_balance()

pete.transfer_money(george, 100).display_user_balance()
george.display_user_balance()




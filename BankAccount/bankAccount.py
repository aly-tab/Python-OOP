class BankAccount:

	accounts =[]

	def __init__(self, int_rate, balance): 
		self.int_rate = 0.01
		if (balance == ''):
			self.balance = 0
		else: 
			self.balance = balance
		BankAccount.accounts.append(self)

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		self.balance -= amount
		if (self.balance < 0):
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self

	def display_account_info(self):
		print("Balance:" , self.balance)
		return self

	def yield_interest(self):
		self.balance += self.balance * self.int_rate
		return self

	@classmethod
	def print_instances(cls):
		for account in cls.accounts:
			print("Balance:" , account.balance , "- Interest Rate:" ,account.int_rate)

pete = BankAccount('', '')

pete.deposit(500).deposit(300).deposit(200).yield_interest().display_account_info()

clark = BankAccount('', 300)

clark.deposit(400).deposit(200).withdraw(50).withdraw(450).withdraw(300).withdraw(1000).yield_interest().display_account_info()

BankAccount.print_instances()
class Account:
	interest = 0.02
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if self.balance < amount:
			return 'chi xi wang xiang'
		self.balance -= amount
		return self.balance

class CheckingAccount(Account):
	interest = 0.01
	withdraw_fee = 1
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
	"""
	A bank has accounts and pays interest
	>>> bank = Bank()
	>>> yue = bank.open_account('yue', 100)
	>>> lls = bank.open_account('lls', 10, CheckingAccount)
	>>> yue.interest
	0.02
	>>> lls.interest
	0.01
	>>> bank.pay_interest()
	>>> yue.balance
	102.0
	>>> lls.balance
	10.1
	"""
	def __init__(self):
		self.accounts = [] 

	def open_account(self, holder, amount, account_type = Account):
		account = account_type(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		for account in self.accounts:
			account.deposit(account.balance * account.interest)







class Account:
	"""
	>>> a = Account('lls')
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'chi xi wang xiang'
	>>> a.balance
	10
	"""

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			return 'chi xi wang xiang'
		self.balance = self.balance - amount
		return self.balance


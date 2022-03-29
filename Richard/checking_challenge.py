print('Question 1')

class CheckingAccount():
	def __init__(self, account_holder, account_number):
		self.account_holder = account_holder
		self.account_number = account_number
		self.balance = 0
		self.withdrawal_limit = 2000

	def deposit(self, amount):
		# self.amount = amount
		try:
			self.balance += amount	
			return self.balance
		except:
			print('system error deposit amount not valid')


	def withdraw(self, amount):
		# self.amount = amount
		try:
			if amount > self.withdrawal_limit:
				print("Withdrawal amount exceeds the max withdrawal limit")
			elif amount > self.balance:
				print("insufficient funds")
			else:
				self.balance -= amount
				return self.balance
		except:
			print('system error withdrawal amount not valid')



'''
	1.1 Create method 'deposit' that adds to the account balance
		- Parameter: amount (int or float)
		- Returns: balance (after adding amount)
'''

'''
	1.2 Create method 'withdraw' that subtracts from the account balance
		- Parameter: amount (int or float)
		- Returns: balance (after subtracting amount)

	Additional requirements:
		- Add an attribute during initialization 'withdrawal_limit' with 2000 set as it's default
		- If amount exceeds the current balance, print 'Insufficient funds'
		- If amount exceeds the withdrawal_limit, print 'Withdrawal amount exceeds the max withdrawal limit'
'''


print('')

print('Question 2')

# 2.1 Create a checking account using CheckingAccount class, use your name and add a random number for initialization
# 2.2 Deposit the amount of 1500
# 2.3 Withdraw the amount of 4000
# 2.4 Print the account balance

'''
class CheckingAccount():
	def __init__(self, name, number):
		self.name = name
		self.number = number
'''

my_account = CheckingAccount('Richard','939393')
print(my_account.account_holder)
print(my_account.account_number)
print(my_account.balance)

my_account.deposit(3442)
print(my_account.account_holder)
print(my_account.account_number)
print(my_account.balance)

print('')

print('Question 3')

# Currently, if you pass non int or float values, the methods 'deposit' and 'withdraw' will error out

# 3.1 - In the 'deposit' method, handle exceptions by wrapping code block with try/except.
# If an exception occurs, print 'System Error: Deposit amount not valid'

my_account.deposit(3442.34)
print(my_account.balance)

my_account.deposit('2349')
print(my_account.balance)

my_account.withdraw(3442.34)
print(my_account.balance)

my_account.withdraw('2349')
print(my_account.balance)


# 3.2 - Call the deposit method with the argument: 'cats' (string)

my_account.deposit('cats')
print(my_account.balance)

# 3.3 - In the 'withdraw' method, handle exceptions by wrapping code block with try/except.
# If an exception occurs, print 'System Error: Withdrawal amount not valid'

# 3.4 - Call the withdraw method with the argument: {} (dictionary)

print('')
my_account.withdraw({})
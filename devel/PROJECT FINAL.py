from random import randint
class Main:
	balance = 100
	loanA = 1000
	income = 0
	month = 0
	def test():
		print ('What is your action')
		x = input('')
		if(x=="loan"):
			Main.loan()
		elif(x=="invest"):
			Main.invest()
		elif(x=="skip"):
			Main.skip()
		else:
			print("Invalid argument")
			Main.test()
		
	def loan():
		print ('Type the desired loan amount')
		x = int(input(''))
		if(x<Main.loanA):
			Main.balance=Main.balance+x
			Main.loanA=Main.loanA-x
		else:
			print("You can'loan that much")
			Main.test()
	def invest():
		print ('Invest secure or risk')
		x = input('')
		if(x=="secure"):
			Main.investS()
		elif(x=="risk"):
			Main.investR()
		else:
			print ("Invalid argument")
			Main.invest()
	def investS():
		print ('How much do you want to invest?')
		amount = int(input(''))
		if(amount<=Main.balance):
			Main.balance=Main.balance-amount
			random =randint(0,10)
			if(random<=8):
				Main.income=amount*1.10
				print("You successfully invested and your income is %d" % Main.income)
			else:
				print("You lost your money")
		else:
			print("Insufficient amount")
			Main.investS()
	def investR():
		print ('How much do you want to invest?')
		amount = int(input(''))
		if(amount<=Main.balance):
			Main.balance=Main.balance-amount
			random =randint(0,10)
			if(random>=8):
				print("You successfully invested and your income is %d" % Main.income)
				Main.income=amount*1.8
			else:
				print("You lost your money")
		else:
			print("Insufficient amount")
			Main.investR()
		
	def skip():
		print("You skipped your month")

while Main.balance>=0 or Main.month==40:
	Main.balance+=Main.income
	print ("%d month passed" % Main.month)
	print ("Your balance: %d" % Main.balance)
	print ("Available loan: %d" % Main.loanA)
	print ("Your income: %d" % Main.income)
	Main.test()
	Main.month+=1
if(Main.balance<0):
	print("You went bankrupt")
else:
	print("You made %d money" % Main.balance)
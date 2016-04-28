from random import randint

print('You can invest into a secure or risk, secure will have lower income for winning while risk will have higher income for winning.')
print('You can also recieve a loan up to 1000 in total to increase profit, after you win a investment it will go into income, each time you type skip you will recieve your income but a months time will pass.')
print('The goal is to reach as much money as possible before month 40.')
print('You may now begin.')

from random import randint
class Bank:
	balance = 100 #starting variables
	loanA = 1000
	income = 0
	month = 0
	def test(self): #main execution
		print ('What is your action? (invest,loan,skip')
		x = input('')
		if(x=="loan"): # if loan then jump to method loan
			self.loan()
		elif(x=="invest"): # if invest jump to method invest
			self.invest()
		elif(x=="skip"): # if skip jump to method skip which is empty
			self.skip()
		else:
			print("Invalid argument")
			self.test() # this is a recursion, basically a method that calls itself, if the user is typing a invalid command.
		
	def loan(self): 
		print ('Type the desired loan amount')
		x = int(input(''))
		if(x<self.loanA): #checks if the amount doesn't exceed the loanA, if it does it repeats
			self.balance=self.getBalance()+x # subtracts your overall loan, and adds it to your blance
			self.loanA=self.getLoanA()-x
		else:
			print("You can'loan that much")
			self.test() 
	def invest(self):
		print ('Invest secure or risk')
		x = input('')
		if(x=="secure"): # if secure then jump to investS
			self.investType(0.8)
		elif(x=="risk"): # if risk then jump to investR, risk percentage applies in investype where I do the calculations
			self.investType(0.2)
	def investType(self,riskPercentage):
		print ('How much do you want to invest?')
		amount = int(input(''))
		if(amount<=self.balance): # same check as in loan method
			self.balance=self.getBalance()-amount #balance reduces depending on the invest amount
			random =randint(1,10)#random number from 1-10
			if(random<=riskPercentage*10): #checks if the number is in the range of your risk percentage
				self.income=amount*(riskPercentage+1)
				print("You successfully invested and your income is %d" % self.getIncome())
			else:
				print("You lost your money")
		else:
			print("Insufficient amount")
			self.investType()	
	def skip():
		print("You skipped your month")
	def getBalance(self):
		return self.balance
	def getIncome(self):
		return self.income
	def getMonth(self):
		return self.month
	def getLoanA(self):
		return self.loanA
bank = Bank()
while bank.getBalance()>=0 or bank.getMonth()==40: # if the user has negative money or 40 months has passed then finish the game.
	print ("%d month passed" % bank.getMonth())
	print ("Your balance: %d" % bank.getBalance())
	print ("Available loan: %d" % bank.getLoanA())
	print ("Your income: %d" % bank.getIncome())
	Balance = bank.getBalance()
	Balance+=bank.getIncome()
	bank.test()
	month = bank.getMonth()
	month+=1 # increments every month
if(bank.getBalance()<0):
	print("You went bankrupt") #prints if the user went minus ( out of money )
else:
	print("You made %d money" % bank.getBalance()) # prints the balance


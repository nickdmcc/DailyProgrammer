#Challenge 2
#Nicholas McCarty
"""
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. 

It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!
"""

import math, sys

def or_tax():
	filer = input("Are you filing as (S)ingle, (J)oint, or (H)ead of household?: ")
	bracket = (int(input("How much income are you making annually?: ")))
	if filer == 's' or filer == 'S':
		if bracket <= 3400:
			tax = bracket * .05
		elif bracket <= 8500:
			tax = bracket * .07
		elif bracket <= 125000:
			tax = bracket * .09
		elif bracket > 125000:
			tax = bracket * .099
		else:
			print("You need to input a number greater than 0")
	elif filer == 'j' or filer == 'J' or filer == 'h' or filer == 'H':
		if bracket <= 6800:
			tax = bracket * .05
		elif bracket <= 17000:
			tax = bracket * .07
		elif bracket <= 250000:
			tax = bracket * .09
		elif bracket > 250000:
			tax = bracket * .099
		else:
			print("You need to input a number greater than 0")
			sys.exit()
	else:
		print("You need to input the letter indicated inside of the parenthesis")
		sys.exit()
	
	print()
	print("Your taxable income from $%d is going to be $%d!" %(bracket, tax))

def estate_tax():
	ans = input("Do you own an estate worth at least a million dollars? (Y)es or (N)o?: ")
	if ans == 'y' or ans == "Y":
		estate = (int(input("How much is the estate valued at?: ")))
		if estate >=1000000 and estate <=1500000:
			tax = estate * .1
		elif estate <= 2500000:
			tax = estate * .1025
		elif estate <= 3500000:
			tax = estate * .105
		elif estate <= 4500000:
			tax = estate * .11
		elif estate <= 5500000:
			tax = estate * .115
		elif estate <= 6500000:
			tax = estate * .12
		elif estate <= 7500000:
			tax = estate * .13
		elif estate <= 8500000:
			tax = estate * .14
		elif estate <= 9500000:
			tax = estate * .15
		elif estate > 9500000:
			tax = estate * .16
		else:
			print("You did not enter a value over 1000000.")
			sys.exit()
	elif ans == 'n' or ans == 'N':
		print("No tax is filable then!")
		sys.exit()
	else:
		print("You didn't enter a 'Y' or 'N'.")
		sys.exit()
	
	print()
	print("Your estate valued at $%d is taxable; the tax being $%d!" %(estate, tax))

or_tax()
estate_tax()
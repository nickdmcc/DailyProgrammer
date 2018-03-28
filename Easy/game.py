import sys, time, random

def game():
	print("Hello! Welcome to 'Guess the Number!'")
	number = int(input("Choose a number between 0 and 100!: "))
	print("Ok, let me think...")
	time.sleep(2)
	guess = random.randint(0, 100)
	print("Ok, is it %d?" %(guess))
	ans = input("(Y)es, or (N)o?: ")
	if ans == 'Y' or ans == 'y':
		print("Ha, we are smarter than you!")
	elif ans == 'N' or ans == 'n':
		print("Oh...")
		time.sleep(2)
		ans = input("Is it (H)igher or (L)ower than %d?: " %(guess))
		if ans == 'H' or ans == 'h':
			guess = random.randint(guess + 1, 100)
		elif ans == 'L' or ans == 'l':
			guess = random.randint(0, guess - 1)
		else:
			print("You didn't choose the right option, so we are cheating, the correct number was %d" %(number))
			sys.exit()
		print("We got this now, is it %d?" %(guess))
		ans = input("(Y)es, or (N)o?: ")
		if ans == 'Y' or ans == 'y':
			print("Ha, we are smarter than you!")
		elif ans == 'N' or ans == 'n':
			print("Oh...")
			time.sleep(4)
			print("Ok... Last guess...")
			time.sleep(2)
			ans = input("Is it (H)igher or (L)ower than %d?: " %(guess))
			if ans == 'H' or ans == 'h':
				guess = random.randint(guess + 1, number)
			elif ans == 'L' or ans == 'l':
				guess = random.randint(number, guess - 1)
			else:
				print("You didn't choose the right option, so we are cheating, the correct number was %d" %(number))
				sys.exit()
			print("For sure! The answer is clearly %d!" %(guess))
			time.sleep(1)
			print("Right?")
			time.sleep(1)
			ans = input("(Y)es, or (N)o?: ")
			if ans == 'Y' or ans == 'y':
				print("Ha, we are smarter than you!")
			elif ans == 'N' or ans == 'n':
				print("I give up, the answer isn't a real number.")
				print("You win!")
	else:
		print("You can't even choose a simple option, we are still smarter than you.")

game()
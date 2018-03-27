#Challenge 1
#Nicholas McCarty 3/26/18

"""create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.
"""
import sys #to use input

def main():
	name = input("What is your name?: ")
	age = input("What is your age?: ")
	reddit_name = input("What is your reddit username?: ")
	
	print("your name is " + name + ", you are " + age + " years old, and your username is " + reddit_name)
	save(name, age, reddit_name)

def save(name, age, reddit_name):
	file = "saveUserInfo.txt"
	wr = open(file, 'w')
	wr.write("your name is " + name + ", you are " + age + " years old, and your username is " + reddit_name)

main()
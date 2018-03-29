#Challenge 3
#Nicholas McCarty

"""
Welcome to cipher day!

write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!
"""

import sys #for user input
from string import ascii_lowercase #for saving time typing out all the letters

def caesar(text, shift):
	alphabet = ascii_lowercase
	shifted_alphabet = alphabet[shift:] + alphabet[:shift] #uses lists to start at index 'shift' and append up to index 'shift' of the alphabet
	table = str.maketrans(alphabet, shifted_alphabet) #maps first param to second param (both must have same length)
	return text.translate(table)

text = input("What is your message?: ")
shift = int(input("What is the shift to be? (between 0 and 25): "))

message = caesar(text, shift)
print(text)
print(message)
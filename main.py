"""
Group 4: David Vaughn, Daniel Miller, Ben Gubbins
CSE 5408, Spring 2022, Lab 4

Prompt user for input, and store into a variable
Use the .join() and reversed() functions to cycle through the
string from the back to the front, and place each character into
a new string, then display the new string.
"""

# Prompt user for input, store into variable
getInput = (input("Type some text: "))

unoReverse = ''.join(reversed(getInput))

print(unoReverse)

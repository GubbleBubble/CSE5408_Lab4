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

#Part B by Ben Gubbins
num = int(input('Enter a number: '))#get number input
prime = 1#variable to track whether prime
for x in range(2,num):#iterate through all numbers less than or equal to the given number
    if num%x==0: #check if the current value of x is a divisor of the given number
        prime = 0
if prime:#print if the number is prime or not
	print(num, "is prime.")
else:
	print(num, "is not prime.")


##PART C##
num12 = str(input("Enter your time in the 12 hour format xxxx: "))
if len(num12) > 4:
    print("!!Invalid input exiting program!!")
    exit()
ampm = int(input("Enter a 0 if your time is am, and a 1 if it is pm: "))
if ampm != 0 and ampm !=1:
    print("!!Invalid input exiting program!!")
    exit()
num24 = 0
standard_p1 = num12[0] + num12[1]
standard_p2 = num12[2] + num12[3]
standard = str(standard_p1) + ":" + str(standard_p2)
if ampm == 0: ##This is the Am addition
    num24 = int(num12)
    print("Current time: " + standard + "\n" + "Military Time: " + str(num24))
elif ampm == 1: ##This is the PM addition
    num24 = int(num12) + 1200
    print("Current time: " + standard + "\n" + "Military Time: " + str(num24))
else:
    print("!!Invalid input exiting program!!")

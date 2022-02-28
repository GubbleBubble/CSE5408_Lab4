
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

import math
import datetime

# print(math.factorial(5))
# print(math.trunc(2.65))
# x = datetime.datetime(2026,6,2)
# print(x)
# print(x.year)


import random
cnum=random.randrange(0,100)
unum = int(input("Enter Your NUmber:"))
if cnum > unum:
    print("Computer number", cnum,"Is greater")
elif unum > cnum:
    print("Computer number ", cnum, "IS smaller")  
else:
    print("Computer number", cnum, "IS number")      
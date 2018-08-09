from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
print(current_year)
print(current_month)
your_name = input("Enter your name:")
your_age = int(input("Enter your age:"))
if (your_age>100):
    print("you are too old")
else:
    turn_hundred = 100 - your_age
    year = current_year + turn_hundred
    n = int(input("enter a number:"))
    print("hello %s, you will turn 100 in %d \n" %(your_name,year)*n)

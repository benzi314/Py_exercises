#This is a number guessing game
import random 
usr_a = input ("Enter your name:")
num = random.randint(0,9)
num = int(num)
num_a = int(input("Guess the number: "))
i = 0
while num_a != num:
    if num_a > num:
        print("Guess a little low number:")
        num_a = int(input("Guess the number: "))
        i = i+1
    elif num_a < num:
        print("Guess a little high number:")
        num_a = int (input("Guess the number: "))
        i = i+1
    else:
        break
print(usr_a + ", have guessed the right number and the number is %d" %num)
print(usr_a + " guessed in %d times" %(i+1))

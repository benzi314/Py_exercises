#String and number is a palindrome or not
word = input("Enter the Word:")
word = str (word)
revs = word[::-1]
if (word == revs):
    print("%s is a palindrome" %word)
else:
    print("%s is not a palindrome" %word)
num = str (input("Enter the number:"))
revs1 = num[::-1]
if (num == revs1):
    print("%s is a palindrome" %num)
else:
    print("%s is not a palindrome" %num)
    

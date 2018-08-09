# this program finds out odd or even number
x = int (input("Enter the number:"))
if (x%2 == 0):
    print("%d is an even number" %x)
else:
    print("%d is an odd number" %x)
#below codes finds the multiple of 4
if (x%4 == 0):
    print ("4 divides %d exactly" %x)
#below codes check the divisibilty of a number
num = int (input("Enter the number (dividend):"))
check = int (input("Enter a number (divisor:"))
if (num%check == 0):
             print("%d divides %d exactly" %(check,num))
else:
             print("%d does not divide %d exactly" %(check,num))

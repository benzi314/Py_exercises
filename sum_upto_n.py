# sum upto first n natural numbers

sum = 0.0
n = int(input("enter the number:"))
i = 0
while i <= n:
    sum = sum + i
    i = i + 1
print ("the sum upto %d is %d" %(n,sum))
formulae = n*(n+1)/2
print (formulae)

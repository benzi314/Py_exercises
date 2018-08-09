#finding out the divisors of a given number
y = int(input("Emter the number:"))
x = range(2,y)
divisors = []
i=2
for i in x:
        if y%i ==0:
               divisors.append(i)
        i = i+1
print("The divisors of %d are" %y)
print(divisors)

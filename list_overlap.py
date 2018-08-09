#This program illustrates the concept of lists overlap
import random
x = int (input("Enter the length of first list:"))
y = int (input("Enter the length of second list:"))
a = (random.sample(range(1,100),x))
b = (random.sample(range(1,100),y))
c = set(a)
d = set(b)
print("The first list is: %s"  %c)
print("The second list is: %s" %d)
new_list = []
for x in a:
    for y in b:
        if x==y:
            new_list.append(x)
print("The overlapped elements are:")
print(new_list)


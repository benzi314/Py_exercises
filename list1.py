#This program is for practicing lists
#Take a list, say for example this one:
#a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.
a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = len(a)
new1 = []
print ("Number of elements in a is %d" %b)
for i in range (0,b):
    if a[i]<5:
        new1.append(a[i])
print(new1)
#below codes requires user to enter the list
new =[]
for i in range(0,10):
    x = int(input("enter the %d th element of the list:" %i))
    new.append(x)
print(new)
new2 = []
for i in range(0,len(new)):
    if new[i]<5:
        new2.append(new[i])
print(new2)

#list comprehensions
#printing only even numbers in a list
import random
y = int(input("Enter the number of elements in the list:"))
x = (random.sample(range(1,100),y))
print(x)
new_list1=[]
new_list2=[]
for i in x:
    if i%2 == 0:
        new_list1.append(i)
    else:
        new_list2.append(i)
print("The even elements are: ")
print(new_list1)
print("The odd elements are: ")
print(new_list2)
    

# Control Flow

#If statement 
temperature = 12
if temperature > 30:
    print("It's warm")

#ELSE Statement
temperature = 23
if temperature > 30:
    print("It's warm")
else:
    print("It's cold")
print("Done")

#ELIF Statement
temperature = 12
if temperature > 30:
    print("It's warm")
elif temperature > 20:
    print("it's nice")
else:
    print("It's cold")
print("Done")

#Nested If Statement
age = 17
own_car = 'False'

if (age >= 18):

    if (own_car == "True"):
        print("Eligible for driving")

    else: 
        print("Purchase a car")

else:
    print ("Not eligible for driving")

#List
marks = [95, 94, 59 , 35, 80, 75]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
 
#It can store multiple data types and also mutable
students = ["Ali", 45, "Osama"]
print(students[0])
students[0] = "Ahsan"
print(students)

#List Slicing
Fruites = ["Apple", "Banana", "Watermelon", "Lemon" ]
print(Fruites[1:3])

# append() - adds an element at the end
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)

# insert() - adds element at specific position
fruits.insert(1, 'blueberry')
print(fruits)

# remove() - removes first matching value
fruits.remove('banana')
print(fruits)

# pop() - removes the item at index
fruits.pop(1)  
print(fruits)

# sort() - sorts list in place in asscending order
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)

#sort in descending order
numbers.sort(reverse=True)

# reverse() - reverses list in place
numbers.reverse()
print(numbers)  

#Tuple
#It is not mutable
#To write tuples it is compulsory to data with single comma
tup = [2, 1, 3, 5, 6]
print(tup)
print(type(tup))
print(tup[0])
print(tup[2])

#Tuple Slicing
num = [2, 3, 5, 6, 7, 9 ]
print(num[1:3])

# count() - counts occurrences of a value
int = (1, 2, 3, 2, 2, 4)
print(int.count(2))

# index() - returns first index of a value
print(int.index(2))


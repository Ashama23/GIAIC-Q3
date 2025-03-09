#arthemetic operators 
a = 2
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #reminder
print(a ** b) #a^b

#Rational Operators
a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#Assignment Operators
num = 10
num += 10
print("num :", num) #20

num = 10
num -= 10
print("num :", num) #0

num = 10
num *= 10
print("num :", num) #100

num = 10
num /= 10
print("num :", num) #0

num = 10
num %= 5
print("num :", num) #0

num = 10
num **= 5
print("num :", num) #1,00,000


#Logical Operators
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = False
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", (a == b) or (a > b))

#Identity Operators

a = 5
b = 5
print(a is b)
print(a is not b)

#Membership Operators

numbers = [23, 24, 245, 45, 65, 76, 45]
num = 45
print (num in numbers) #True

x = 4
numbers = [1,2,3,5,8,9,0]
print(x not in numbers) #False

#Bitwise Operators 

a = 5
b = 4
print(a & b)

a = 10
b = 5
print(a | b)

a = 10
print(~a)

a = 10
b = 9
print(a ^ b)
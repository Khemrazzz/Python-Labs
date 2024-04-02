
import sys 
print(sys.version)

if 5 > 2 : #little demo
    print("Five is greater than two") #comment input 

    """
    servi 3 kut double quotes 
    pou met gros comment 

    """


print("hello world") 

x = 5
y = ("Nev") #assigning values to variables 

print(x) #printing the values of the variables 
print(y)

"""
#Registration for a patient changing hospital for some reasons 
name = input("what is your name ?\n")
print("Dear " + name)
age = input("What is your age ?\n")
print(name + " is registered as new patient.")
follow_ups = input("For how many years have you been following treatments ?\n")
treatment_period = 2024 - int(follow_ups)
print("Patient named " + name + " has been diagnosed since " + str(treatment_period))
"""

"""
#performing mathematical calculations

num_1 = input("Enter number 1\n")        #int() = 99  float() = 45.555 bool() =   str = "err"
num_2 = input("Enter number 2\n")

sum = float(num_1) + int(num_2) #using float to calculate decimal number 
print("sum = " + str(sum))

print(10 + 33)
print(10 - 22)
print(10/2)
print(10/3)
print(10//3)
print(10*2)
print(10%4)
print(10**2)

z = 10
z += 3 # works same as z = z + 3
print(z)

"""
"""
course = " i am in a big mess"

print(course.upper())
print(course.find("s"))
print(course.replace("mess", "trouble"))
print("am" in course)
print("zero" in course)

"""

"""
x = 3>2
print(x)

price = 21

print(price > 12 and price < 25) # and , or 
print(not price > 40)

if price > 30 :
    print("over-rated")
else :
    print("correct price")

# use of elif : ..... reduces else .. if

"""
"""
print("Enter 10 numbers:\n")
count = 0
total = 0

for i in range(10):
    print("Enter a number (",i,")...")
    number = int(input())
    total += number
    count += 1

    print("Total = " + str(total))
    print("Count = " + str(count))

#for loop
"""

"""
#while loop 

count = 0
total = 0
print("Enter a list of numbers in your sheet")
number = float(input())
while number >= 0 :
    count += 1
    total += number
    print("Enter next number...")
    number = float(input())
print("Total = ", total, "and count = ", count) # instead of + ...... , can be used for concatenation"

"""
"""
i = 1

while  i <= 20 :
    print(i * "*")
    i *= 2
"""
"""
#lists 

names = ["jo", "lo", "ho", "po", "ni", "no", "pi" , "pe"]
nums = [3, 4, 6, 7, 8, 9, 0, 78, 6]
names[0] = "oG"
print(names)
print(names[2])
print(names[-3])
print(names[0])
print(names[0:4])

print(0 in nums)
print(12 in nums)
print(len(names))

"""

import numpy as np

numarray = np.zeros(10)   # create an empty 10 element array 
print("Enter 10 numbers:/n")

for i in range(len(numarray)):
    print("Enter a number (",i,")")
    numarray[i] = float(input())
print("Total is", numarray.sum())
print(numarray)




"""
print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())
    
print('Total is ', numarray.sum())

"""
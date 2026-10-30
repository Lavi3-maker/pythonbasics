# A pyhton program that checks if a person is elegible to vote
age=int(input("Enter your age"))

if  age >=18:
    print("You ar eligible to vote")
else:
    print("You ar not eligible to vote too young")

# A python program to check if a number is odd or even
# create a python script that check the largest in three input using input output

num=int(input("Enter a number"))
if num % 2==0:
    print("The number is even")
else: 
    print("The number is odd")

number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))
if number1 > number2:
    largest_number=number1
else: largest_number = number2
if largest_number > number3:
    largest = largest_number
else: largest = number3
print(f"The largest number is: {largest}")


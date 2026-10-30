def greet():
    print("Welcome to pixel class!!")
greet()
greet()
# function with parameters
def student(name,age):
    print(f"My name is {name} and I am {age} years old ")
student("Lavender",28)

# function using input output
def add_numbers(a,b):
    return a+b
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

result=add_numbers(num1,num2)
print(f"The sum is {result}")

# create a program that gives 10% discount
def calculate_dicount(price):
    discount=price*0.10
    final_price=price-discount
    return final_price
price=float(input("Enter your product price:"))
total=calculate_dicount(price)
print(f"Price after discount:{total}")


# List datastructures
# mutable/changeable
# has indexed

products=["Bread","Milk","Sugar","Blueband"]
print(f"My products {products}")
products[0]="Cake"

products[0]="Cake"
print(f"Update products {products}")

products.pop()
print(products)
for p in products:
    print(p)
# tuple datastructure
# immutable, unchangeable

location=("Nairobi", "Uganda","Tanzania")
# location[1]="Burunda"
print(location)

# set datastructure
# removes duplicates
mystock={"hp","Lenovo","dell","hp"}
print(mystock)

# dictionary datastructures
customer={
    "name":"Eric",
    "age":30,
    "city":"Nairobi",
    "proffesion":"Software Engineer"
}

print(f"Name: {customer['name']}")

# store products and their prices
shop={
    "Bread": 130,
    "Milk": 90,
    "Sugar": 190
}
for product ,price in shop.items():
    print(product,"cost Ksh",price)
print("Milk cost Ksh", shop["Milk"])

# imagine you are building a school system 
# that calculates the average mark of a student
marks=[76,83,67,90,79]
total=0
for mark in marks:
    total=total+mark
average=total / len(marks)
print(f"Total Marks :{total}")
print(f"Average Marks :{average}")

# create a complex
# calculator using input output and loops
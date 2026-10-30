# class Student:
#     name="Lavender"
#     age=25
# # object 
# student1=Student()
# print(f"Name of student: {student1.name}")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("Lavender",25)
student2=Student("Cherop",19)

print(student1.name)
print(student1.age)

# inheritance 
class Animal:
    def speak(self):
        print("Animal Speaking")

# child class 
class Dog(Animal):
    def bark(self):
        print("Dog barking")

#creating object

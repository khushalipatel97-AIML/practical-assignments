# 17. Create a class Person and inherit it into a Student class.
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
class Person(Student):
    def __init__(self, name, roll_no, age):
        # Inherit values from Student class
        super().__init__(name, roll_no)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Age:", self.age)

p1 = Person("Khushali", 101, 20)
p1.display();
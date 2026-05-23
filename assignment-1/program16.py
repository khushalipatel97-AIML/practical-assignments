# 16. Create a class Student with attributes and a method to calculate average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # marks should be a list

    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        return average
    
student1 = Student("Khushali", [85, 90, 78, 92])
print("Student Name:", student1.name)
print("Average Marks:", student1.calculate_average())

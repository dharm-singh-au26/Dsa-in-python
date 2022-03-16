"""
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
"""

class Student :
    def __init__(self,name,roll_number,age,marks):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.marks = marks
    
    def Display(self):
        print(self.name) 
        print(self.roll_number)
    
    def setAge(self):
        print(self.age)
    def setMarks(self):
        print(self.marks)

S = Student("Dharm",789542,22,540)
print(S.Display(),S.setAge(),S.setMarks())

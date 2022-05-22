class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print("Hello My Name is: ", self.name)
        print('My Rollno is: ', self.rollno)

s=Student('Durga', 101)
s.display()
print("---", s.name, s.rollno)

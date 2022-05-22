class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def talk(self):
        print("Hello My Name is : " , self.name)
        print("My Rollno is: ", self.rollno)


s = Student(100, "Venky")

s.talk()
print(s.name)
print(s.rollno)

r = Student(200, "Bunny")
r.talk()

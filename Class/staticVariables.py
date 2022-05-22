class Student:
    cname='DURGASOFT' # static varible

    def __init__(self, name, rollno):
        self.name = name      # instant Varible
        self.rollno = rollno   # instant Varible
        Student.branch = "ECE"  #static varible

    def m1(self):
        Student.class = "Maths" # static Variables


s1 = Student('Durga', 101)
s2 = Student('Pavan', 102)

print(s1.name, s1.rollno, Student.cname)
print(s2.name, s2.rollno, Student.cname)

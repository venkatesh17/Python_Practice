class Student:
    school = 'Telusko'
    def __init__(self,m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def get_school(cls):
        return cls


s1 = Student(34, 47, 32)

print(s1.avg())
print(s1.get_m1())
print(Student.get_school('s33'))





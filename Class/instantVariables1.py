class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        self.d = 40

    def m2(self):
        self.e = 50



t1 = Test()
t1.m1()
t2 = Test()
t2.m2()
t2.s = 200
t2.y = 300
print(t1.__dict__)
print(t2.__dict__)

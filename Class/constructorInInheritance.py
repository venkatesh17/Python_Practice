class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):
        print("in B Init")
    
    def feature3(self):
        print("Feature 1-b working")
    
    def feature4(self): 
        print("Feature 4 working")
        
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("in C Init")
        
    def feat(self):
        super().feature2()
        super().feature1()


a1 = C()
a1.feat()
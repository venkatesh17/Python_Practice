class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def delete(self):
        del self.b
        del self.c
          # del self
# ============================================
# t1=Test()
# t1.delete()
# # del t1.a
# print(t1.__dict__)

# =====================================
# t1=Test()
# t2=Test()
# del t1.a
# del t2.b
# print(t1.__dict__)
# print(t2.__dict__)

# =============================================
t1=Test()
t2=Test()
t1.a = 888
t1.b=999
print(t1.a, t1.b)
print(t2.a, t2.b)

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print('Spell Check')
        print("Convention Check")
        print("Compiling 123")
        print("Running 123")

class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
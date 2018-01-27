class base():
    #def __init__(self,name):
     #   self.name=name

    def getName(self,name):
        self.name=name
        return name

    def isEmployee(self):
        return False


class inherited(base):
    def isEmployee(self):
        return True


emp1=base()

print(emp1.getName("geek"),emp1.isEmployee())

emp2=inherited()

print(emp2.getName("rohan"),emp2.isEmployee())


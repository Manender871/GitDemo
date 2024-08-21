class Calculator:
    num = 100  # variables/attributes
    # Default  Constructor

    def __init__(self, a, b):
        self.Firstnumber = a
        self.Secondnumber = b
        print("I am Default constructor and automatically called, when obj is created")

    def getdata(self):
        # Method- func if we use inside class, called Method
        print("I am now executing as method in class")

    def summation(self):
        return self.Firstnumber + self.Secondnumber + Calculator.num
    def substraction(self):
        return self.Firstnumber - self.Secondnumber

obj = Calculator(2, 3) # Syntax to create obj in Python
obj.getdata()
print(obj.summation())
print(obj.substraction())

obj1 = Calculator(4, 5) # Syntax to create obj in Python
obj1.getdata()
print(obj1.summation())

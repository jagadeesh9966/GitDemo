class Calculator:
    num = 100
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class")
    def summation(self):
        return self.firstnumber+self.secondnumber+Calculator.num
obj = Calculator(2,3)
obj.getdata()
print(obj.summation())
obj = Calculator(4,5)
obj.getdata()
print(obj.summation())

class childimpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)
    def getcompletedata(self):
        return self.num2+self.num+self.summation()
obj = childimpl()
print(obj.getcompletedata())
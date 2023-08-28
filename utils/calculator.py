class Calculator:
    def __init__(self,numA,numB):
        self.numA = numA
        self.numB = numB

    def addition(self):
        return self.numA + self.numB
    
    def subtraction(self):
        return self.numA - self.numB

    def multiplication(self):
        return self.numA*self.numB
    
    def divide(self):
        if self.numB ==0:
            return "invalid"
        else:
            return self.numA/self.numB
    
ty= Calculator(23,0)
print(ty.divide())
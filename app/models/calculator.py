class Calculator(object):
    def __init__(self, first, second): # self is the instance of the class, __init__ is the constructor
        self.first = first
        self.second = second
    
    def sum(self):
        return self.first + self.second
    
    def subtract(self):
        return self.first - self.second
    
    def multiply(self):
        return self.first * self.second
    
    def divide(self):
        return self.first / self.second




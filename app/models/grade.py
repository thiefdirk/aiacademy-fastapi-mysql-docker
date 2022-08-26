class Grade(object):
    def __init__(self, name, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math
        self.name = name
        self.avg = 0.0
        
    def set_avg(self):
        self.avg = (self.korean + self.english + self.math)/3
    
    def get_avg(self):
        return self.avg
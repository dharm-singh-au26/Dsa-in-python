"""
Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
"""

class Circle :
    def __init__(self,redius):
        self.redius = redius

    def get_Area (self):
        area = 3.14*self.redius*self.redius
        return area
    
    def get_Circumfrence(self):
        circumfrence = 2*3.14*(self.redius)
        return circumfrence
C = Circle(5)
print(C.get_Area(),C.get_Circumfrence())

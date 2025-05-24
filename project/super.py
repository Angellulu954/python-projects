class Shape:
    def __init__(self,colour,filled):
        self.colour=colour
        self.filled=filled
    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.filled else 'not filled'}")    
class Circle(Shape):
    def __init__(self,colour,filled,radius):
       super().__init__(colour,filled)
       self.radius=radius
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14*self.radius*self.radius}cm^2")   
class Square(Shape):
    def __init__(self,colour,filled,width):
        super().__init__(colour,filled)
        self.width=width
    def describe(self):
        super().describe()
        print(f"It is a Square with an area of {self.width*self.width}cm^2")       
class Triangle(Shape):
    def __init__(self,colour,filled,width,height):
        super().__init__(colour,filled)
        self.width=width
        self.height=height
    def describe(self):
        super().describe()
        print(f"It is a Triangle with an area of {self.width*self.height/2}cm^2")       
circle=Circle(colour="red",filled=True,radius=5)
square=Square(colour="blue",filled=False,width=6)
triangle=Triangle(colour="yellow",filled=True,height=8,width=7)     
print(triangle.colour)
print(triangle.filled)       
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()

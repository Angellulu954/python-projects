class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property    
    def width(self):
        return f"{self._width:.1f}cm "
    @property   
    def height(self):
        return f"{self._height:.1f}cm "    
    @width.setter
    def width(self,newwidth):
        if newwidth>0:
            self._width=newwidth
        else:
            print("Width must be greater than 0") 
    @height.setter        
    def height(self,newheight):
        if newheight>0:
            self._height=newheight
        else:
            print("Height must be greater than 0") 
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.") 
    @height.deleter      
    def height(self):
        del self._height
        print("Height has been deleted.")                       
rectangle=Rectangle(3,4)
rectangle.width=5
rectangle.height=7
del rectangle.width
del rectangle.height
print(rectangle.width)
print(rectangle.height)        
        
        
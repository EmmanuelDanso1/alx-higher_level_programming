#!/usr/bin/python3
'''Rectangle module'''
from .base import Base
class Rectangle(Base):
    '''Rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
         if not isinstance(value,int):
             raise TypeError("height must be an integer")
         if value <= 0:
             raise ValueError("height must be > 0")
         self.__height = value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(" y must be an integer")
        if value < 0:
             raise ValueError(" y must be >= 0")
        self.__y = value
    def area(self):
        '''returns area'''
        area = self.width  * self.height
        return area

    def display(self):
        '''displaying a hashtag #'''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print("" *self.x + "#" * self.width)

    def __str__(self):
        '''Rectangle update by overriding by __str__'''
        return "[Rectangle]({}){}/{} - {}/{}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)


    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i,attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break
if __name__ == "__main__":
    r1 = Rectangle(10,10,10,10)
    print(r1)
    r1.update(height=1)
    print(r1)


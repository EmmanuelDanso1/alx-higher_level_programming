#!/usr/bin/python3
from .rectangle import Rectangle
'''Rectangle module'''
class Square(Rectangle)
    '''class inheritance'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y,id)
    @property
    def size(self):
        '''getting the size'''
        return self.width
    @setter.width
    def size(self):
        '''setting the width'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Return a string representation'''
        return "[Square]({}) {}/{} - {}".format(self.id, self.x, self.y, self.width

    def update(self, *args, **kwargs):
        '''public methods that assign attribute'''
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.height = value
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

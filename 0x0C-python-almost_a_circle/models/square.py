#!/usr/bin/python3
from rectangle import Rectangle
'''Rectangle module'''
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y,id)
    
    def __str__(self):
        return "[Square]({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
if __name__ == "__main__":
    s1 = Square(5)
    print(s1)

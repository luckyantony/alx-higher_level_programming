#!/usr/bin/python3
'''
    class rectangle
'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        represent a class rectangle heritance from basegeometry
    '''
    def __init__(self, width, height):
        '''
            define width and height of rectangle class
            call the method of the superclass
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.height = height

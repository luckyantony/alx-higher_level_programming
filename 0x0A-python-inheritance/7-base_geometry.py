#!/usr/bin/python3
'''
    BaseGeometry class
'''


class BaseGeometry():
    '''
        basegeometry class
    '''
    def area(self):
        '''
            raise an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            method to validate value
            raise TypeError and Valueerror
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

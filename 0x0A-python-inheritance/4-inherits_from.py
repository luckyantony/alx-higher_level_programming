#!/usr/bin/python3
'''
    class inherits direct or indirectly from specified class
'''


def inherits_from(obj, a_class):
    '''
        check if object belongs to a class or inheritance but not a superclass
        args:
            obj: object
            a_class: class to check
        Return:
            True or False
    '''
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False

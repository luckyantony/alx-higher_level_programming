#!/usr/bin/python3
'''
    check if object is exactly an instance of a class
'''


def is_same_class(obj, a_class):
    '''
        check if object belongs to a class
        args:
            obj:object
            a_class: class to check
        Return:
            True or False
    '''
    if type(obj) is a_class:
        return True
    else:
        return False

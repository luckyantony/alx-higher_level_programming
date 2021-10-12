#!/usr/bin/python3
'''
    check if a specific object is a kind of instance or a class
'''


def is_kind_of_class(obj, a_class):
    '''
        check if object belongs a class or inheritance
        args:
            obj: object
            a_class: class to check
        Return:
            True of False
    '''
    return isinstance(obj, a_class)

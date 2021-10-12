#!/usr/bin/python3
'''
    class inheritance from list
'''


class MyList(list):
    '''
        print a list sorted
    '''
    def print_sorted(self):
        print(sorted(self))

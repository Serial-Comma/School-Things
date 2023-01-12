'''
My first module in Python.
It contains a few classic hello-world functions.
'''

def hello_once(name):
    '''Say hello once
    
    Args: 
        A string containing the name
    '''
    print('Hello again {}'.format(name))

def hello_many(items):
    '''Say hello multiple times

    Args: 
        A list of names
    '''
    for item in items:
        hello_once(item)

import sys
if __name__ == '__main__':
    print("Script name: {}".format(sys.argv[0]))
    if len(sys.argv) == 2:
        hello_once(sys.argv[1])
    if len(sys.argv) > 2:
        hello_many(sys.argv[1:])
import random

def inport_length():
    valid = False
    while valid == False:
        length = input("Enter rectangle's length: ")
        try:
            length = float(length)
            if length<0:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers: ")
        except:
            print("Something went wrong, please try again: ")
        else:
            valid = True
            return length

def inport_breadth():
    valid = False
    while valid == False:
        breadth = input("Enter rectangle's breadth: ")
        try:
            breadth = float(breadth)
            if breadth < 0:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers: ")
        except:
            print("Something went wrong, please try again: ")
        else:   
            valid = True
            return breadth
             
length = inport_length()
breadth = inport_breadth()

perimeter = length*2 + breadth*2
print("Rectangle's perimeter: {}".format(perimeter))
area = length*breadth
print("Rectangle's area: {}".format(area))
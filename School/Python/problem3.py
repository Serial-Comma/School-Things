import random

def inport_mass():
    valid = False
    while valid == False:
        mass = input("Enter your mass in Kilograms: ")
        try:
            mass = float(mass)
            if mass<0:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers: ")
        except:
            print("Something went wrong, please try again: ")
        else:
            valid = True
            return mass

def inport_height():
    valid = False
    while valid == False:
        height = input("Enter your height in metres: ")
        try:
            height = float(height)
            if height<0:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers: ")
        except:
            print("Something went wrong, please try again: ")
        else:
            valid = True
            return height

name = input("Enter your name: ")
mass = inport_mass()
height = inport_height()

bmi = mass/(height*height)

print("Hi {}, your BMI is {}.".format(name, bmi))
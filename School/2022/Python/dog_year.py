def inport_age():
    valid = False
    while valid == False:
        age = input("Enter the age in human years: ")
        try:
            age = float(age)
            if age<0:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers: ")
        except:
            print("Something went wrong, please try again: ")
        else:
            valid = True
            return age

def compute_age(age):
    age = float(age)
    if age <=2:
        dogyears = age*10.5
    else:
        dogyears = 21.0 + (age-2)*4
    return dogyears

age = inport_age()
print("Dog Years: ",compute_age(age))

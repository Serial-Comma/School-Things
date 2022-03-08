def inport_thing():
    valid = False
    while valid == False:
        thing = input("Enter your requested loan in Dollars only: ")
        try:
            thing = float(thing)
            if thing<0 or thing>100_000:
                raise ValueError

        except ValueError:
            print("Please enter only non-negative numbers that are less than 100 000: ")
        except:
            print("Something went wrong, please try again: ")
        else:
            thing = float(thing)
            valid = True
            return thing

def deposit_calculation(loan):
    if loan < 25_000:
        deposit = (5/100)*loan
    elif loan > 25_000 and loan < 50_000:
        deposit = 1250 + (10/100)*(loan-25_000)
    else:
        deposit = 5000 + (25/100)*(loan-50_000)
    return deposit

loan = inport_thing()

print("Your deposit is ${}".format(deposit_calculation(loan)))

import random
import string
import re

def generate_password():
    character_set = string.ascii_letters + string.digits
    return "".join(random.choice(character_set) for i in range(64))

x = generate_password()
print(x)


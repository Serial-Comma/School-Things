#Bilbosorter.py
#!/usr/bin/env python3
# Path: School/Python/Bilbosorter.py

import os
lst = []
with open('/home/kenspoems/Documents/School-Things/School/Python/bilbo.txt','r') as f:
    for line in f:
        lst.append(line)
    lst.sort()

with open('/home/kenspoems/Documents/School-Things/School/Python/bilbosorted.txt','w') as f:
    for line in lst:
        if line != '\n':
            f.write(line)
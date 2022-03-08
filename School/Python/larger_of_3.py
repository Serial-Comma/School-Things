file = open('abc.txt','r') #open abc.txt which should be in the same directory

a = float(file.readline().rstrip()) #read the first line and strip and float it
b = float(file.readline().rstrip()) #same thing
c = float(file.readline().rstrip())

if (a > b) == True:
    Larger = a 
else:
    Larger = b

if (Larger > c) == True:
    pass
else:
    Larger = c

print(Larger)


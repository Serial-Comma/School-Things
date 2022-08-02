def HS(studentID):
    Hash = 0
    HashTotal = 0
    for i in range(len(studentID)):
        HashTotal = HashTotal + ord(studentID[i])
    Hash = HashTotal % 500
    return Hash

def main():
    No = '0'
    studentIDList = ['G0923358Q','S9744135I','S9721536G']
    for No in range(len(studentIDList)):
        print(studentIDList[No], '->', HS(studentIDList[No]))
main()


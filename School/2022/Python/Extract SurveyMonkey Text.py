import csv

with open("/home/kenspoems/Downloads/data 2/Data_All_220823/Q10_Text.csv", 'r') as f:
    reader = csv.reader(f)

    data = []
    for row in reader:
        data.append(row)

for i in range(4,len(data)):
    if len(data[i]) == 4:

        print(data[i][2])

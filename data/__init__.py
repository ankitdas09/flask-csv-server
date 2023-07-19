import csv
import os
def getParsedData():
    print("parsing data from csv...")
    output = []
    cwd = os.getcwd()
    with open(cwd + '/data/src/letter_frequency.csv', mode='r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            temp = {}
            for i in range(3):
                if i == 0:
                    temp['letter'] = row[i].strip()
                elif i == 1:
                    temp['frequency'] = row[i].strip()
                else:
                    temp['percentage'] = row[i].strip()
            output.append(temp)            
    return output

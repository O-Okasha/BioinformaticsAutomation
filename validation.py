fileName = input("Enter File Name: ")

if len(fileName) == 0:
    print('invalid file name')

if '.fastq' not in fileName:
    print("Invalid format")

try:
    file = open(fileName, 'r')
    data = file.readlines()
    file.close()

except Exception as e:
    print(e)

readNumber = 0
startIndex = 0

for line in range(3, len(data) - 1, 4):

    read = data[startIndex: line+1]
    readNumber += 1


    if not read[0].startswith('@'):
        print('invalid ID at', readNumber)
        break

    sequence = read[1].strip()
    seqLength = len(sequence)

    for i in sequence:

        if i not in ['A', 'T', 'C', 'G', 'N']:
            print(i)
            print('Corrupted sequence at read', readNumber)
    
    delimiter = read[2].strip()

    if delimiter != '+':
        print(delimiter)
        print('Broken read at', readNumber)
        break 

    qualityLine = read[3].strip()

    if len(qualityLine) != seqLength:
        print('Quality length not equal read length at', readNumber)
    
    

    startIndex = line + 1


    




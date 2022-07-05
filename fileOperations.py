from Bio import SeqIO

class FileHandler:

    def __init__(self):
        pass

    def convertFastqToFasta(self, fileName, outfile = 'fastafile.fasta'):

        if '.fasta' not in outfile:
            outfile += '.fasta'

        converted = SeqIO.convert(fileName, "fastq", outfile, "fasta")
        print("Converted %i records" % converted)

    def validateFastq(self, data = None, fileName = None):
        
        if data == None:

            data, fileName = self.getFile()

        print('Validating', fileName + '...')

        readNumber = 0
        startIndex = 0

        for line in range(3, len(data) - 1, 4):

            read = data[startIndex: line+1]
            readNumber += 1


            if not read[0].startswith('@'):
                return False, 'invalid ID at '+ str(readNumber)
                

            sequence = read[1].strip()
            seqLength = len(sequence)

            for i in sequence:

                if i not in ['A', 'T', 'C', 'G', 'N']:
                    print(i)
                    return False, 'Corrupted sequence at read ' + str(readNumber)
            
            delimiter = read[2].strip()

            if delimiter != '+':
                print(delimiter)
                return False, 'Broken read at '+ str(readNumber)
                break 

            qualityLine = read[3].strip()

            if len(qualityLine) != seqLength:
                return False, 'Quality length not equal read length at ' + str(readNumber)
            
            startIndex = line + 1
        return True, ''
        print('File', fileName, 'is valid.')


    def getFile(self, want='f'):

        fileName = input("Enter File Name: ")
        if want == 'n':
            return fileName

        if len(fileName) == 0:
            raise Exception('invalid file name')

        if '.fastq' not in fileName:
            raise Exception("Invalid format")

        try:
            file = open(fileName, 'r')
            data = file.readlines()
            file.close()
            return data, fileName

        except Exception as e:
            raise Exception(e)
    
        
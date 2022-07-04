from fileOperations import FileHandler
from seqOperations import SequenceHandler


fileOp = FileHandler()
seqOp = SequenceHandler()


while True:

    inp = input('1 - Fetch \n2 - Fastq to Fasta \n3 - Validate fastq \n4 - Exit \n>> ')

    if inp == '1':
        print(seqOp.fetch())
    elif inp == '2':
        fileOp.convertFastqToFasta()
    elif inp == '3':
        fileOp.validateFastq()
    elif inp == '4':
        exit(0)




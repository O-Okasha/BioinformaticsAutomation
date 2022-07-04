from fileinput import filename
from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd
from fileOperations import FileHandler


class StatisticsOperations:

    def __init__(self) -> None:
        self.fileName = None
        self.file = None
        self.SeqFile = None

    def getInput(self, fileName: str):

        if '.fastq' in fileName:
            with open(fileName) as f:
                FileHandler.convertFastqToFasta(f, fileName)
        self.SeqFile = SeqIO.parse('fastafile.fasta', 'fasta')
        

    def getCGContent(self):
        sequences = self.SeqFile
        output = []
        for seq in sequences:
            seq_id = seq.id
            sequence = seq.seq
            gc_content = GC(sequence)
            gc_content = round(gc_content, 2)
            output.append([seq_id, gc_content])
        return output

    def countNeo(self):

        file = self.SeqFile
        output = []
        for cur_record in file :

            gene_name = cur_record.name
            A_count = cur_record.seq.count('A')
            C_count = cur_record.seq.count('C')
            G_count = cur_record.seq.count('G')
            T_count = cur_record.seq.count('T')

            output.append([gene_name, A_count, C_count, G_count, T_count])
        return output
    
    
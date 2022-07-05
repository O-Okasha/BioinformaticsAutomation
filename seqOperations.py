import os
import string
from Bio import Entrez, SeqIO
from Bio.SeqUtils import GC
from fileOperations import FileHandler
from Bio import pairwise2
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment 
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align.Applications import ClustalwCommandline

class SequenceHandler:

    def fetch(self, ids):
        try:
            Entrez.email = 'bioinfocoach@bioinfo.com'
            handle = Entrez.efetch(db = "nucleotide", id=ids, rettype='fasta')
            ls = handle.readlines()
            fasta = ''
            for line in ls:
                fasta += line
            return fasta
        except Exception as e:
            return e


    def getIDs(self) -> list[str]:
        ids = []

        while True:
            id = input('Enter accession number or enter e to stop')
            if id.lower() == 'e':
                break
            else:
                if self.validateID(id):
                    ids.append(id)
        return ids

    
    def validateID(self, id: str) -> bool:
        chars = list(string.ascii_letters)
        digits = list(string.digits)

        acc = ''

        if '.' in id:
            acc = id.split('.')[0]

            for i in id.split('.')[1]:
                if i not in digits:
                    return False

        else:
            acc = id
        charCounter = 0

        if len(acc) == 6:
            for i in acc:
                if i in chars:
                    charCounter += 1
                if charCounter > 1:
                    return False

        elif len(acc) == 8:
            for i in acc:
                if i in chars:
                    charCounter += 1
                if charCounter > 2:
                    return False
        return True
    def pairwise(self, method, filename1 = None, filename2 = None, seq1 = None, seq2 = None):

        try:
            if seq1 == None:
                seq = SeqIO.parse(filename1, 'fasta')
                for i in seq:
                    seq1 = i
                    break
                for i in seq:
                    seq2 = i
            if method == 'local':
                alignments = pairwise2.align.localxx(seq1, seq2) 
                output = []
                for alignment in alignments:
                    output.append(format_alignment(*alignment))
            elif method == 'global':
                alignments = pairwise2.align.globalxx(seq1, seq2) 
                output = []
                for alignment in alignments:
                    output.append(format_alignment(*alignment))
            else:
                raise Exception('Unknown method')
            return output
        except Exception as e:
            return e

    def multipleAllignment(self, file):
        
        clustalw_exe = r"C:\Program Files (x86)\ClustalX2\clustalx.exe"
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile = file)
        assert os.path.isfile(clustalw_exe), "Clustal_W executable is missing or not found"
        stdout, stderr = clustalw_cline()
        print(clustalw_cline)

    def tree(self, file):
        align = AlignIO.read(file,"clustal")
        calculator = DistanceCalculator('identity')
        distMatrix = calculator.get_distance(align)
        constructor = DistanceTreeConstructor()
        UPGMATree = constructor.upgma(distMatrix)
        Phylo.draw(UPGMATree)
import string
from Bio import Entrez, SeqIO

class SequenceHandler:

    def fetch(self):
        ids = self.getIDs()
        Entrez.email = 'bioinfocoach@bioinfo.com'
        handle = Entrez.efetch(db = "nucleotide", id=ids, rettype='fasta')
        ls = handle.readlines()
        fasta = ''
        for line in ls:
            fasta += line
        return fasta


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


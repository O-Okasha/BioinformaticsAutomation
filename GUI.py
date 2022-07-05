from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from seqOperations import SequenceHandler
from statisticsOperations import StatisticsOperations
from fileOperations import  FileHandler
from Bio import SeqIO

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('yarab.ui', self)
        self.show()
        self.seq = None
        self.fq = None
        self.fn = None
        self.cf = None
        self.filesHandler = FileHandler()
        self.seqHandler = SequenceHandler()
        self.stat = StatisticsOperations()
        self.pushButton.clicked.connect(self.OpenFile)
        self.pushButton_3.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.fetch)
        self.pushButton_9.clicked.connect(self.doStats)
        self.pushButton_18.clicked.connect(self.pairwiselocal)
        self.pushButton_16.clicked.connect(self.pairwiseglobal)
        self.pushButton_15.clicked.connect(self.MSA)
        self.pushButton_17.clicked.connect(self.tree)
    def OpenFile(self):
        filename = self.lineEdit.text()
        print(filename)
        if '.fastq' in filename:
            with open(filename) as f:
                data = f.readlines()
            b, ret = self.filesHandler.validateFastq(data, filename)
            
            if not b:
                self.output(ret)
            else:
                self.output(filename + ' FastQ file is loaded')
                self.fq = data
                self.fn = filename
        elif '.fasta' in filename:
            with open(filename) as f:
                data = f.readlines()
            self.seq = SeqIO.parse(filename, 'fasta')
            self.fq = data
            self.fn = filename
            self.output(filename + ' Fasta file is loaded')
        
    def output(self, text):
        self.textEdit.setText(text)
    
    def convert(self):
        if self.fn == None:
            self.output('No file is loaded.')
            return
        else:
            outfile = self.lineEdit_3.text()
            self.filesHandler.convertFastqToFasta(self.fn, outfile=outfile)
            self.output(f'Successfully converted {self.fn} to {outfile}.')
            self.cn = outfile
    def fetch(self):
        try:
            ids = self.lineEdit_2.text()
            ids = ids.split(',')
            if len(ids) == 1:
                out = self.seqHandler.fetch(ids[0])
            else:
                for i in range(len(ids)):
                    ids[i] = ids[i].strip()
                out = self.seqHandler.fetch(ids)
            with open('fetch.fasta', 'w') as f:
                f.write(out)
            self.output('Sequrnces saved to fetch.fasta')
            self.output(out)
        except Exception as e:
            self.output(e)
    def doStats(self):
        if self.radioButton.isChecked():
            if self.fn == None:
                self.output('Must open file first.')
            elif '.fastq' in self.fn:
                if self.cf == None:
                    self.filesHandler.convertFastqToFasta(self.fn)
                    self.stat.getInput('fastafile.fasta')
                    cg = self.stat.getCGContent()
                    cnt = self.stat.countNeo()
                else:
                    self.stat.getInput(self.cf)
                    cg = self.stat.getCGContent()
                    cnt = self.stat.countNeo()
                    with open(self.cf, 'r') as file:
                        data = file.read()
                        occurrencesofA = data.count("A")
                        occurrenceofT = data.count("T")
                        occurrencesofG = data.count("G")
                        occurrencesofC = data.count("C")
                        print('Number of occurrences of A :', occurrencesofA)
                        print('Number of occurrences of T :', occurrenceofT)
                        print('Number of occurrences of G :', occurrencesofG)
                        print('Number of occurrences of C:', occurrencesofC)
                        cnt = [occurrencesofA, occurrencesofC, occurrencesofG, occurrenceofT]
                    out = 'GC Content:\n'
                    for i in cg:
                        out += i[0] + '\t' + str(i[1]) + '\n'
                        out += '\n'
                        out += "Counts:\n \tA\tC\tG\tT \n"
                    print(cnt)
                    out += '\t' + str(cnt[0]) + '\t' + str(cnt[1]) + '\t' + str(cnt[2]) + '\t' + str(cnt[3])
                    self.output(out)
            else:
                self.stat.getInput(self.fn)
                cg = self.stat.getCGContent()
                cnt = self.stat.countNeo()
                with open(self.fn, 'r') as file:
                    data = file.read()
                    occurrencesofA = data.count("A")
                    occurrenceofT = data.count("T")
                    occurrencesofG = data.count("G")
                    occurrencesofC = data.count("C")
                    print('Number of occurrences of A :', occurrencesofA)
                    print('Number of occurrences of T :', occurrenceofT)
                    print('Number of occurrences of G :', occurrencesofG)
                    print('Number of occurrences of C:', occurrencesofC)
                    cnt = [occurrencesofA, occurrencesofC, occurrencesofG, occurrenceofT]
                out = 'GC Content:\n'
                for i in cg:
                    out += i[0] + '\t' + '\t' + str(i[1]) + '\n'
                    out += '\n'
                out += "Counts:\n \tA\tC\tG\tT \n"
                print(cnt)
                out += '\t' + str(cnt[0]) + '\t' + str(cnt[1]) + '\t' + str(cnt[2]) + '\t' + str(cnt[3])
                self.output(out)
        elif self.radioButton_2.isChecked():
            try:
                self.stat.getInput('fetch.fasta')
                cg = self.stat.getCGContent()
                with open('fetch.fasta', 'r') as file:
                    data = file.read()
                    occurrencesofA = data.count("A")
                    occurrenceofT = data.count("T")
                    occurrencesofG = data.count("G")
                    occurrencesofC = data.count("C")
                    print('Number of occurrences of A :', occurrencesofA)
                    print('Number of occurrences of T :', occurrenceofT)
                    print('Number of occurrences of G :', occurrencesofG)
                    print('Number of occurrences of C:', occurrencesofC)
                    cnt = [occurrencesofA, occurrencesofC, occurrencesofG, occurrenceofT]
                out = 'GC Content:\n'
                for i in cg:
                    out += i[0] + '\t' + str(i[1]) + '\n'
                    out += '\n'
                out += "Counts:\n \tA\tC\tG\tT \n"
                print(cnt)
                out += '\t' + str(cnt[0]) + '\t' + str(cnt[1]) + '\t' + str(cnt[2]) + '\t' + str(cnt[3])
                self.output(out)
            except Exception as e:
                self.output(e)
    def pairwiselocal(self):
        out = self.seqHandler.pairwise('local', filename1='fetch.fasta')
        self.output(out[0])
        with open('allign.aln', 'w') as f:
            f.write(out)
    def pairwiseglobal(self):
        out = self.seqHandler.pairwise('global', filename1='fetch.fasta')
        self.output(out[0])
        with open('allign.aln', 'w') as f:
            f.write(out)
    def MSA(self):
        if self.radioButton_2.isChecked():
            self.seqHandler.multipleAllignment('fetch.fasta')
        else:
            fname = self.lineEdit_10.text()
            if '.fastq' in fname:
                self.filesHandler.convertFastqToFasta(fname)
                self.seqHandler.multipleAllignment('fastafile.fasta')
            else:
                self.seqHandler.multipleAllignment(fname)
    def tree(self):
        self.seqHandler.tree('output.aln')


        




def main():
    app = QApplication([])
    window = GUI()
    app.exec_()



if __name__ == '__main__':
    main()
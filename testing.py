from Bio import SeqIO

converted = SeqIO.convert("test.fastq", "fastq", "fasta-convert.fasta", "fasta")
print(converted)

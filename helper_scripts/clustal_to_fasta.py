#!/usr/bin/env python3
import sys
from Bio import SeqIO

records = SeqIO.parse(sys.argv[1], "clustal")
count = SeqIO.write(records, str(sys.argv[1]) + ".fa", "fasta")
print("Converted %i records" % count)
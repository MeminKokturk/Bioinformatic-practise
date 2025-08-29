import sys

from DNAtoolkit import *

#This program is going to find the EcoRI cutting site and return the cut DNA after the cutting event occured



dna_seq = input("Enter the sequence that is going to be cut by EcoRI: ")

EcoRI_cut_site = "GAATTC"

dna_seq = dna_seq.upper()


if validateSeq(dna_seq) == False:
    print("This is not a DNA sequence!!!")
    sys.exit()


find_count = 0
find_count = dna_seq.count(EcoRI_cut_site)

if find_count == 0:
     print("There is no complementary site for EcoRI")
if find_count == 1:
    position = int(dna_seq.find(EcoRI_cut_site))
    length = int(len(dna_seq))
    print(dna_seq[position + 1:length])
else:
    position = int(dna_seq.find(EcoRI_cut_site))
    length = int(len(dna_seq))
    dna_seq = dna_seq[position + 1:length]
    position2 = int(dna_seq.find(EcoRI_cut_site))
    print(dna_seq[0:position2+1])


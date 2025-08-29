from DNAtoolkit import *
import random


rndDNAstr = ''.join((random.choice(Nucleotides))
                for nuc in range(20))

print(type(rndDNAstr))

print(validateSeq(rndDNAstr))

print(countNucFreq(rndDNAstr))
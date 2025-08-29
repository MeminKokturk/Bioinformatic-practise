# DNA toolkit file

Nucleotides = ["A", "C", "G", "T"]

# We need to validate it is a DNA string


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFreq(seq):
    tmpFreqDic = {"A": 0, "T": 0, "C": 0, "G": 0}
    for nuc in seq:
        tmpFreqDic[nuc] += 1
    return tmpFreqDic
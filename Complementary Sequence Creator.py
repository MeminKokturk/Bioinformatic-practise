Seq=input("Please input the sequence that you want the complementary of: ")

Nucleotides = ["A", "T", "C", "G"]
comp_seq=""
upcase=""

for i in Seq:
    upcase = i
    upcase = str.upper(upcase)
    if upcase == "A":
        comp_seq = comp_seq+"T"
    if upcase == "T":
        comp_seq = comp_seq + "A"
    if upcase == "C":
        comp_seq = comp_seq + "G"
    if upcase == "G":
        comp_seq = comp_seq + "C"
    if upcase not in Nucleotides:
        print("non-nuclotide letter detected, mission aborted")
        break
print(comp_seq)

def length_dna(dna):
    return len(dna)
sequence = "ATGCGTAA"
length = length_dna(sequence)
print("The length of Dna:", length)
# count dna 
def count_dna(dna):
    count = dna.count("A")
    return count
seq = "ATGCAAAT"
print(count_dna(seq))
# GC content 
def gc_content(dna):
    sequence = dna.upper().replace("N", " ")
    if len(sequence) == 0:
        return None
    gc = (sequence.count("G") + sequence.count("C"))/len(sequence) *100
    return gc
genes = "ATGCGCGAT"
print("The gc content of the sequence are:", gc_content(genes))
# diluation equation
def dilution(c2, v2, c1):
   v1 = c2*v2/c1 
   return v1 
print(dilution(10,50,100))
# gc rich 
def gc_rich(seq):
    sequence = seq.upper().replace("N", " ")
    gc = (sequence.count("G") + sequence.count("C"))/len(sequence) *100 
    if gc > 50 :
        return gc, "GC content is rich"  
    else:
        return gc, "GC content is low"
gene = "GGGGCCCCATCG"
gc, message = gc_rich(gene)
print("GC content:", gc)
print(message)
# dna validation 
def dna_validation(seq):
    for base in seq:
        if base not in "ATGCN":
            return "Invalid dna"
    return "valid DNA" 
sample1 = "ATGCATGC"
sample2 = "ATGBXYZ"
print(dna_validation(sample1))
print(dna_validation(sample2))
# functions and loops 
def gc_content(seq)
    dna = seq.upper().replace("N","")
    if len(dna) == 0:
        return None 
    gc = (dna.count("G") + dna.count("C"))/len(dna) * 100
sequences = [
    "ATGC",
    "GGGG",
    "ATAT",
    "CCCGGG"
]
for sequence in sequences:
    if sequence >
                                    








# DNA Base Counter
dna = "ATGCGATCGAATTC"
counts = {}
for base in dna:
    if base in counts:
        counts[base] += 1
    else:
        counts[base] = 1
print(counts)
# Gene Filter
gene_expression = {
    "TP53": 250,
    "BRCA1": 80,
    "EGFR": 320,
    "MYC": 150,
    "KRAS": 90
}
for gene, value in gene_expression.items():
    if value > 200:
        print("The highest expression gene:", gene)
        print("The Highest expressed gene value:", value)
#Most Frequent Codon
codons = [
    "ATG",
    "AAA",
    "ATG",
    "TTT",
    "ATG",
    "AAA",
    "GGG"
]
counts = {}
for codon in codons:
    if codon in counts:
        counts[codon] += 1
    else:
        counts[codon] = 1
print(counts)
most_frequent_codon = ""
counts_of_codon = 0
for codon, count in counts.items():
    if count > counts_of_codon:
        counts_of_codon = count
        most_frequent_codon = codon
print("The most_frequent_codon:", most_frequent_codon)
print("The count of most frequent codon:", counts_of_codon)
#Motif Finder
dna = "ATGCGATGCGATGCG"
motif = "GCG"
for i in range(len(dna)):
    base = dna[i:i+3]
    if base == motif in dna:
        print("The position of motif found in dna:", i)
# Restriction Enzyme Report
dna = "AAGCTTCGAATTCAGCTTCGA"
enzymes = {
    "EcoRI": "GAATTC",
    "AluI": "AGCT",
    "TaqI": "TCGA",
    "NotI": "GCGGCCGC"
}
for enzyme, sequence in enzymes.items():
    if sequence in dna:
        position  = dna.find(sequence)
        print(enzyme, sequence, position)
    else:
        print("The enzyme not found in dna:", enzyme)
# longest sequence and shortest sequence 
sequences = [
    "ATGC",
    "ATGCGA",
    "AT",
    "ATGCGAT",
    "ATGCG",
    "AT"
]
# longest sequence
longest_sequence = ""
longest_length = 0
# shortest sequence 
shortest_sequence = sequences[0]
shortest_length = len(sequences[0])
for seq in sequences:
    if len(seq) > longest_length:
        longest_sequence = seq
        longest_length = len(seq)
    elif len(seq) < shortest_length:
        shortest_length = len(seq)
        shortest_sequence = seq
print("The longest_sequence:", longest_sequence)
print("The shortest_sequence:", shortest_sequence)
print("The longest_length of the sequence:", longest_length)
print("The shortest_length of the sequence:", shortest_length)
# fasta score 
fastq_scores = [35, 20, 30, 40, 18, 38, 25, 31]
counts = {"High": 0,
          "Medium": 0,
          "low": 0}
for value in fastq_scores:
    if value > 30:
       counts["High"] += 1
    elif 20<= value <=30:
        counts["Medium"] += 1
    else:
        counts["low"] += 1
print(counts)
# last 
dna = "ATGAAATTTGGGCCCATGAAA"
counts = {}
for i in range(0,len(dna),3):
    base = dna[i:i+3]
    if base in counts:
        counts[base] += 1
    else: 
        counts[base] =1
print(counts)

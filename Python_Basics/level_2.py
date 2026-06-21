# gene sum
genes = ["TP53", "BRCA1", "EGFR", "TP53", "EGFR"]
counts = {}
for codon in genes:
  if codon in counts:
   counts[codon] += 1
  else:
   counts[codon] = 1
print(counts)
#Count the frequency of every character WITHOUT pre-defining the dictionary.
dna = "ATGCGATTA"
counts={}
for base in dna:
 if base in counts:
  counts[base] += 1
 else:
  counts[base] = 1
print(counts)
#Print only genes whose expression is greater than 100.
gene_expression = {
    "TP53": 50,
    "BRCA1": 120,
    "EGFR": 80,
    "MYC": 200
}
for gene, value in gene_expression.items():
 if value > 100:
  print(gene, value)
  # GC content
dna = "ATGCGATTACG"
A = 0
T = 0
C = 0
G = 0
for i in dna:
  if i == "A":
    A += 1
  elif i == "T":
    T += 1
  elif i == "C":
    C += 1
  elif i == "G":
    G += 1
print("The no_of_Base A:", A)
print("The no_of_Base T:", T)
print("The no_of_Base C:", C)
print("The no_of_Base G:", G)
# perncetage of GC content 
sum = G + C
GC_content = (sum/len(dna))*100
print("The percentage of GC_content:", GC_content)
# Create a codon counter
dna = "ATGAAATTTGGGCCC"
counts = {}
for i in range(0,len(dna),3):
 codon = dna[i:i+3]
 if i in counts:
  counts[codon] += 1
 else:
  counts[codon] = 1
print(counts)
# smaple with highest expression
samples = {
    "Sample1": 100,
    "Sample2": 250,
    "Sample3": 80,
    "Sample4": 300
}
highest_expression = 0
highest_sample = ""
for sample, value in samples.items():
 if value > highest_expression:
  highest_expression = value
  highest_sample = sample
print ("the highest expression of the gene:", highest_expression)
print("the highest sample of the gene:", highest_sample)
# fastq
fastq_quality = [30, 35, 28, 40, 20, 38]
counts = {
 "Good":0,
 "Poor":0
}
for value in fastq_quality:
 if value > 30:
  counts["Good"] += 1
 elif value <= 30:
  counts["Poor"] += 1
print(counts)
#most frequent nucleotide
dna = "ATGCGATTACGATGCGA"
counts = {}
for base in dna:
 if base in counts:
  counts[base] += 1
 else:
  counts[base] = 1
highest_count = 0
frequent_nucleotide = ""
for base, count in counts.items():
 if count > highest_count:
  highest_count = count
  frequent_nucleotide = base
print("The highest count nucleotide in dna:",highest_count)
print("The frequent_nucleotide in dna:", frequent_nucleotide)
# mini project 
sequences = [
    "ATGC",
    "ATGCGA",
    "AT",
    "ATGCGAT",
    "ATG"
]
length = {}
for seq in sequences:
 length[seq] = len(seq)
print(length)
    
 


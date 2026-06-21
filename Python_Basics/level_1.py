# count the bases
dna = "ATGCGATTA"
A = 0
T = 0
C = 0
G = 0
for bases in dna:
  if bases == "A":
    A += 1
  elif bases == "T":
    T += 1
  elif bases == "C":
    C += 1
  elif bases =="G":
    G += 1  
print("The no_of_ base A:", A)
print("The no_of_ base T:", T)
print("The no_of_ base C:", C)
print("The no_of_ base G:", G)
# dictionaries count 
genes = ["TP53", "BRCA1", "EGFR", "TP53", "EGFR"]
counts = {}
for gene in genes :
  if gene in counts:
    counts[gene] += 1
  else:
    counts[gene] = 1
print(counts)
# dictionaries for amino acids 
protein = "MKTLLVAAAGG"
counts = {}
for amino_acid in protein:
  if amino_acid in counts:
    counts[amino_acid] += 1
  else:
    counts[amino_acid] = 1
print(counts)
# gene Expression
expression = [120,80,250,90,300,150,40]
counts = {
  "High": 0,
  "Low": 0
}
for value in expression:
  if value >= 100:
    counts["High"] += 1
  elif value <= 100:
    counts["Low"] += 1
print(counts)
# codon counter 
dna = "ATGAAATTTGGGATGAAA"
counts = {}
for i in range(0,len(dna),3):
  codon = dna[i:i+3]
  if codon in counts:
    counts[codon] += 1
  else:
    counts[codon] = 1
print(counts)
# each mutation occur 
mutations = [
    "A>T",
    "G>C",
    "A>T",
    "T>G",
    "G>C",
    "A>T"
]
counts = {}
for i in mutations:
  if i in counts:
    counts[i] += 1
  else:
    counts[i] = 1
print(counts)
# challenge question
genes = [
    "TP53",
    "BRCA1",
    "EGFR",
    "TP53",
    "MYC",
    "BRCA1",
    "TP53"
]
counts = {}
for gene in genes:
  if gene in counts:
    counts[gene] += 1
  else:
    counts[gene] = 1
print(counts)
# FASTQ Quality 
qualities = [35, 20, 40, 15, 32, 28, 38]
counts = {
  "Good":0,
  "Bad":0
}
for value in qualities:
  if value >=30:
    counts["Good"] += 1
  elif value < 30:
    counts["Bad"] += 1
print(counts)
# most frequent nucleotide
dna = "ATGCGATTACGATGCGA"
counts = {}
for base in dna:
  if base in counts:
    counts[base] +=1
  else:
    counts[base] = 1
print(counts)
highest_count = 0
most_frequent_base = ""
for base, count in counts.items():
  if count > highest_count:
    highest_count = count
    most_frequent_base = base
print("Most frequent base:", most_frequent_base)
print("Count:", highest_count) 
#gene expression
gene_expression = { "TP53": 120, "BRCA1": 80, "EGFR": 250, "MYC": 90 }
for gene, value in gene_expression.items():
  if value > 100:
    print(gene, value)

  
          
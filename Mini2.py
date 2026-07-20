print("---------------------------------------------------------------------------------------------")
print("DNA-Mutation-Analysis".center(84))
print("---------------------------------------------------------------------------------------------")
##Gene:- BRCA1, Organism:- Homo Sapiens, GeneID=672, chromosome=17
                                                    
b=""

a= open("Data/gene.fna.txt","r")
text = a.read()
for ch in text:
    if ch in ("A","T","G","C"):
        b = b + ch 
print("Length of the DNA sequence is:",len(b))
   
import Protein_Dictionary as pd
count_A=count_T=count_G=count_C = 0
for nucleotide in b:
            if(nucleotide == 'A' ):
             count_A = count_A+1
            elif(nucleotide== 'T' ): 
             count_T = count_T+1
            elif(nucleotide == 'G' ): 
                count_G = count_G+1
            else: 
                count_C = count_C+1            
GC_content = ((count_G + count_C)/(count_C + count_G+ count_A+count_T))  * 100
AT_content = ((count_A + count_T)/(count_C + count_G+ count_A+count_T))  * 100

print("Total AT content is: ",AT_content,"%")
print("Total GC content is: ",GC_content,"%")


protein =[]

print("---------------------------------------------------------------------------------------------")

for i in range(0,len(b)-2,3):       
        amino_acid=pd.dic[b[i:i+3]]
        protein.append(amino_acid)
print("Protein Synthesized")
print("The length of protein is: ",len(protein))         ##Length of the Translated Protein 

import random
bases = ['A', 'T', 'G', 'C']
num_mutations = 250
for i in range(num_mutations):
        pos = random.randint(0, len(b) - 1)
        current_base = b[pos]
        possible_bases = bases.copy()
        possible_bases.remove(current_base)
        new_base = random.choice(possible_bases)
        b = b[:pos] + new_base + b[pos + 1:]
print("---------------------------------------------------------------------------------------------")

print("After random point mutations:")
print("Length of mutated DNA is: ",len(b))
new_protein = []
for i in range(0,len(b)-3,3):
        amino_acid=pd.dic[b[i:i+3]]
        new_protein.append(amino_acid)
print("Mutated protein synthesized")
print("Length of mutated protein is:",len(new_protein))          

common_AA = 0

for i in range(0, min(len(protein), len(new_protein))):
        if protein[i] == new_protein[i]:
            common_AA += 1
per_cent = (common_AA/len(protein))*100 
print("---------------------------------------------------------------------------------------------")
print("Total number of common amino acids:",common_AA)
print("Percentage of Common Amino Acids is:",per_cent)
print("---------------------------------------------------------------------------------------------")

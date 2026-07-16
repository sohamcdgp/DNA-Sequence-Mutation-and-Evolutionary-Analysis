print("DNA-Sequence-Mutation-and-Evolutionary-Analysis")
##Gene:- BRCA1, Organism:- Homo Sapiens, GeneID=672, chromosome=17
a= open("Data/gene.fna.txt","r")
b=""
def read_dna():  
    '''
    Opens the FASTA file in reading mode,
    converts it into a string and returns it.
    '''

    text = a.read()
    global b
    for ch in text:
        if ch in ("A","T","G","C"):
            b = b + ch 
    return(b)   
    return len(b)     ###Length of Original DNA

read_dna()
import Protein_Dictionary as pd
def cGC():
    '''
    Calculates the DNA GC content of your file 
    Loops through each individual nucleotide in the file, and for each nucleotide it adds it's pre-existing count by one. 
    Finally, it calculates the percentage of GC in the DNA, 
    then the length of the entire DNA.
    '''
    
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
    return count_A+count_T+count_G+count_C, GC_content


protein =[]
def translate_dna(b):
    '''
    Translates the DNA into protein
    then returns it.
    '''

    for i in range(0,len(b)-2,3):       
        amino_acid=pd.dic[b[i:i+3]]
        protein.append(amino_acid)
    print("Protein Synthesized")
    
    return protein
    return len(protein)         ##Length of the Translated Protein 
translate_dna(b)
def mutate_dna():
    '''
    induces point mutations at random positions at the DNA strings
    returns new string.
    '''
    global b
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
    print("After random point mutations:")
    print("Mutated DNA:")

    return b
    return len(b)        ###Length of mutated DNA
mutate_dna()
new_protein = []
def mutated_protein():
    '''
    Translates the mutated DNA into protein 
    and then returns it.
    '''
    for i in range(0,len(b)-3,3):
        amino_acid=pd.dic[b[i:i+3]]
        new_protein.append(amino_acid)
    print("Mutated protein synthesized")
    return new_protein
    return len(new_protein)          ###Length of mutated protein
mutated_protein()

def Compare():
    '''Compares the amino acid sequences across the two proteins
    and then returns the total number of common amino acids and percentage similarity between the two sequences
    '''
    common_AA = 0

    for i in range(0, min(len(protein), len(new_protein))):
        if protein[i] == new_protein[i]:
            common_AA += 1
    per_cent = (common_AA/len(protein))*100 
    return common_AA,per_cent
Compare()

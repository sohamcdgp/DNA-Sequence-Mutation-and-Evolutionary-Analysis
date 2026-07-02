import dic
print("Evolutionary Sequence Simulation and Comparative Analysis System")
###Gene name
b=""
def read_dna():
    
   
    a = open("gene.fna.txt",'r')
    text = a.read()

    global b
    for ch in text:
        if ch in ("A","T","G","C"):
            b = b + ch 
    return(b)   

read_dna()
dic = {
    "TTT" : "Phe",
    "TTC" : "Phe",
    "TTA" : "Phe",
    "TTG" : "Phe",
    "CTT" : "Leu",
    "CTC" : "Leu",
    "CTA" : "Leu",
    "CTG" : "Leu",
    "ATT" : "Ile",
    "ATC" : "Ile",
    "ATA" : "Ile",
    "ATG" : "Met",
    "GTT" : "Val",
    "GTC" : "Val",
    "GTA" : "Val",
    "GTG" : "Val",
    "TCT":"Ser",
    "TCC":"Ser",
    "TCA":"Ser",
    "TCG":"Ser",
    "CCT":"Pro",
    "CCC":"Pro",
    "CCA":"Pro",
    "CCG":"Pro",
    "ACT":"Thr",
    "ACC":"Thr",
    "ACA":"Thr",
    "ACG":"Thr",
    "GCT":"Ala",
    "GCC":"Ala",
    "GCA":"Ala",
    "GCG":"Ala",
    "TAT":"Tyr",
    "TAC":"Tyr",
    "TAA":"Stop",
    "TAG":"Stop",
    "CAT":"His",
    "CAC":"His",
    "CAA":"Gln",
    "CAG":"Gln",
    "AAT":"Asn",
    "AAC":"Asn",
    "AAA":"Lys",
    "AAG":"Lys",
    "GAT":"Asp",
    "GAC":"Asp",
    "GAA":"Glu",
    "GAG":"Glu",
    "TGT":"Cys",
    "TGC":"Cys",
    "TGA":"Stop",
    "TGG":"Trp",
    "CGT":"Arg",
    "CGC":"Arg",
    "CGA":"Arg",
    "CGG":"Arg",
    "AGT":"Ser",
    "AGC":"Ser",
    "AGA":"Arg",
    "AGG":"Arg",
    "GGT":"Gly",
    "GGC":"Gly",
    "GGA":"Gly",
    "GGG":"Gly"
}
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
    for i in range(0,len(b)-2,3):       
        amino_acid=dic[b[i:i+3]]
        protein.append(amino_acid)
    print("Protein Synthesized")
    
    command =input("Type yes to see the protein sequence: ")
    if(command=="yes"):
        return protein
    
translate_dna(b)
def mutate_dna():
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
    command =input("Type yes to see the mutated DNA sequence: ")
    if(command=="yes"):
        return b
mutate_dna()
new_protein = []
def mutated_protein():
    for i in range(0,len(b)-3,3):
        amino_acid=dic[b[i:i+3]]
        new_protein.append(amino_acid)
    print("Mutated protein synthesized")
    command =input("Type yes to see the mutated protein sequence: ")
    if(command=="yes"):
       return new_protein
mutated_protein()


def Compare():
    common_AA = 0

    for i in range(0, min(len(protein), len(new_protein))):
        if protein[i] == new_protein[i]:
            common_AA += 1
    per_cent = (common_AA/len(protein))*100 
    return common_AA,per_cent
Compare()
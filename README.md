# DNA-Mutation-Analysis-Toolkit

A python-based bioinformatics toolkit for analyzing DNA sequences, calculating GC content, translating DNA to protein, inducing random point mutations, and comparing protein sequences to study evolutionary changes.

## Overview
 
This project provides a simple yet comprehensive platform to perform fundamental DNA sequence analysis and evolutionary simulation. It accepts DNA sequences and performs four core analyses in a clean, intuitive interface.

## Features
 
### 1. GC Content Analysis
- Calculates the percentage of guanine (G) and cytosine (C) nucleotides in the DNA sequence
- **Formula:** (G count + C count) / Total length × 100
  
### 2. AT Content Analysis
- Calculates the percentage of adenine (A) and thymine (T) nucleotides in the DNA sequence
- **Formula:** (A count + T count) / Total length × 100

### 3. DNA to Protein Translation
- Translates DNA sequences into protein sequences using the complete genetic code
- Maps all codons to their corresponding amino acids
- Processes the sequence in triplet codons (5' → 3')
- Returns protein length

 ### 4. Point Mutation Generation
- Induces point mutations at random sites in DNA.
- Total number of mutations: 250

### 5. Protein Sequence Comparison
- Compares original and mutated protein sequences
- Counts matching amino acids at corresponding positions
- Calculates similarity percentage
- Displays comparison metrics:
  - Number of matching amino acids
  - Similarity percentage



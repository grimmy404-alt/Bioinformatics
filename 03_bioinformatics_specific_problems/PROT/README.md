# Translating RNA into Protein

**Problem ID:** PROT  
**Rosalind Link:** [PROT](https://rosalind.info/problems/prot/)

---

## Problem Description

Translate an RNA string into a protein string using the genetic code.

### Input Format
An RNA string s of length at most 10 kbp in FASTA format.

### Output Format
The protein string encoded by s.

---

## Biological Context

Translation is the second step of gene expression. The genetic code maps RNA codons to amino acids. Used in gene annotation, ORF prediction, and proteomics.

---

## Sample Dataset

**Input:**
```
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
```

**Output:**
```
MAMAPRTEINSTRING
```

---

## Solution Approach

This solution:
1. Reads the input data from a file
2. Processes the data according to the problem requirements
3. Outputs the result in the specified format

### Key Concepts Used
- String manipulation
- File I/O
- FASTA parsing

---

## Usage

```bash
python solution.py
```

When prompted, enter the path to your input file (e.g., `sample_input.txt`).

---

## Files in This Directory

- `README.md` - This file
- `solution.py` - Python solution
- `sample_input.txt` - Sample input data from Rosalind
- `sample_output.txt` - Expected output

---

**Author:** Nilesh Ghosh

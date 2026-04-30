# Computing GC Content

**Problem ID:** GC  
**Rosalind Link:** [GC](https://rosalind.info/problems/gc/)

---

## Problem Description

Calculate the GC content of DNA sequences in FASTA format and identify the sequence with highest GC content.

### Input Format
At most 10 DNA strings in FASTA format (each of length at most 1 kbp).

### Output Format
The ID of the sequence with highest GC content, followed by the GC content (as a percentage with 6 decimal places).

---

## Biological Context

GC content varies across genomes and influences DNA stability, gene density, and recombination rates. High GC content is common in thermophilic organisms. Used in quality control of sequencing data.

---

## Sample Dataset

**Input:**
```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

**Output:**
```
Rosalind_0808
60.919540
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

**Author:** Nilesh  
**Date Solved:** 2024

# Counting DNA Nucleotides

**Problem ID:** DNA  
**Rosalind Link:** [DNA](https://rosalind.info/problems/dna/)

---

## Problem Description

Given a DNA string, count the occurrence of each nucleotide (A, C, G, T).

### Input Format
A DNA string of length at most 1000 nt.

### Output Format
Four integers (separated by spaces) counting A, C, G, and T respectively.

---

## Biological Context

Nucleotide counting is fundamental to sequence analysis. GC content affects DNA stability, gene expression, and is used in genome assembly quality control.

---

## Sample Dataset

**Input:**
```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

**Output:**
```
20 12 17 21
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
- Basic sequence operations

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

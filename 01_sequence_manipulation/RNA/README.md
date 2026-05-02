# Transcribing DNA into RNA

**Problem ID:** RNA  
**Rosalind Link:** [RNA](https://rosalind.info/problems/rna/)

---

## Problem Description

Convert a DNA string into its RNA transcript by replacing thymine (T) with uracil (U).

### Input Format
A DNA string having length at most 1000 nt.

### Output Format
The transcribed RNA string.

---

## Biological Context

Transcription is the first step of gene expression. DNA is transcribed into mRNA, which is then translated into protein. This is a core concept in molecular biology.

---

## Sample Dataset

**Input:**
```
GATGGAACTTGACTACGTAAATT
```

**Output:**
```
GAUGGAACUUGACUACGUAAAUU
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

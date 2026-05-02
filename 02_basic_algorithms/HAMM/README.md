# Counting Point Mutations

**Problem ID:** HAMM  
**Rosalind Link:** [HAMM](https://rosalind.info/problems/hamm/)

---

## Problem Description

Calculate the Hamming distance between two DNA strings of equal length.

### Input Format
Two DNA strings s and t of equal length (at most 1 kbp).

### Output Format
The Hamming distance dH(s,t).

---

## Biological Context

Point mutations are single nucleotide changes. Hamming distance quantifies genetic divergence between sequences and is foundational to sequence alignment scoring.

---

## Sample Dataset

**Input:**
```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```

**Output:**
```
7
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

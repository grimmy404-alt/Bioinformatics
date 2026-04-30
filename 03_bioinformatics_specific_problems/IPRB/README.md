# Mendel's First Law

**Problem ID:** IPRB  
**Rosalind Link:** [IPRB](https://rosalind.info/problems/iprb/)

---

## Problem Description

Calculate the probability that two randomly selected organisms will produce an offspring with a dominant allele.

### Input Format
Three positive integers k, m, and n representing counts of homozygous dominant, heterozygous, and homozygous recessive organisms.

### Output Format
The probability that two randomly selected organisms produce an individual with at least one dominant allele.

---

## Biological Context

Mendelian genetics describes inheritance patterns. Understanding probability in genetics is crucial for variant calling, GWAS studies, and population genetics.

---

## Sample Dataset

**Input:**
```
2 2 2
```

**Output:**
```
0.78333
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

**Author:** Nilesh  
**Date Solved:** 2024

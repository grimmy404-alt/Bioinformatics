**Problem ID:** SUBS  
**Rosalind Link:** [SUBS](https://rosalind.info/problems/subs/)

---

## Problem Description

Given two DNA strings s and t, find all starting positions where t appears as a substring of s.

### Input Format
Two DNA strings s and t (each of length at most 1 kbp).

### Output Format
All locations of t as a substring of s (using 1-based indexing, space-separated).
---

## Biological Context

Motif finding is one of the most fundamental tasks in bioinformatics. DNA motifs are short, recurring patterns that often have biological significance:

Transcription Factor Binding Sites (TFBS)
Restriction Enzyme Recognition Sites
Promoter Elements
Splice Sites
Primer Binding Sites

In real bioinformatics pipelines, motif finding is used in:

ChIP-seq analysis (finding where proteins bind to DNA)
Gene regulatory network reconstruction
Genome annotation and feature prediction
Comparative genomics (finding conserved regulatory elements)
---

## Sample Dataset

**Input:**
```
GATATATGCATATACTT
ATAT
```

**Output:**
```
2 4 10
```

---

## Solution Approach

This solution uses a sliding window approach:

1. Read the DNA string s and the motif t
2. Slide a window of length len(t) across the string s
3. At each position i, check if s[i:i+len(t)] matches t
4. If it matches, record position i+1 (using 1-based indexing as per Rosalind convention)
5. Output all matching positions separated by spaces

---

### Key Concepts Used
- String slicing and comparison
- Sliding window technique
- 1-based vs 0-based indexing conversion
- File I/O and string parsing

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
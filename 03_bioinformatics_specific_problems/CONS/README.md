**Problem ID:** CONS  
**Rosalind Link:** [CONS](https://rosalind.info/problems/cons/)

---

## Problem Description

Given a collection of DNA strings of equal length, construct:
1. A **profile matrix** - a 4×n matrix where each row represents the count of A, C, G, or T at each position
2. A **consensus string** - formed by taking the most common nucleotide at each position

### Input Format
A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

### Output Format
- First line: consensus string
- Following lines: profile matrix (one row per nucleotide: A, C, G, T)

---

## Biological Context

Consensus sequences are fundamental in bioinformatics for identifying conserved patterns across multiple sequences:

- **Multiple Sequence Alignment (MSA)**: Consensus represents the most conserved nucleotides
- **Transcription Factor Binding Sites**: Consensus motifs show preferred binding sequences
- **Phylogenetic Analysis**: Conserved positions indicate functional importance
- **Sequence Logo Generation**: Profile matrices are used to create visual representations of conservation
- **Promoter Prediction**: Consensus sequences help identify regulatory elements

In real bioinformatics pipelines, consensus finding is used in:

- ChIP-seq peak analysis (identifying binding motifs)
- RNA-seq for splice site prediction
- Genome assembly quality assessment
- Primer design for PCR (choosing conserved regions)
- Vaccine design (identifying conserved epitopes)

---

## Sample Dataset

**Input:**
```
Rosalind_1
ATCCAGCT
Rosalind_2
GGGCAACT
Rosalind_3
ATGGATCT
Rosalind_4
AAGCAACC
Rosalind_5
TTGGAACT
Rosalind_6
ATGCCATT
Rosalind_7
ATGGCACT
```

**Output:**
```
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
````

---

---

## Solution Approach

This solution uses a position-by-position counting strategy:

1. **Parse FASTA format**: Extract DNA sequences, skipping header lines (lines starting with `>`)
2. **Initialize profile dictionary**: Create a dictionary mapping each nucleotide to a list of zeros (length = sequence length)
3. **Build profile matrix**: 
   - For each position i across all sequences
   - Count occurrences of A, C, G, T at that position
   - Store counts in the profile dictionary
4. **Construct consensus string**:
   - For each position, find which nucleotide has the maximum count
   - Append that nucleotide to the consensus string
5. **Format output**: Print consensus, then profile matrix rows

---

### Key Concepts Used
- FASTA file parsing with `startswith()`
- Dictionary of lists for tabular data storage
- Nested loops (position iteration + sequence iteration)
- Finding maximum values in dictionaries
- String building with `+=`
- Output formatting with unpacking operator `*`

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

#parsing fasta files
file= input("Enter File Name:")
with open(file,"r") as f:
    data= f.read().splitlines()

#initialising DNA array
DNA_array= []
current_sequence=""     #saves current running sequence

#constructing the DNA string matrix
for line in data:
    if line.startswith(">"):
        if current_sequence:        # checks if the string is not empty. Empty string is "falsy", so this means "if we have something to save"(note for self)
            DNA_array.append(current_sequence)
        current_sequence=""
    elif line.strip():
        current_sequence += line.strip()

if current_sequence:
    DNA_array.append(current_sequence)

#initialising profile dictionary
n= len(DNA_array[0])
profile_dict= {'A':[0]*n,'C':[0]*n,'G':[0]*n,'T':[0]*n}

#constructing profile
for i in range(n):
    for string in DNA_array:
        nucleotide= string[i]
        profile_dict[nucleotide][i]+= 1

#initialising and constructing consensus 
consensus= ""

for i in range(n):
    counts= {'A':profile_dict['A'][i],
            'C':profile_dict['C'][i],
            'G':profile_dict['G'][i],
            'T':profile_dict['T'][i]
            }
    
    max_value= max(counts.values())

    for nucleotide , count in counts.items():
        if count== max_value:
            consensus += nucleotide
            break

#printing in desired format
print(consensus)

for nucleotide in ["A","C","G","T"]:
    print(nucleotide + ":", *profile_dict[nucleotide])      #here * was used for unpacking(note for self)
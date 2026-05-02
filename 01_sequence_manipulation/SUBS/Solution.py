#parsing input data
file= input("Enter File Name:")
with open(file,"r") as f:
    data= f.read().split("\n")

#storing DNA string and motif
s= data[0]
t= data[1]

#validating constriants
if len(s)<len(t):
    exit()

motif_length= len(t)
positions=[]

#core logic
for i in range(len(s)-len(t)+1):        #reads DNA string linearly within valid frame
    if s[i:i+motif_length]== t:         #compares current string slice with motif
        positions.append(i+1)

result= " ".join(str(i) for i in positions)     #stores result in required format

print (result)
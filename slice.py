string= input()
indices= input()

parts= indices.split()
a= int(parts[0])
b= int(parts[1])
c= int(parts[2])
d= int(parts[3])

s1= string[a:(b+1)]
s2= string[c:(d+1)]

print (s1+" "+s2)

s1 = input("Enter the first String: ")
s2 = input("Enter the second String: ")
output=""
i=0
j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output+s1[i]
        i+=1
    if j<len(s2):
        output = output+s2[j]
        j+=1

print(output)


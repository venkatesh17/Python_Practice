
s=input("Enter the Something: ")
l=s.split()
newWords = [word[::] for word in l[::-1]] 
print(newWords)      

output = " ".join(newWords)
print(output)


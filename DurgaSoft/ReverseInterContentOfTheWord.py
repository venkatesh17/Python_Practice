s=input("Enter Something: ")

l=s.split(" ")
newwords = [word[::-1] for word in l]

print(" ".join(newwords))

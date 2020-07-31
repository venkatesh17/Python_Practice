
s=input("Enter the String: ")
# print(s[::-1])

# print("".join(reversed(s)))

i=len(s)-1
target=""

while i>=0:
    target=target+s[i]
    i=i-1

print(target)
s=input("Enter Some String:")
# print("Characters at Even Position:",s[0::2])
# print("Characters at Odd Position:",s[1::2])


i=0
while i<len(s):
    if s[i]!=' ':
        print(s[i],end=",")
    i=i+2

print()
i=1
while i<len(s):
    if s[i]!=' ':
        print(s[i], end=",")

    i=i+2

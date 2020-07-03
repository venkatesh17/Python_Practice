# s.replace(oldstring,newstring)
# inside s, every occurrence of oldstring will be replaced with newstring.

s="difficult Learning Python is very difficult"
s1=s.replace("difficult","easy")

print(s1)

# easy Learning Python is very easy

s="ababababababab"
s1=s.replace("a","b")
print(s, id(s))
print(s1, id(s1))

# bbbbbbbbbbbbbb


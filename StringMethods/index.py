# index()	Searches the string for a specified value and returns 
# the position of where it was found

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)



txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)


txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))



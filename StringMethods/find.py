# find()	Searches the string for a specified value and returns 
# the position of where it was found

txt = "Hello , welcome to my world. welcome"
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)


txt = "Hello, welcome to my world."
x = txt.find("e", 10, 100)
print(x)


txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))


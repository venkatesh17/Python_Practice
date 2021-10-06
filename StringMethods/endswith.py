# endswith()	Returns true if the string ends with the specified value

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("welcome", 5, 11)
print(x)


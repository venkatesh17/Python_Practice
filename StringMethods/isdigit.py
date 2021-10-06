# isdigit()	Returns True if all characters in the string are digits

txt = "50800"
x = txt.isdigit()
print(x)

txt = "gffgfd"
x = txt.isdigit()
print(x)


a = "\u0030" #unicode for 0
# b = "00B2" #unicode for ²

print(a.isdigit())
# print(b.isdigit())

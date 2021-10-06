# format()	Formats specified values in a string

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'am {1}".format("John",36)
txt3 = "My name is {}, I'am {}".format("John",36)

print(txt1) 
print(txt2)
print(txt3)


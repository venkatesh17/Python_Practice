# isalnum()	Returns True 
# if all characters in the string are alphanumeric

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)


txt = "Company%#12"
x = txt.isalnum()
print(x)

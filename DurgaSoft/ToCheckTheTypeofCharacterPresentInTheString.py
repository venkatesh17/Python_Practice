"""
1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
3) isdigit(): Returns True if all characters are digits only( 0 to 9)
4) islower(): Returns True if all characters are lower case alphabet symbols
5) isupper(): Returns True if all characters are upper case aplhabet symbols
6) istitle(): Returns True if string is in title case
7) isspace(): Returns True if string contains only spaces



print('Durga786'.isalnum()) #True
print('durga786'.isalpha()) #False
print('durga'.isalpha()) #True
print('durga'.isdigit()) #False
print('786786'.isdigit()) #True
print('abc'.islower()) #True
print('Abc'.islower()) #False
print('abc123'.islower()) #True
print('ABC'.isupper()) #True
print('Learning python is Easy'.istitle()) #False
print('Learning Python Is Easy'.istitle()) #True
print(' '.isspace()) #True
"""


s=input("Enter any character:")
if s.isalnum():
    print("Alpha Numeric Character")
    if s.isalpha():
      print("Alphabet character")
      if s.islower():
        print("Lower case alphabet character")
      else:
        print("Upper case alphabet character")
    else:
     print("it is a digit")
     
elif s.isspace():
    print("It is space character")
else:
    print("Non Space Spacial Characters")
"""
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
"""

n= int(input("Enter the number of Rows: "))
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(64+i), end=" ")
    print()

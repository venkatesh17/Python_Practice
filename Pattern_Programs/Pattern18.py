"""
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
"""
n= int(input("Enter the number of Rows: "))
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print
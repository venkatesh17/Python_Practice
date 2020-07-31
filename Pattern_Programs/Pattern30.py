"""
  999999999
   88888888
    7777777
     666666
      55555
       4444
        333
         22
          1
"""

n=int(input("Enter the number of Rows: "))
for i in range(1, n+1):
    print(" "*(i-1),str(n+1-i)*(n+1-i))
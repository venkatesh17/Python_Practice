"""
          *
         * *
        * * *
       * * * *
      * * * * *
     * * * * * *
    * * * * * * *
   * * * * * * * *
  * * * * * * * * *
 * * * * * * * * * *
"""

n=int(input("Enter the number of Rows: "))
for i in range(1, n+1):
    print(" "*(n-i),"* "*i, end=" ")
    print()


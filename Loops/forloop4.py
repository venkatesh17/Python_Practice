from random import randint

rand_num = randint(1,5)
for i in range(6):
    print('Hello '*rand_num)


for i in range(6):
    rand_num = randint(1,5)
    print('Hello'*rand_num)



count = 0
for i in range(10000):
    num = randint(1, 100)
    if num%12==0:
        count=count+1
        
print('Number of multiples of 12:', count)

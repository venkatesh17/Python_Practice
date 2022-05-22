
largest = eval(input('Enter a positive number: '))
for i in range(9):
    num = eval(input('Enter a positive number: '))
    if num>largest:
        largest=num
print('Largest number:', largest)


# ==================================================================
num = eval(input('Enter number: '))
flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1
if flag==1:
    print('Not prime')
else:
    print('Prime')


#================================================================
count = 0
for i in range(10):
    num = 15 # eval(input('Enter a number: '))
    if num>10:
        count=count+1

print('There are', count, 'numbers greater than 10.')

#===========================================

count = 0
for i in range(1,101):
    if (i**2)%10==4:
        print(i)
        count = count + 1

print(count)


# ===================================
s = 0
for i in range(1,101):
    s = s + i
print('The sum is', s)

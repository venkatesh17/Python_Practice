from random import randint

x=randint(1,10)

# print('A random number between 1 and 10: ', x)

guess = eval(input("Enter your guess: "))

if(x==guess):
    print("you got it")
else:
    print("sorry, you missed it", x)

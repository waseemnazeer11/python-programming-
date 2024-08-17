
"""Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses"""
import random

def guess():
    print('please Enter the two number to specify the range')
    a = int(input('please Enter the first integer: '))
    b = int(input('please Enter the second integer: '))

    c = random.randint(a,b)
    
    i = 0
    while (i < 7):
        d = int(input("please Enter the number to guess: "))
        i +=1
        if (d==c):
            print('Congratulations you guess the number corretly')
            break
        elif (d > c):
            print('your guess is too high')
        else:
            print('your guess is too low')
                
guess()
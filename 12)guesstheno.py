import random
x=random.randint(1,20)
print('I have thought of a number between 1 and 20')
#the player can guess the secret number upto 7 times.
for guesstaken in range(1,8):
    print('take a guess:')
    guess=int(input())
    if guess<x:
        print('guess is lower than the secret number')
    elif guess>x:
        print('guess is higher than secret number')
    else:
        break #this condition is the correct guess ^^
if guess==x:
    print('you is right!'+ str(x)+ 'was the number i thought of~~')
else:
    print('aigoo '+str(x)+' was the number i thought of')

import random

def getans(ansno):
    if ansno==1:
        return 'its certain'
    elif ansno==2:
        return 'its decidedly so'
    elif ansno==3:
        return 'yep'
    elif ansno==4:
        return 'reply hazy, try again~'
    elif ansno==5:
        return 'better luck next time'
    elif ansno==6:
        return 'think of a better question'
    elif ansno==7:
        return 'nope, not gonna happen'
    elif ansno==8:
        return 'not good enough'
    elif ansno==9:
        return 'issa doubtful'

print("think of a yes/no question to see where your luck lies.")
print(getans(random.randint(1,9)))

print('how many times do you want to play?')
z=int(input())
import sys
if z ==0:
    sys.exit()
else:
    for i in range (0,z):
        import random
        c=random.randint(1,3)
        print('lets play rock,paper, and scissors')
        print('enter 1 for rock, 2 for paper and 3 for scissors.')
        x=int(input())
        if x>3:
            print('invalid input given, try again')
            sys.exit
        elif x==c:
            print('its both same~')
        elif x==1 and c==2:
            print('i win!')
        elif x==2 and c==1:
            print('whoa,you win~')
        elif x==3 and c==2:
            print('you winnn')
        elif x==2 and c==3:
            print('i winzzz')
        elif x==1 and c==3:
            print('you  won')
        else:
            print('i winnn')

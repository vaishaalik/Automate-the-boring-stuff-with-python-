print('Hi there! Enter 1 if you are in gryffindor')
print('2 if you are in slytherin')
print('3 if you are in ravenclaw')
print('and 4 if you are in hufflepuff')
house=int(input())
while (house!=1 and house!=2 and house!=3 and house!=4):
    print('invalid input,try again')
    house=int(input())
while (house>=1 and house<=4):
    print('thats cool')
    if(house==4):
        print('ah! you are in hufflepuff~~')
        break
    elif(house==2):
        print("damn, your in sytherin.... that's amazzzing")
        break
    elif(house==1):
         print('Oh! you are in the same house as harry! coolio')
         break
    else:
        print('i am in ravenclaw too!!')
        break
print('thanks, lets meet again!')


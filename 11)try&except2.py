print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('So manyyy')
    else:
        print('ah, thats not much')
except ValueError:
    print('please enter a number as input')

#we get a ValueError when input is say given as, six instead of 6.
#So, thats why we put in try and except.

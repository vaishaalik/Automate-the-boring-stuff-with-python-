def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError: #or even just except: =>this'll accept all kind of errors
        print('Error:You tried to divide by zero.')
        
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

#Remember: Functions that return without a return statement return the 'None' value.

def perfect_square (x):
    y = int(x**(1/2))

    if x == 0 :
        return True

    elif x/y != y:
        return False
    else:
        return True
    
print(perfect_square(0))
    

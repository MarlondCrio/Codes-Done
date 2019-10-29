def prime(x):
    if x == 0 or x == 1:
        return False
    else:
        count = 0
        for y in range(2,x):
            z = divmod (x,y)
            if z[1] == 0:
               count = count + 1
            else:
                pass
        if count != 0:
            return False
        else:
            return True
print (prime(6897))

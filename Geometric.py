numbers = [ 0]

total=1
if len(numbers)== 0 :
    print(None)
else:
    for nums in numbers:
        total= total * nums
    num_num= len(numbers)
    Avg = total**(1/num_num)
    print (Avg)

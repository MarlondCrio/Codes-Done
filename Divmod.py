dividend = 0
divisor = 7
Answer = 0
if dividend != 0:
    while dividend > 0 :
        dividend = dividend-divisor
        Answer = Answer + 1
    if dividend != 0 :
        Remainder= dividend + divisor
        print (Answer-1)
        print (Remainder)
    elif dividend == 0 :
        Remainder = 0
        print (Answer)
        print (Remainder)
else:
    print(Answer)
    print(0)

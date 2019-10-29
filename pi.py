p_d = 8021
p_c= int(p_d/2)
count=0
count2=0
for x1 in range(-p_c, p_c+1):
    for y1 in range(-p_c, p_c+1):
        z=(x1**2)+(y1**2)
        if ((z**(1/2))<= p_d/2) :
            count = count + 1
        else:
            a=3
for x1 in range(-p_c, p_c+1):
    for y1 in range(-p_c, p_c+1):
        count2 = count2 + 1

print( (count/count2)* 4)

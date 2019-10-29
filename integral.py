poly = [7,0,3]
const = 5
count = 1
integral=[]
if poly != []:
    integral.append(const)
    for element in poly:
        if count==1:
            integral.append(poly[0])
            count= count+1
        else:
            integral.append(poly[count-1]/count)
            count = count + 1
    print(integral)
else:
    print([const])
            
         

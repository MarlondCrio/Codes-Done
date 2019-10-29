def ndoors(x):
    n = x
    a = list ( range ( 1, n + 1))
    locked = []
    l = locked               ##list of potential values of doors
    while len(l) < n :
        l.append(0)

        
    for element in a:
        multi_list = [element]
        count= 1
        while element < n and count < n // element :
            count= count + 1
            z = element * count
            multi_list.append(z)
            
        for nums in multi_list:
            if l[nums-1] == 0:
                l[nums-1] = 1
            else:
                l[nums-1] = 0
    doors = 0
    for things in l:
        if things == 1 : 
            doors = doors + 1
        else:
            pass
    final=[]
    count2 = 0
    for bees in l:
        if bees == 0:
            count2= count2 + 1

        else:
            count2 = count2 + 1
            final.append(count2)
    ans = final
    return ans
print(ndoors(1000))

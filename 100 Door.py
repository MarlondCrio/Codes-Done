def creat_multiples(y):
    multi_list = [y]
    count= 1
    while y < 100 and count < 100 // y :
        count= count + 1
        z = y * count
        multi_list.append(z)
    return multi_list



locked = []

l = locked               ##list of potential values of doors
while len(l) < 100 :
    l.append(0)

a = list ( range ( 1, 101))
  
for elements in a:
    b = creat_multiples(elements)
    for nums in b:
        if l[nums-1] == 0:
            l[nums-1] = 1
        else:
            l[nums-1] = 0
print (l)

doors = 0
for things in l:
    if things == 1 : 
        doors = doors + 1
    else:
        pass
print ( doors )
final=[]
count2 = 0
for bees in doors:

    if bees == 0:
        count2= count2 + 1

    else:
        count2 = count2 + 1
        final.append(count2)
print (final)

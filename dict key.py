def swap(d,k1,k2):
    d[k2], d[k1] = d[k1], d[k2]
    return None

d1 = {'cat':7, 'coca':'cola', (1,2):3.2, 7:[1,2,3], 'hunde':'dogs', 'sieben':[1,2,3], 'dog':7, 'hamster':7}
swap(d1,'hunde','sieben')
print(d1)

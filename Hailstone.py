import sys
sys.setrecursionlimit(100000)
def hailstone_sequence(a_0):
    procs = [a_0]
    a_k = a_0
    while a_k != 1:
        if a_k % 2 == 0:
            a_k = a_k/2
            procs.append(a_k)
            
        else:
            a_k = 3*a_k + 1
            procs.append(a_k)
    return procs

print(hailstone_sequence(4543))

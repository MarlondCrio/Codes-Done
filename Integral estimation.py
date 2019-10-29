def approx_integral(f, lo, hi, num_regions):

    span = list(range (1, num_regions + 1))

    height = ((hi - lo)/num_regions)

    def g(x):
        return f(x)

    start = g(lo)
    
    for trap in span:
        if trap == 1:
            area = (g(lo)+ g(lo+height))*.5*height
        elif trap == num_regions + 1 :
            pass
        else:
            area = area + (g(lo+(trap-1)*height)+ g(lo+(trap)*height))*.5*height
        
    return area

print(approx_integral(lambda x : 2*x, 0, 4, 10))

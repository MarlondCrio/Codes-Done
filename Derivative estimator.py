def approx_derivative(f, x, delta = 1e-6):
   
    def a(x):
        return f(x+delta)
    def b(x):
        return f(x-delta)
    c = (a(x)-b(x))/(2*delta)
    return c
    
print( approx_derivative(lambda x : x + 2, 8.98))

def approx_derivative_2(f, delta = 1e-6):
    def g(x):
            return ((f(x+delta))-(f(x-delta)))/(2*delta)
    return g

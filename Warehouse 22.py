class Warehouse:

    def __init__(self):
        self.x = {}

    def process(self,y):
        
        if y[1] not in self.x.keys():
            self.x[(y[1])] = y[2]
        
        else:
            if y[0] == 'receive':
                self.x[(y[1])] += y[2]

            elif y[0] == 'ship':
                self.x[(y[1])] -= y[2]
                
        return self.x 

    def lookup(self,z):
        if z in self.x.keys():
            return (self.x[z])
        else:
            return 0


w = Warehouse()
w.process(('receive', 'a', 10))
print(w.lookup('a'))

class Vector:


    def __init__( self, x ):
        self.list = x


    def as_list(self):
        return self.list


    def size(self):
        return len(self.list)


    def magnitude(self):
        a = 0
        for elements in self.list:
            a = a + elements**2
        return a**.5


    def euclidean_distance(self,other):
        if len(self.list) == len(other.list):
            b = 0
            mag = Vector( self.list)
            for elements in range(len(other.list)):
                mag.list[elements] = (self.list[elements] - other.list[elements])**2
            for things in mag.list:
                b = things + b
            return b**.5

    def normalized(self):
        norm = Vector(self.list)
        a = self.magnitude()
        for elements in range(len(self.list)):
                norm.list[elements] = self.list[elements]/a
        return norm
            

    def cosine_similarity(self,other):
        sim = 0

        for elements in range(len(self.list)):
            sim = sim + self.list[elements]*other.list[elements]
        sim = sim / (self.magnitude()*other.magnitude())
        return sim        

    def __add__ (self, other):

        if type(other) != Vector:
            return None
        

        elif type(other) == Vector :
            
            if len(self.list) == len(other.list):
                new = Vector(self.list)
                for elements in range(len(other.list)):
                    new.list[elements] = self.list[elements] + other.list[elements]
                return new
        else:
            return None

    def __sub__(self,other):
        if type(other) != Vector:
            return None
            
        elif len(self.list) == len(other.list):

            minus = Vector(self.list)

            for elements in range(len(other.list)):
                minus.list[elements] = self.list[elements] - other.list[elements]

            return minus

        else:
            return None

    def __mul__(self,other):

        if type(other) == int or type(other) == float:
            mult = Vector(self.list)

            for elements in range(len(self.list)):
                mult.list[elements] = mult.list[elements] * other
            return mult

        elif type(other) == Vector:
            
            if self.size() == other.size():

                dot = 0

                a = Vector(self.list)
                for elements in range(self.size()):
                    dot = dot + self.list[elements] * other.list[elements]
                return dot

            elif self.size != other.size:
                return None
        elif type(other) != Vector or type(other) != int or type(other) != float:
            return None
        
        
       
        else:
            return None


    def __truediv__(self,other):

        if type(other) == int or type(other) == float:
            if other == 0 or other == 0.0:
                return None
            else:
                div = Vector(self.list)

                for elements in range(len(self.list)):
                    div.list[elements] = div.list[elements]/other
                return div
        else:
            return None

class Matrix:

    def __init__(self, x):
        self.grand_list = x

    def size(self):
        count_row = 0
        count_col = 0
        
        for elements in self.grand_list[0]:
            count_col = count_col + 1
            
        for items in self.grand_list:
            count_row = count_row + 1

        return(count_row, count_col)

    def get(self,r,c):
        return self.grand_list[r][c]

    def set(self,r,c,val):
        self.grand_list[r][c] = val


    def row(self,n):
        return self.grand_list[n]

    def col(self,n):
        col=[]
        for elements in range(self.size()[0]):
            col.append(self.get(elements,n))
        return col


    def transpose(self):
        initial_row = self.size()[0]
        initial_col = self.size()[1]
        new = Matrix([])
        for elements in range(self.size()[1]):
            new.grand_list.append(self.col(elements))
            print([self.col(elements)])
        return new


    def __mul__(self,other):

    
        if isinstance(other,Matrix):
            
                rows = self.size()[0]
                cols = self.size()[1]
                rows2 = other.size()[0]
                cols2 = other.size()[1]
                mult = Matrix([])
                grand = []
                adding = []

                if cols == rows2:
                    for r in range(rows):
                        
                        new = 0
                        
                        for c in range(cols2):

                            new = 0
                            for z in range(rows2):
            
                               new = new + self.grand_list[r][z]*other.grand_list[z][c]
                            print (new)
                            adding.append(new)
                        grand.append(adding)
                        
                        adding = []
                        
                    mult.grand_list = grand    
                    return mult
                else:
                    return None
        elif isinstance(other,int) or isinstance(other,float):
                back = Matrix(self.grand_list)
                for elements in range(self.size()[0]):
                    for items in range(self.size()[1]):
                        back.grand_list[elements][items] = back.grand_list[elements][items]*other
                return back

        
            
    def __add__(self,other):
        
        if isinstance(other,int)or isinstance(other,float):
            back = Matrix(self.grand_list)

            for elements in range(self.size()[0]):
                for items in range(self.size()[1]):
                    back.grand_list[elements][items] = back.grand_list[elements][items]+other

            return back

        elif isinstance(other,Matrix) and (self.size() == other.size()):
            rows = self.size()[0]
            cols = self.size()[1]
            new2 = Matrix(self.grand_list)
        
            for elements in range (rows):
                    for items in range (cols):
                        new2.grand_list[elements][items] = new2.grand_list[elements][items] + other.grand_list[elements][items]
            return new2
        else:
            return None

    def __sub__(self,other):

       
        if isinstance(other,Matrix) and (self.size() == other.size()):

            rows = self.size()[0]
            cols = self.size()[1]
            new2 = Matrix(self.grand_list)
        

            for elements in range (rows):
                for items in range (cols):
                    new2.grand_list[elements][items] = new2.grand_list[elements][items] - other.grand_list[elements][items]
            return new2
     



        elif isinstance(other,int)or isinstance(other,float):


        


            back = Matrix(self.grand_list)
            for elements in range(self.size()[0]):
                    for items in range(self.size()[1]):
                        back.grand_list[elements][items] = back.grand_list[elements][items]-other
            return back

        else:
            return None












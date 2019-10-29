class Rational:

    def __init__(self, num, den):
        self.top = num
        self.bot = den

    def get_denominator(self):
        return self.bot

    def get_numerator(self):
        return self.top

    def to_float(self):
        a = self.top/self.bot
        return a

    def reciprocal(self):
        b = Rational(self.bot,self.top)
        return b

    def gcd(self):
        a = self.bot
        b = self.top
        r = 0
        if a < b :
            a,b=b,a
        r = a % b
        if r == 0:
            return b
        while r != 0: 
            a = b
            b = r 
            r = a%b
        return b
    
    def reduce(self) :
        a = self.gcd()
        b = Rational(self.top,self.bot)
        b.top = self.top//a
        b.bot = self.bot//a
        return b

    def __add__(self,other):

        if type(other) == Rational:

            if self.bot == other.bot:
                b = Rational(self.top,self.bot)
                b.top += other.top
                
                return b
            else:
                b = Rational(self.top,self.bot)
                b.bot = self.bot*other.bot
                b.top = self.top*other.bot + other.top*self.bot
                return b

        elif type(other) == int:
            b = Rational(self.top,self.bot)
            b.top = other*self.bot + self.top
            return b

        elif type(other) == float:
            a = self.top
            b = self.bot
            c = a/b
            return other + c
        else:
            return None

    def __mul__(self,other):

        if type(other) == Rational:
                b = Rational(self.top,self.bot)
                b.bot = self.bot*other.bot
                b.top = self.top*other.top
                return b

        elif type(other) == int:
            b = Rational(self.top,self.bot)
            b.top = other*self.top
            
            return b

        elif type(other) == float:
            a = self.top
            b = self.bot
            c = a/b
            return other * c

    def __truediv__(self,other):
        b = Rational(self.top,self.bot)
        if type(other) == Rational:
                b.bot = self.bot*other.top
                b.top = self.top*other.bot
                return b

        elif type(other) == int:
            b.bot = other*self.bot
            
            return b

        elif type(other) == float:
            a = self.top
            b = self.bot
            c = a/b
            return c/other
    def __sub__(self,other):

        b = Rational(self.top,self.bot)
        
        if type(other) == Rational:

            if self.bot == other.bot:
                b.top -= other.top
                return b
            else:
                b.bot = self.bot*other.bot
                b.top = self.top*other.bot - other.top*self.bot
                return b

        elif type(other) == int:
            b.top = self.top - other*self.bot
            return b

        elif type(other) == float:
            a = self.top
            b = self.bot
            c = a/b
            return c - other
        else:
            return None


        

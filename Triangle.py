import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)


def check(x,y):
        if abs(x-y) <= .00000001:
            return True
        else:
            return False


        
class Triangle:
        
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        pass

    def side_lengths(self):
        s1 = self.a.euclidean_distance(self.b)
        s2 = self.b.euclidean_distance(self.c)
        s3 = self.c.euclidean_distance(self.a)
        return (s1,s2,s3)

    def angles(self):
        a = self.side_lengths()[0]
        b = self.side_lengths()[1]
        c = self.side_lengths()[2]

        A = math.acos(((a**2) - (b**2) - (c**2)) / (-2*b*c) )
        B = math.acos(((b**2) - (a**2) - (c**2)) / (-2*a*c) )
        C = math.acos(((c**2) - (a**2) - (b**2)) / (-2*a*b) )
        return(A,B,C)

    def side_classification(self):
        s1 = self.side_lengths()[0]
        s2 = self.side_lengths()[1]
        s3 = self.side_lengths()[2]

        if (check(s1,s2) == True and check(s1,s3) == False ) \
        or (check(s2,s3) == True and check(s2,s1) == False ) \
        or (check(s1,s3) == True and check(s2,s3) == False ):
            return 'isosceles'
        elif (check(s1,s2) and check(s2,s3) and check(s3,s1)) == True:
            return 'equilateral'
        else:
            return 'scalene'
        
    def angle_classification(self):
        a1 = self.angles()[0]
        a2 = self.angles()[1]
        a3 = self.angles()[2]
        if a1 > (math.pi/2) or a2 > (math.pi/2) or a3 > (math.pi/2):
            return 'obtuse'

        elif check(a1,((math.pi)/2))  or check(a2,((math.pi)/2)) or check(a3,((math.pi)/2)):
            return 'right'

        elif (check(a1,a2) and check(a2,a3) and check(a3,a1)) == True:
            return 'equiangular'
        
        elif a1 <= ((math.pi)/2)  or a2 <= ((math.pi)/2) or a3 <= ((math.pi)/2):
            return 'acute'
        

    def is_right(self):
        a1 = self.angles()[0]
        a2 = self.angles()[1]
        a3 = self.angles()[2]
        if (check(a1,(math.pi/2)) or check(a2,(math.pi/2)) or  check(a3,(math.pi/2))): 
            return True
        else:
            return False

    def area(self):
        A = self.side_lengths()[0]
        B = self.side_lengths()[1]
        c = self.angles()[2]
        area = A*B*math.sin(c)*.5
        return area

    def perimeter(self):
        s1 = self.side_lengths()[0]
        s2 = self.side_lengths()[1]
        s3 = self.side_lengths()[2]

        all_s = s1+s2+s3
        return all_s

    
    def check(x,y):
        if abs(x-y) <= 10**(-6):
            return True
        else:
            return False

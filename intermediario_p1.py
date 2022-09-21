import math

def CalcDist(p1,p2):
    x=p1[0]-p2[0]
    y=p1[1]-p2[1]
    h = math.sqrt(pow(x,2)+pow(y,2))
    return h

def CalcAng(p1,p2,p3):
    a=CalcDist(p2,p3)
    b=CalcDist(p1,p3)
    c=CalcDist(p1,p2)
    Rc=(pow(a,2)+pow(c,2)-pow(b,2))/(2*a*c)
    r=math.degrees(math.acos(Rc))
    return r


print(CalcAng([3,3],[0,0],[3,0]))
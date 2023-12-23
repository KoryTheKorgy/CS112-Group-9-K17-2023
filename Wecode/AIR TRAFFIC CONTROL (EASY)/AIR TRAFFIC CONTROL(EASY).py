import sys

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def CCW(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)>0
def touch(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)==0
def onSegment(a, b, c): 
    if ( (b.x <= max(a.x, c.x)) and (b.x >= min(a.x, c.x)) and 
           (b.y <= max(a.y, c.y)) and (b.y >= min(a.y, c.y))): 
        return True
    return False
def intersect(a,b,c,d):

    if touch(a,b,c) and onSegment(a,c,b):
        return True
    if touch(a,b,d) and onSegment(a,d,b):
        return True
    if touch(c,d,a) and onSegment(c,a,d):
        return True
    if touch(c,d,b) and onSegment(c,b,d):
        return True

    return CCW(a,c,d) != CCW(b,c,d) and CCW(a,b,c) != CCW(a,b,d)
  
t = int(sys.stdin.readline())
for _ in range(t):
    points = []   
    pre = 0
    for i,index in zip(map(int,sys.stdin.readline().split()),range(0,8)):
        if index%2==1:
            points.append(Point(pre,i))
        else:
            pre = i
    if intersect(points[0], points[1], points[2], points[3]): 
        sys.stdout.write('YES\n') 
    else: 
       sys.stdout.write("NO\n")
def clockwise(x1, y1, x2, y2):
    # 1: clockwise, -1: counterclockwise, 0: colinear
    d = x1 * y2 - x2 * y1
    return 0 if d == 0 else 1 if d < 0 else -1

def is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
    cw1 = clockwise(x3 - x1, y3 - y1, x4 - x1, y4 - y1) 
    cw2 = clockwise(x3 - x2, y3 - y2, x4 - x2, y4 - y2)
    cw3 = clockwise(x1 - x3, y1 - y3, x2 - x3, y2 - y3) 
    cw4 = clockwise(x1 - x4, y1 - y4, x2 - x4, y2 - y4)

    if cw1 * cw2 == 0 and cw3 * cw4 == 0:
        if (cw1 + cw2 != 0):
            return True
        else:
            minx1, maxx1 = (x1, x2) if x1 < x2 else (x2, x1)
            miny1, maxy1 = (y1, y2) if y1 < y2 else (y2, y1)
            minx2, maxx2 = (x3, x4) if x3 < x4 else (x4, x3)
            miny2, maxy2 = (y3, y4) if y3 < y4 else (y4, y3)
            return maxx1 >= minx2 and maxx2 >= minx1 and maxy1 >= miny2 and maxy2 >= miny1
    if cw1 * cw2 <= 0 and cw3 * cw4 <= 0:
        return True
    return False    

def check_pos(point, polygon):
    x, y = point
    direction = [0 for _ in range(n)]
    for i in range(-1, n - 1):
        x1, y1, x2, y2 = *polygon[i], *polygon[i + 1]
        direction[i] = clockwise(x1 - x, y1 - y, x2 - x, y2 - y)
        if direction[i] == 0:
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                return 'BOUNDARY'
    n_intersection = 0
    for i in range(-1, n - 1):
        x1, y1, x2, y2 = *polygon[i], *polygon[i + 1]
        if y1 == y and x1 > x:
            if y2 == y:
                direction[i] = direction[i - 1]
                continue
            else:
                if direction[i] * direction[i - 1] == -1:
                    #print(i, x1, y1, x2, y2)
                    n_intersection += 1
        else:
            n_intersection += 1 if is_intersecting(x, y, 1000000000, y, x1, y1, x2, y2) else 0
    #print(direction)
    #print(n_intersection)
    if n_intersection % 2 == 0:
        return 'OUTSIDE'
    return 'INSIDE'

n, m = map(int, input().split())
polygon = [0 for _ in range(n)]
for i in range(n):
    polygon[i] = tuple(map(int, input().split()))
for j in range(m):
    point = tuple(map(int, input().split()))
    print(check_pos(point, polygon))
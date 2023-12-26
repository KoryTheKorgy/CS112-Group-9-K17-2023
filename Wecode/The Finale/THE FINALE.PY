def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def direction(x, y, z):
    return cross([y[0] - x[0], y[1] - x[1]], [z[0] - y[0], z[1] - y[1]])


n = int(input().strip())
for i in range(n):
    s = list(map(int, input().split()))
    d = direction(s[0:2], s[2:4], s[4:6])
    if d == 0:
        print("TOUCH")
    elif d > 0:
        print("LEFT")
    elif d < 0:
        print("RIGHT")
import bisect

class OrderedSet:
    def __init__(self):
        self.elements = []

    def add(self, item):
        if item not in self.elements:
            index = bisect.bisect_left(self.elements, item)
            self.elements.insert(index, item)

    def remove(self, item):
        self.elements.remove(item)

    def __contains__(self, item):
        return item in self.elements

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

class Segment:
  def __init__(self, a, b, x, y, idx):
    self.a = a
    self.b = b
    self.x = x
    self.y = y
    self.idx = idx

  def __lt__(self, other):
    return self.x > other.x
  
  
def sign(x):
  if x == 0:
    return 0
  return -1 if x < 0 else 1

def mul(point1, point2):
   return sign(point1[0] * point2[1] - point1[1] * point2[0])

def sub(point1, point2):
   return (point1[0] - point2[0], point1[1] - point2[1])

'''
    To check if two segments intersect we will use the
    signed area of the ABC triangle. This can be derived
    from the cross product of the vectors AB and AC.
'''
def intersect(segA, segB):
  p1 = (segA.a, segA.b)
  q1 = (segA.x, segA.y)
  p2 = (segB.a, segB.b)
  q2 = (segB.x, segB.y)
  return mul(sub(q2, p1), sub(q1, p1)) * mul(sub(q1, p1), sub(p2, p1)) >= 0 and \
         mul(sub(q1, p2), sub(q2, p2)) * mul(sub(q2, p2), sub(p1, p2)) >= 0

if __name__ == "__main__":
  n = 0
  segments = []
  events = []
  
  n = int(input())
  segments = [0] * n
  for i in range(n):
    a, b, x, y = map(int, input().split(" "))
    if a > x:
      a, x = x, a
      b, y = y, b
    segments[i] = Segment(a,b,x,y,i)
    events.append((a, i, 1))
    events.append((x+1, i, 0))
  events.sort(key=lambda x: (x[0],-x[2]))
  active = OrderedSet()
  counts = [0] * n
  intersections = 0
  for i in events:
    idx = i[1]
    type = i[2]
    if type == 1:
      active.add(segments[idx])
    else:
      for i in active:
        if i.x < segments[idx].a:
          break
        if intersect(i, segments[idx]) and i.idx != idx:
          counts[i.idx]+=1
          counts[idx]+=1
          intersections+=1

  for i in range(n):
    if counts[i] == intersections:
      print(i + 1)
      break
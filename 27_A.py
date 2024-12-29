from math import sqrt
def d(A, B):
    return sqrt((A.x - B.x)**2 + (A.y - B.y)**2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

class Claster:
    def __init__(self):
        self.data = []

    def append(self, x, y):
        self.data.append(Point(x, y))

    def centroid(self):
        if len(self.data) == 0:
            return -1
        msdist = float('inf')
        centroid = Point(0, 0)
        for point1 in self.data:
            sdist = 0
            for point2 in self.data:
                sdist += d(point1, point2)
            if sdist < msdist:
                msdist = sdist
                centroid = point1
        return centroid

    def show(self):
       for point in self.data:
           point.show()

file = open('27_A_19257.txt')
file.readline()

c1, c2 = Claster(), Claster()
for line in file:
    x, y = [float(i.replace(',', '.')) for i in line.split()]
    if y < 6:
        c1.append(x, y)
    else:
        c2.append(x, y)

centroid1 = c1.centroid()
centroid2 = c2.centroid()

P1 = (centroid1.x + centroid2.x) / 2
P2 = (centroid1.y + centroid2.y) / 2

print(abs(P1) * 10000, abs(P2) * 10000)

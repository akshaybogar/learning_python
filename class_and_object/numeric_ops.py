class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point x:{}, y{}'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    # Without defining __add__ below statement will give error
    p3 = p1 + p2
    print(p3)

    p4 = p1 - p2
    print(p4)

    p1 += p2
    print(p1)

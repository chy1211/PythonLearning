class Head:
    def __init__(self, size):
        self.size = size


class Body:
    def __init__(self, capacity):
        self.capacity = capacity


class Hand:
    def __init__(self, length):
        self.length = length


class Leg:
    def __init__(self, width):
        self.width = width


class People:
    def __init__(self):
        self.hd = None
        self.bd = None
        self.lh = None
        self.rh = None
        self.ll = None
        self.rl = None


a = People()
a.hd = Head(20)
a.bd = Body(300)
a.lh = Hand(50)
a.rh = Hand(50)
a.ll = Leg(60)
a.rl = Leg(60)

b = People()
b.hd = Head(18)
b.bd = Body(250)
b.lh = Hand(45)
b.rh = Hand(45)
b.ll = Leg(58)
b.rl = Leg(58)

print(a.hd.size)
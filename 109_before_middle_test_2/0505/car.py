class Car:
    def __init__(self):
        self.lb = None
        self.eg = None
        self.fl = None
        self.fr = None
        self.bl = None
        self.br = None


class Engine:
    def __init__(self, cc):
        self.cc = cc


class wheels:
    def __init__(self, size):
        self.size = size


class Car1:
    def __init__(self):
        self.lb = None
        self.eg = None
        self.wh = None


a = Car()
a.lb = "Porsche"
a.eg = Engine(3000)
a.fl = wheels(20)
a.fr = wheels(20)
a.bl = wheels(20)
a.br = wheels(20)

b = Car1()
b.lb = "Porsche"
b.eg = Engine(3000)
b.wh = []

for i in range(4):
    temp = wheels(20)
    b.wh.append(temp)

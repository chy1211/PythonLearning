class Label:
    def __init__(self, label):
        self.label = label


class Engine:
    def __init__(self, cc):
        self.cc = cc


class FLTire:
    def __init__(self, size):
        self.size = size


class FRTire:
    def __init__(self, size):
        self.size = size


class BLTire:
    def __init__(self, size):
        self.size = size


class BRTire:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self):
        self.lb = None
        self.eg = None
        self.fl = None
        self.fr = None
        self.bl = None
        self.br = None


a = Car()
a.lb = Label("Porsche")
a.eg = Engine(3000)
a.fl = FLTire(20)
a.fr = FRTire(20)
a.bl = BLTire(20)
a.br = BRTire(20)

b = Car()
b.lb = Label("Ferari")
b.eg = Engine(2500)
b.fl = FLTire(19)
b.fr = FRTire(19)
b.bl = BLTire(19)
b.br = BRTire(19)

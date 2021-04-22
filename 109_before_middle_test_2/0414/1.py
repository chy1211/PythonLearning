class Person:
    def __init__(self, name, weight, hp, ap):
        self.name = name
        self.weight = weight
        self.hp = hp
        self.ap = ap

    def eat(self, vol):
        self.weight += vol

    def exercise(self, vol):
        self.weight -= vol

    def underattack(self, who):
        self.hp -= who.ap

    def attack(self, who):
        who.hp -= self.ap


a = Person("a", 50, 2000, 100)
a.eat(5)
a.exercise(4)
print(a)
print(a.name)
print(a.weight)
b = Person("b", 60, 2500, 500)
print(b)
b.eat(3)
b.exercise(5)
print(b.name)
print(b.weight)

a.underattack(b)
a.attack(b)
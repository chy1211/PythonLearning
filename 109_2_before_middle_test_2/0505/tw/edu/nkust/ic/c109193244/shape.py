from math import pi

# import math as m
class Square:
    def __init__(self, length=0.0):
        self.length = length

    def setlength(self, length):
        if length < 0:
            print("error happend")
        self.length = length

    def getlength(self):
        return self.length

    def get_area(self):
        return self.length ** 2

    def get_meter(self):
        return self.length * 4


class Rectangle:
    def __init__(self, length=0.0, width=0.0):
        self.length = length
        self.width = width

    def setlength(self, length):
        self.length = length

    def getlength(self):
        return self.length

    def setwidth(self, width):
        self.width = width

    def getwidth(self):
        return self.width

    def get_area(self):
        return self.length * self.width

    def get_meter(self):
        return (self.length + self.width) * 2


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def setradius(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def get_area(self):
        return pi * self.radius ** 2
        # return m.pi*self.radius**2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self, y):
        self.y = y

    def gety(self):
        return self.y

    def __add__(self):
        return self.x + self.y

    def __mul__(self):
        return self.x * self.y

from tw.edu.nkust.ic.c109193244.shape import Circle
from tw.edu.nkust.ic.c109193244.shape import Square
from tw.edu.nkust.ic.c109193244.shape import Rectangle
from tw.edu.nkust.ic.c109193244.shape import Point

a = Circle(3.0)
print("圓面積", a.get_area())

b = Square(3.0)
print("正方形面積", b.get_area())
print("正方形周長", b.get_meter())

c = Rectangle(3.0, 4.0)
print("長方形面積", c.get_area())
print("長方形周長", c.get_meter())

d = Point(2, 2)
print("加法", d.__add__())
print("乘法", d.__mul__())

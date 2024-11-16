class Point:
    color = 'red'
    circle = 2

a = Point()
b = Point()

a.color = 'black'
a.circle = 9
Point.type_pt = 'disk'
setattr(Point,'prop',1)
a.__dict__

a.circle = 10


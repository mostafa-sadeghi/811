import turtle
s = turtle.Screen()
s.register_shape('strawberry.gif')
p = turtle.Pen()
p.shape('strawberry.gif')
# p.speed('fastest')
# p.speed('slowest')
# p.speed('fast')
p.speed('slow')
'''
   'fastest' : 0
    'fast' : 10
    'normal' : 6
    'slow' : 3
    'slowest' : 1

'''
p.fd(100)
p.lt(120)
p.fd(100)
p.lt(120)
p.fd(100)
p.lt(120)
s.exitonclick()

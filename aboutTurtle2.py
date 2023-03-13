import turtle
import random
# تولید اعداد تصادفی
# number = random.randrange(9)
# print(number)
COLORS = ['red', 'green', 'blue', 'gray', 'cyan', 'gold']
color_index = random.randrange(6)
s = turtle.Screen()
s.bgcolor('black')
# s.bgpic('mario.png')
p = turtle.Pen()
p.pensize(4)
p.pencolor(COLORS[color_index])
# کشیدن اولین مثلث
p.fd(100)
p.right(120)
p.fd(100)
p.right(120)
p.fd(100)
p.right(120)
# کشیدن دومین مثلث
p.fillcolor('green')
p.begin_fill()
p.fd(100)
p.left(120)
p.fd(100)
p.left(120)
p.fd(100)
p.left(120)
p.end_fill()
s.exitonclick()

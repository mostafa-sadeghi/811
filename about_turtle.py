import turtle

s = turtle.Screen()
s.bgcolor('orange')

p = turtle.Pen()
p.pencolor('red')
p.pensize(4)
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
p.shape('square')
# p.forward(100)
# p.left(120)

# p.forward(100)
# p.left(120)

# p.forward(100)

# مربع
p.forward(100)
p.left(90)

p.fd(100)
p.left(90)

p.forward(100)
p.left(90)

p.fd(100)

# exercise 1 : کشیدن پنج ضلعی
# exercise 1 : کشیدن شش ضلعی
# exercise 1 : کشیدن هفت ضلعی
# exercise 1 : کشیدن هشت ضلعی

s.exitonclick()

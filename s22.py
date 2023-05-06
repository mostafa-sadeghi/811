# for i in range(8):
#     for i in range(10):
#         print('*', end=' ')
#     print()

# Ex1
"""
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
"""
# for i in range(10):
#     for j in range(10):
#         print(j, end=' ')
#     print()

# EX2:
"""
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
"""
# for i in range(10):
#     for j in range(10):
#         print(i, end=' ')
#     print()


# for i in range(5):
#     print("python")

# i = 0
# while i < 5:
#     print("python")
#     i = i + 1


import turtle
my_pen = turtle.Turtle()
my_pen.color('red', 'green')
my_pen.pensize(3)

my_pen.begin_fill()
for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)
my_pen.end_fill()

turtle.done()


# with for and while draw:
# مثلث
# پنجضلعی
# کشیدن خانه
# کشیدن ستاره
# کشیدن 12 مربع چرخشی

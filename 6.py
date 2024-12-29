from turtle import *
screensize(1500, 1500)
tracer(0)

k = 30
lt(90)

for _ in range(8):
    fd(16 * k)
    rt(90)
    fd(22 * k)
    rt(90)
up()
fd(5 * k)
rt(90)
fd(5 * k)
lt(90)
down()
for _ in range(8):
    fd(52 * k)
    rt(90)
    fd(77 * k)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
exitonclick()
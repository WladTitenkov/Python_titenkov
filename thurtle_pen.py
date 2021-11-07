import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()


def draw_stairs(n, size=25):  # &lt;- создали функцию, для рисования
    for i in range(0, n):  # &lt;- цикл нарисует указанное количество ступеней
        turtlePen.left(90)
        turtlePen.forward(size)
        turtlePen.right(90)
        turtlePen.forward(size)


turtlePen.speed(5)
draw_stairs(6)
turtle.done()
import turtle

def draw_spiral(t, angle, turns):
    """Draws a spiral with turns of size sz with angle"""
    for i in range(4*turns):
        t.forward(i)
        t.left(angle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pencolor('blue')
alex.fillcolor('blue')
alex.pensize(1)

draw_spiral(alex, 89, 5)
wn.mainloop()

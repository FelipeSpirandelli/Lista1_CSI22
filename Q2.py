import turtle

def draw_poly(t, n, sz):
    """Make turtle t draw a regular polygon of size sz."""
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pencolor('pink')
tess.fillcolor('pink')
tess.pensize(3)

# Draws the squares of different sizes
draw_poly(tess, 8, 50)
wn.mainloop()

import turtle

def draw_square(t, sz):
    """Make turtle t draw a centralized square of size sz."""
    # Moves the turtle to the upper right corner of the square
    t.up()
    t.home()
    t.forward(sz/2)
    t.left(90)
    t.forward(sz/2)
    t.left(90)
    t.down()
    # Draws the square
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pencolor('pink')
alex.fillcolor('pink')
alex.pensize(3)

# Draws the squares of different sizes
draw_square(alex, 20)
draw_square(alex, 40)
draw_square(alex, 60)
draw_square(alex, 80)
draw_square(alex, 100)
wn.mainloop()

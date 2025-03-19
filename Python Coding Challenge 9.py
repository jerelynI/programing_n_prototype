import turtle

def lt(bob, degrees):
    bob.left(degrees)

def rt(bob, degrees):
    bob.right(degrees)

def fd(bob, distance):
    bob.forward(distance)

def polygon(bob, n, length):
    angle = 360 / n
    for _ in range(n):
        fd(bob, length)
        lt(bob, angle)

bob = turtle.Turtle()
n_values = [3, 4, 5, 6, 7, 8]
length = 100

for n in n_values:
    polygon(bob, n, length)
    bob.penup()  # Lift the pen to move without drawing
    bob.setposition(0, 0)  # Return to starting position
    bob.pendown()  # Put the pen down to start drawing again

turtle.done()

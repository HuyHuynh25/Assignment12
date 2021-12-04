########################################################################
 ##
 ## CS 101 Lab
 ## Program 12
 ## Name: Huynh Gia Huy-Jim Huynh
 ## Email: hghydv@umsystem.edu
 ##
 ## PROBLEM : Create write a program to use the turtle 
 ## module to draw on the screen a little
 ##      Step 1:  Start
 ##      Step 2:  Import turtle
 ##      Step 3:  Define Superclass calls Point
 ##      Step 4:  Define function __init__(self, x, y, color)
 ##      Step 5:  Define function draw(self)
 ##      Step 6:  Define function draw_action(self)
 ##      Step 7:  Define class calls Box
 ##      Step 8:  Define function __init__(self, x1, y1, width, height, color)
 ##      Step 9:  Define function draw_action(self) for Class Box
 ##      Step 10: Define class calls BoxFilled
 ##      Step 11: Define function __init__(self, x1, y1, width, height, color, fillcolor)
 ##      Step 12: Define function draw_action(self) for Class BoxFilled
 ##      Step 13: Define class calls Circle
 ##      Step 14: Define function __init__(self, x1, y1, radius, color)
 ##      Step 15: Define function draw_action(self) for Class Circle
 ##      Step 16: Define class called CircleFilled
 ##      Step 17: Define function __init__(self, x1, y1, radius, color, fillcolor)
 ##      Step 18: Define function draw_action(self) for CircleFilled
 ##      Step 19: Make an if __name__ == "__main__"
 ##      Step 20: Declare p equals Point(-100, 100, "blue")
 ##      Step 21: Call p.draw
 ##      Step 22: Declare box equals Box(-100, 100, 50, 25, "blue")
 ##      Step 23: Call box.draw
 ##      Step 24: Declare b equals BoxFilled(1, 2, 100, 200, "red", "blue")
 ##      Step 25: Call b.draw
 ##      Step 26: Declare circle equals Circle(-200, 150, 50, 'black')
 ##      Step 27: Call circle.draw
 ##      Step 28: Declare c equals CircleFilled(-200, 150, 50, 'red', 'yellow')
 ##      Step 29: Call c.draw
 ##      Step 30: End
 ##ERROR HANDLING
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import turtle
import time
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.begin_fill()
        turtle.color(self.fillcolor)
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
if __name__ == "__main__":
    p = Point(-100, 100, "blue")
    p.draw()
    box = Box(-100, 100, 50, 25, "blue")
    box.draw()
    b = BoxFilled(1, 2, 100, 200, "red", "blue")
    b.draw()
    circle = Circle(-200, 150, 50, 'black')
    circle.draw()
    c = CircleFilled(-200, 150, 50, 'red', 'yellow')
    c.draw()
    time.sleep(1)

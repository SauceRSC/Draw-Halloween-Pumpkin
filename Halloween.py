# Original code from: https://trinket.io/python/1dfa00f900
# Comments like these help explain the program.

# Make a turtle named 'tina' 
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(2)


# Function to draw triangles of a color, in X and Y coordinates and it can be of 2 sizes
def make_triangle(x, y, color,grande=True):
  tina.penup()
  tina.goto(x,y)
  tina.begin_fill()
  tina.color(color)
  tina.pendown()
  if(grande):
    for count in range(3):
      tina.forward(55)
      tina.left(120)
  else:
    for count in range(3):
      tina.forward(35)
      tina.left(120)
  tina.end_fill()

# Function to draw flipped triangles of a color, in X and Y coordinates and it can be of 2 sizes
def make_triangle_reversed(x, y, color,grande=True):
  tina.penup()
  tina.goto(x,y)
  tina.begin_fill()
  tina.color(color)
  tina.pendown()
  if(grande):
    for count in range(3):
      tina.forward(55)
      tina.right(120)
  else:
    for count in range(3):
      tina.forward(35)
      tina.right(120)
  tina.end_fill()

# Function to draw a square of a color, in X and Y coordinates
def make_square(x, y, color):
  tina.penup()
  tina.goto(x,y)
  tina.begin_fill()
  tina.color(color)
  tina.pendown()
  for count2 in range(3):
    tina.forward(50)
    tina.left(90)
  tina.end_fill()

# To draw the Pumpkin:
tina.penup()
tina.goto(0,-150)
tina.color("#F26513")
tina.begin_fill()
tina.circle(150)
tina.end_fill()
tina.left(180)

# Color to be used
color="#F23A1A"
color1="#F2C849"

# The Teeth:
make_triangle(-35, -30, color)
make_triangle(0, -30, color)
make_triangle(35, -30, color)
make_triangle(70, -30, color)

make_triangle(-45, -35, color1,False)
make_triangle(-10, -35, color1,False)
make_triangle(25, -35, color1,False)
make_triangle(60, -35, color1,False)
tina.left(180)


# The Nose:
make_triangle_reversed(-35, 25, color)
make_triangle_reversed(-25, 20, color1,False)

# The Eyes:
make_triangle(-70, 50, color)
make_triangle(0, 50, color)

make_triangle(-60, 50, color1,False)
make_triangle(10, 50, color1,False)

# The Stump:
make_square(-20, 125, '#99A637')

# Write Happy Halloween! ❤
tina.color("#FF0000")
palabra = 'Happy Halloween! ' + "\u2764"

tina.penup()
tina.goto(0,-200)
tina.write(palabra,font=("Arial",24,"normal"),align="center")

# Move Turtle and change it to green
tina.color('#99A637')
tina.goto(0,-230)
tina.left(180)

x=input()

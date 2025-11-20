import turtle
pen=turtle.Turtle()
pen.shape("turtle")
pen.color("lime")

penother=turtle.Turtle()
penother.color("dark blue")
penother.penup()
penother.goto(-150,350)
penother.pendown()
penother.write("hello welcome to microsoft paint this is the real one i promise\ngood old Wolfeschlegelsteinhausenbergerdorff the turtle will be hosting our annotating thingamabob",font=("comic sans",20,"bold"),align="center")
penother.hideturtle()

steps=int(input("enter the number of steps you want Wolfeschlegelsteinhausenbergerdorff to move"))

def go_forward():
    pen.forward(steps)

def go_up():
    pen.setheading(90)

def go_down():
    pen.setheading(270)

def go_right():
    pen.setheading(0)

def go_left():
    pen.setheading(180)

#key events

screen=turtle.Screen()
screen.listen()
screen.onkey(go_up,"w") 
screen.onkey(go_right,"d")
screen.onkey(go_down,"s")
screen.onkey(go_left,"a")   
screen.onkey(go_forward,"space")

#mouse events

def click(x,y):
    screen.tracer(0)
    pen.setheading(pen.towards(x,y))
    pen.goto(x,y)
    screen.tracer(1)

def drag(x,y):
    screen.tracer(0)
    pen.goto(x,y)
    screen.tracer (1)

screen.onclick(click)
pen.ondrag(drag)
turtle.done()
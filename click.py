import turtle
import random
# pen = turtle.Turtle()

# paper = turtle.Screen()

# r=random.randint(0,255)
# g=random.randint(0,255)
# b=random.randint(0,255)

# c = ["red","yellow","green","blue","pink"]
# clr = random .choice(c)

# def hi (x,y):
#   paper.bgcolor(clr)

# paper.onclick(hi)
# turtle.done()

import turtle
import random
colours_list=['red','blue','black','yellow','green','orchid1','firebrick1']
screen=turtle.Screen()
def colours(x,y):
  c=random.choice(colours_list)
  screen.bgcolor(c)
screen.onclick(colours)
turtle.done()
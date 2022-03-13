import turtle
wn = turtle.Screen()
laki= turtle.Turtle()
#laki is our turtle's name
laki.shapesize(2)
laki.color("red")

#with use def
def oval(x):
    for i in range (2):
        laki.circle(x,90)
        laki.circle(x//10,90)

oval(200)  #size of oval

wn.mainloop()



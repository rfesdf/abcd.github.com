import turtle
t=turtle.Turtle()
list1= ["purple","red","orange","blue","green"]
for i in range(400):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)

from turtle import *
speed(10000000000000000000000000000000000000000000000)
width(3)
bgcolor("skyblue")
# drawing square
color("purple")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()
penup()
left(90)
forward(200)
pendown()
#end of square

# drawing a roof
color("black")
begin_fill()
right(40)
forward(155)
right(100)
forward(155)
right(130)
forward(200)
end_fill()
#end of roof

#shape of square
for i in range(4):
    left(90)
    forward(200)

left(90)
forward(200)
left(90)
forward(70)
left(90)
#end of shape

#drawing door
color("red")
begin_fill()
for i in range(4):
    forward(100)
    right(90)
    forward(60)  
    right(90)
end_fill()
color("black")
left(90)
backward(60)
right(90)
for i in range(4):
    forward(100)
    left(90)
    forward(60)
    left(90)
#end of door

# drawing window
penup()
color("yellow")
right(90)
forward(60)
left(90)
forward(175)
left(90)
pendown()
begin_fill()
for i in range(4):
    forward(45)
    left(90)
end_fill()

left(90)
forward(22.5)
color("black")
width(7)
right(90)
forward(45)
backward(22.5)
left(90)
forward(22.5)
backward(45)
width(3)


# second window
right(90)
penup()
forward(167.5)
pendown()
penup()
backward(55)
pendown()
color("yellow")
begin_fill()
for i in range(4):
    forward(45)
    left(90)
end_fill()

left(90)
forward(22.5)
color("black")
width(7)
right(90)
forward(45)
backward(22.5)
left(90)
forward(22.5)
backward(45)


exitonclick()



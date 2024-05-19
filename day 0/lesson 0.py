from turtle import*


#we want to paint a house


#step 1:  draw a square
speed(10)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drowin a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10,50)
pendown()

color("turquoise")
begin_fill()
right(150)
forward(90) #window's higth
right(90)
forward(40)  #windows width
right(90)
forward(90)
right(90)
forward(40)
end_fill()

penup()
goto(150,50)
pendown()

begin_fill()
right(90)
forward(90)
right(90)
forward(40)
right(90)
forward(90)
right(90)
forward(40)
end_fill()


exitonclick()
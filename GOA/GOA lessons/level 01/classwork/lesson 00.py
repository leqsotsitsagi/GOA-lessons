from turtle import *
speed(30)
# დავხაზოთ კვადრატი
width(4)
color("brown")
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

#დავხაზოთ კარები

forward(70)
begin_fill()
color("gray")
left(90)

forward(100)
right(90)

forward(60)
right(90)

forward(100)
end_fill()

penup() # კალმის აღება
goto(200, 200)
pendown() # კალმის დადება

color("brown")
begin_fill() #შიგნით გაფერადება
right(150)
forward(200)

left(120)
forward(200)
end_fill() # გაფერადება დასრულებულია

color("black")

left(120)
forward(200)

# დამკეტი ფრჩხილი
exitonclick()
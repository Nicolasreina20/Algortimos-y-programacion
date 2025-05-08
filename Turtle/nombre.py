import turtle 

t = turtle.Turtle()  

t.speed(8)

turtle.bgcolor("black")  
turtle.pensize(2)  

#N
t.shape("turtle")
t.color("white")
t.pensize(35)
t.penup()
t.goto(-450,-90)
t.pendown()
t.lt(90)
t.fd(140)
t.rt(145)
t.fd(170)
t.lt(145)
t.fd(140)

#I
t.color("white")
t.penup()
t.goto(-300,50)
t.pendown()
t.lt(180)
t.fd(140)

#C
t.color("white")
t.penup()
t.goto(-130,30)
t.pendown()
t.rt(130)
t.circle(70, 270)

#O
t.color("white")
t.penup()
t.goto(50,-70)
t.pendown()
t.circle(70)

#L
t.color("white")
t.penup()
t.goto(110,50)
t.pendown()
t.lt(220)
t.fd(140)
t.lt(90)
t.fd(90)

#A
t.color("white")
t.penup()
t.goto(240,-90)
t.pendown()
t.rt(-65)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

#S
t.color("white")
t.penup()
t.goto(470,50)
t.pendown()
t.rt(30)
t.circle(40, 230)
t.pendown()
t.rt(30)
t.circle(-40, 230)


turtle.done()

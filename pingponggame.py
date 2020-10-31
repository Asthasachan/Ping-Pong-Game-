import turtle
import winsound
wn= turtle.Screen()
wn.title("PING PONG!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop from updating

#score
score_a=0
score_b=0
#pad a
pad_a = turtle.Turtle()
pad_a.speed(0) #animation speed
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

#pad b
pad_b = turtle.Turtle()
pad_b.speed(0) #animation speed
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0) #animation speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.2
ball.dy= -0.2

#penboard
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 :: Player B: 0" , align="center", font=("Courier", 24,"normal"))

def pad_a_up():
	y=pad_a.ycor()
	y=y+20
	pad_a.sety(y)

def pad_a_down():
	y=pad_a.ycor()
	y=y-20
	pad_a.sety(y)	

def pad_b_up():
	y=pad_b.ycor()
	y=y+20
	pad_b.sety(y)

def pad_b_down():
	y=pad_b.ycor()
	y=y-20
	pad_b.sety(y)		

#keyboard winding
wn.listen()
wn.onkeypress(pad_a_up,"w")	
wn.onkeypress(pad_a_down,"s")	
wn.onkeypress(pad_b_up,"Up")	
wn.onkeypress(pad_b_down,"Down")	

while True:
	wn.update()

	#move ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	#border
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy*=-1	
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A: {} :: Player B: {}".format(score_a,score_b) , align="center", font=("Courier", 24,"normal"))

	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx*=-1	
		score_b+=1
		pen.clear()
		pen.write("Player A: {} :: Player B: {}".format(score_a,score_b) , align="center", font=("Courier", 24,"normal"))

	if pad_b.ycor()>280:
		pad_b.sety(280)

	if pad_b.ycor()<-280:
		pad_b.sety(-280)

	if pad_a.ycor()>280:
		pad_a.sety(280)

	if pad_a.ycor()<-280:
		pad_a.sety(-280)	
			
	

	#PAD and ball colli
	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<pad_b.ycor()+50 and ball.ycor()>pad_b.ycor()-50):
		ball.setx(340)
		ball.dx*=-1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<pad_a.ycor()+50 and ball.ycor()>pad_a.ycor()-50):
		ball.setx(-340)
		ball.dx*=-1	
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


		


	
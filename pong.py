import turtle

wn = turtle.Screen()
wn.title("Pong by Divyansh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("green")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

# paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("green")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2


# Functions
def paddleAup():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddleAdown():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddleBup():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddleBdown():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddleAup, "w")
wn.onkeypress(paddleAdown, "s")
wn.onkeypress(paddleBup, "Up")
wn.onkeypress(paddleBdown, "Down")


# main logic
while True:
    wn.update()

    # moving the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # border checking
    # UP
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # DOWN
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # LEFT
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # RIGHT
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1


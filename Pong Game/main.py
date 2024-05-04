import turtle

window = turtle.Screen()
window.setup(width=700, height=600)
window.tracer(0)
window.bgcolor("black")
window.title("Ping Pong")
run = True

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.goto(-300, 0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.speed(0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.goto(300, 0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.speed(0)

# Ball

ball = turtle.Turtle()
ball.goto(0, 0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.speed(0)
ball.dx = 0.4
ball.dy = 0.4

player1_score = 0
player2_score = 0
score1 = turtle.Turtle()
score1.goto(0, 240)
score1.speed(0)
score1.hideturtle()
score1.color("white")
score1.write("Player A : {}      Player B : {}".format(player1_score, player2_score), align="center", font=("agency fb", 20, "normal"))

# Functions
def paddle1_up():
    y = paddle1.ycor()
    if y == 250:
        pass
    else:
        y += 50
        paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    if y == 250:
        pass
    else:
        y += 50
        paddle2.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    if y == -250:
        pass
    else:
        y -= 50
        paddle1.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    if y == -250:
        pass
    else:
        y -= 50
        paddle2.sety(y)


# Game Loop
window.listen()
window.onkey(paddle1_up, "w")
window.onkey(paddle1_down, "s")
window.onkey(paddle2_up, "Up")
window.onkey(paddle2_down, "Down")
while run:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() > 340:
        player1_score += 1
        score1.clear()
        score1.write("Player A : {}      Player B : {}".format(player1_score, player2_score), align="center", font=("agency fb", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() < -340:
        score1.clear()
        player2_score += 1
        score1.write("Player A : {}      Player B : {}".format(player1_score, player2_score), align="center", font=("agency fb", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() > 300 and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.dx *= -1
        ball.dy *= 1
    if ball.xcor() < -300 and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.dx *= -1
        ball.dy *= 1
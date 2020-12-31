from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()


# TODO 1. Set Screen size
# TODO 2. Scoreboard
# TODO 3. Player 1 and player 2 reusable
# TODO 4. Ball
# TODO 5. Midlle line
# TODO 6. Bouncing side walls
# TODO 7. When is game over.
# TODO 8. When point is gain



# Create screen
# Create moving paddle
# Create another paddle.
# Create a ball and make it move
# Detect collision and make it bounce back
# Detect colition with a paddle
# Detect when paddle misses a ball
# Keep score


screen.exitonclick()
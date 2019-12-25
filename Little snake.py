import time
import turtle
from random import randrange

BREAK_FLAG = False

# game window
screen = turtle.Screen()
screen.title('Little snake')
screen.bgcolor('white')
screen.setup(450, 450)
screen.tracer(8,25)

# boorders creating
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-211, 211)
border.pendown()
border.goto(211, 211)
border.goto(211, -211)
border.goto(-211, -211)
border.goto(-211, 211)

# snake creating
snake = []
for i in range(2):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('#7a995d')
    else:
        snake_segment.color('#475936')
    snake.append(snake_segment)

# food creating
food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.penup()
food.goto(randrange(-200, 200, 20), randrange(-200, 200, 20))

# keypress
screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.listen()

while True:

    # making a snake longer
    # recreating a food again
    if snake[0].distance(food) < 10:
        food.goto(randrange(-200, 200, 20), randrange(-200, 200, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('#7a995d')
        snake_segment.penup()
        snake.append(snake_segment)

    # snake tail moving
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    # snake head moving
    snake[0].forward(20)
    screen.update()

    # crush with borders
    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    if x_cor > 200 or x_cor < -200:
        screen.bgcolor('#323332')
        break
    if y_cor > 200 or y_cor < -200:
        screen.bgcolor('#323332')
        break

    # crush with itself
    for i in snake[1:]:
        i = i.position()
        if snake[0].distance(i) < 10:
            BREAK_FLAG = True
    if BREAK_FLAG:
        screen.bgcolor('#323332')
        break
    time.sleep(0.3)

screen.mainloop()
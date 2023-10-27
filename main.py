from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_starts = True
while is_game_starts:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detuct collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    #detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        score.reset()
        snake.reset()
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()






screen.exitonclick()

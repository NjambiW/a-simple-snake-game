import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect a collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.new_score()
    # detect a collision with the walls
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scores.reset()
        snake.reset()
    # detects a collision with its own body.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scores.reset()
            snake.reset()


screen.exitonclick()

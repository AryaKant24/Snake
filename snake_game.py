from turtle import Turtle,Screen
from snake import Snake
import random
import time
from food import Food
from scoreboard import Scoreboard
import pygame

# initialize pygame mixer
pygame.mixer.init()

# load and play background music (loop forever)
pygame.mixer.music.load("suit.mp3")  # supports wav, mp3, ogg
pygame.mixer.music.play(-1)         # -1 = loop indefinitely

food = Food()
screen = Screen()
score_board = Scoreboard()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect colission with food
    if snake.head.distance(food) < 18:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on = False
        pygame.mixer.music.stop()
        score_board.game_over()

    #Detect collision with tail
    for part in snake.snake[1:]:
        if snake.head.distance(part)<10:
            game_on = False
            pygame.mixer.music.stop()
            score_board.game_over()
        
screen.exitonclick()
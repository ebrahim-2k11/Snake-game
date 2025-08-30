from turtle import Turtle, Screen
from snake import Snake
from food import Food,Score
import time

# Initializing 
windo=Screen()
windo.bgcolor("black")
windo.setup(800,800)
windo.tracer(0)
snake=Snake()
food= Food()
score=Score()
game_on=True
food.random_place()
#Game on

while game_on:

    windo.update()
    snake.move()
    score.display_score()
    windo.update()
#   Move

    windo.listen()
    windo.onkey(snake.up,"Up")
    windo.onkey(snake.down,"Down")
    windo.onkey(snake.left,"Left")
    windo.onkey(snake.right,"Right")

#   if eat food   

    if snake.head.distance(food)<18:
    
        snake.add_segment()
        food.random_place()
        score.add_score()

#   if quit the resolution

    if snake.head.xcor() >370 or snake.head.xcor() < -370 or snake.head.ycor() < -370 or snake.head.ycor() >370:
        windo.bgcolor("darkred")
        game_on=False
        score.game_over()

#   if eat my self
    
    for segment in snake.snake[0:len(snake.snake)-2]:
        
        if snake.head.distance(segment)<10 :
            windo.bgcolor("darkred")
            score.game_over()
            game_on=False
    
    time.sleep(0.1) 



windo.exitonclick()    
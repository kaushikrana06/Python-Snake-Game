import time
from turtle import Screen , Turtle
import random
from snake import Snake
from food import Food
from score import Score

s = Screen()

s.setup(width=600 , height=600)
s.bgcolor("black")
s.title("Snake Game")


sn = Snake()
f = Food()
sc = Score()


s.listen()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.left ,"Left")
s.onkey(sn.right,"Right")

on = True
while on:
    s.update()
    time.sleep(0.05)
    sn.move()

    if sn.h.distance(f)<15:
        f.refresh()
        sn.ext()
        sc.sc()

    if sn.h.xcor() > 280 or sn.h.xcor() < -280 or sn.h.ycor() > 280 or sn.h.ycor() < -280:

        sc.re()
    for seg in sn.k[1:]:
        if sn.h.distance(seg) < 10:
             sc.re()
             sn.re()


s.exitonclick()
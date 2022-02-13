
from turtle import Turtle
st=[(0,0),(-20,0),(-40,0)]
d= 20
u1 = 90
u2 = 270
u3 = 180
u4 = 0
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.k = []
        self.sn()
        self.h = self.k[0]

    def sn(self):
        for x in st:
            self.seg(x)


    def seg(self, x):

        t3 = Turtle(shape="square")
        t3.color("white")
        t3.penup()
        t3.goto(x)
        self.k.append(t3)


    def re(self):
        for seg in self.k:
            seg.goto(1000 , 1000)

        self.k.clear()
        self.seg()
        self.h = self.k[0]

    def ext(self):
        self.seg(self.k[-1].position())


    def move(self):
        for x in range(len(self.k) - 1, 0, -1):
            ax = self.k[x - 1].xcor()
            ay = self.k[x - 1].ycor()
            self.k[x].goto(ax, ay)
        self.h.forward(d)
    def up(self):
       if self.h.heading() != u2 :
          self.h.setheading(u1)
    def down(self):
       if self.h.heading() != u1:
        self.h.setheading(u2)

    def left(self):
       if self.h.heading() != u4:
         self.h.setheading(u3)

    def right(self):
       if self.h.heading() != u3:
          self.h.setheading(u4)


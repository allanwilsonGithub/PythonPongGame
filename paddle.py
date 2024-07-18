from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_coords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(start_coords)
        self.clear()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        self.clear()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        self.clear()

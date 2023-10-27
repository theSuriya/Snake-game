from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
       for seg in self.segment:
           seg.goto(1000, 1000)
       self.segment.clear()
       self.create_snake()
       self.head = self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[seg_num - 1].xcor()
            y_cor = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





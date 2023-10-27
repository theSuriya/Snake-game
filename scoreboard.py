from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("arial", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.higher_score = int(f.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.create_score()

    def create_score(self):
        self.clear()
        self.write(f"score: {self.score}   high score: {self.higher_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.higher_score:
            self.higher_score = self.score
            with open("data.txt", mode="w") as k:
                k.write(f"{self.higher_score}")
        self.score = 0
        self.create_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.create_score()






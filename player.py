from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["grey","green", "blue", "purple", "pink", "red", "yellow", "golden"]

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.color(COLORS[self.level % len(COLORS)])   # Change color based on level (cycles through colors)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1
            return True
        else:
            return False

    def level_up(self):
        self.level += 1
        self.go_to_start()
        current_size = self.shapesize()[0] # Make turtle slightly bigger each level
        if current_size < 2:  # Limit max size
            self.shapesize(current_size + 0.1, current_size + 0.1)


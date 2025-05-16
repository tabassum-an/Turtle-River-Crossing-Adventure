from turtle import Turtle
import random

COLORS = ["red", "grey", "black", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class LogManager:
    def __init__(self):
        self.all_logs = []
        self.log_speed = STARTING_MOVE_DISTANCE

    def create_log(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_log = Turtle("square")
            new_log.shapesize(stretch_wid=1, stretch_len=2)
            new_log.penup()
            new_log.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_log.goto(300, random_y)
            self.all_logs.append(new_log)

    def move_logs(self):
        for log in self.all_logs:
            log.backward(self.log_speed)

    def level_up(self):
        self.log_speed += MOVE_INCREMENT

    def reset(self):
        for log in self.all_logs:
            log.hideturtle()
        self.all_logs.clear()
        self.log_speed = STARTING_MOVE_DISTANCE
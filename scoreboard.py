from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        self.pause_writer = Turtle()
        self.pause_writer.hideturtle()
        self.pause_writer.penup()
        self.pause_writer.color("grey")

    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Flash red background
        screen = self.getscreen()
        original_bg = screen.bgcolor()

        for _ in range(3):
            screen.bgcolor("red")
            screen.update()
            time.sleep(0.1)
            screen.bgcolor(original_bg)
            screen.update()
            time.sleep(0.1)

        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))
        self.goto(0, -40)
        self.color("blue")
        self.write("Press R to Restart", align="center", font=("Courier", 16, "bold"))

    def show_pause(self):
        self.clear()
        self.pause_writer.goto(0, 0)
        self.pause_writer.write(f"PAUSED\nLevel: {self.level}", align="center", font=FONT)

    def hide_pause(self):
        self.pause_writer.clear()

    def reset(self):
        self.level = 1
        self.update_scoreboard()
import time
from turtle import Screen, Turtle
from player import Player
from tree_log_manager import LogManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgcolor("#B0DB9C")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Instruction setup
instruction_writer = Turtle()
instruction_writer.hideturtle()
instruction_writer.penup()
instruction_writer.color("black")
instruction_writer.goto(0, 100)

instruction_writer.write("Use Arrow Keys to Move\n"
                         "Press SPACE to Pause\n"
                         "Reach the Top to Level Up\n"
                         "Avoid Logs in the River!\n\n"
                         "Press ENTER to Start",
                         align="center",
                         font=("Courier", 16, "normal"))

# Initialize game components
player = Player()
log_manager = LogManager()
scoreboard = Scoreboard()

# Game state variables
game_is_on = True
paused = False
game_started = False

# Movement wrapper functions
def move_up():
    if game_started:
        player.go_up()

def move_down():
    if game_started:
        player.go_down()

def move_left():
    if game_started:
        player.go_left()

def move_right():
    if game_started:
        player.go_right()

# Toggle pause function
def toggle_pause():
    global paused
    if game_started:
        paused = not paused
        if paused:
            scoreboard.show_pause()
        else:
            scoreboard.hide_pause()
            scoreboard.update_scoreboard()

# Reset function
def reset_game():
    if game_started:
        player.go_to_start()
        log_manager.reset()
        scoreboard.reset()
        play_game()

# Game loop
def play_game():
    global game_is_on
    game_is_on = True
    player.go_to_start()
    log_manager.reset()
    scoreboard.reset()

    while game_is_on:
        if not paused:
            time.sleep(0.1)
            screen.update()

            log_manager.create_log()
            log_manager.move_logs()

            # LOG COLLISION FUNCTIONALITY
            for log in log_manager.all_logs:
                if log.distance(player) < 20:
                    game_is_on = False
                    scoreboard.game_over()
                    return # Return to allow reset via key press

            # SUCCESSFUL CROSSING FUNCTIONALITY
            if player.is_at_finish_line():
                player.go_to_start()
                log_manager.level_up()
                scoreboard.increase_level()
        else:
            screen.update()
            time.sleep(0.1)

# Start game when ENTER is pressed
def start_game():
    global game_started
    instruction_writer.clear()
    game_started = True
    play_game()

# Controls setup
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(toggle_pause, "space")
screen.onkey(reset_game, "r")
screen.onkey(start_game, "Return")

screen.mainloop()

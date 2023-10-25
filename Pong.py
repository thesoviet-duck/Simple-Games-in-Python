# Welcome To The Code For Pong
# By Me and a lil help from Chat GTP

# Imports
import os
import turtle
import random
import subprocess


# Provide the path to the audio file you want to play
bounce_sound = "bounce sound.wav"
score_sound = "score sound.mp3"
win_sound = "win sound.mp3"

# Basic Stuff
wn = turtle.Screen()
wn.title("Pong by Me")
wn.bgcolor("white")
wn.setup(width=1280, height=800)
wn.tracer(0)
print("What do you think your doing looking in here?")

# variables
color_list = ["yellow", "green", "orange", "blue", "red", "purple", "cyan", "white"]
paddle_speed = 0
text_pos_1 = -500
text_pos_2 = 500
text_pos_3 = 330

# Score
score_a = 0
score_b = 0

# Adding appropriate speed according to the screen size

# get screen width
screen_width = int(wn.textinput("What is your screen width", "Please enter your screen size (inches)"))

# speed variables
paddle_speed_1 = 0
paddle_speed_2 = 0
paddle_speed_3 = 0
ball_speed_1 = 0
ball_speed_2 = 0
ball_speed_3 = 0

# Setting speed
if screen_width <= 21:
    paddle_speed_1 = 25
    paddle_speed_2 = 35
    paddle_speed_3 = 45
    ball_speed_1 = 2.5
    ball_speed_2 = 3.5
    ball_speed_3 = 4.5

elif screen_width <= 24:
    paddle_speed_1 = 35
    paddle_speed_2 = 45
    paddle_speed_3 = 55
    ball_speed_1 = 3.5
    ball_speed_2 = 4.5
    ball_speed_3 = 5.5

elif screen_width >= 27:
    paddle_speed_1 = 45
    paddle_speed_2 = 55
    paddle_speed_3 = 65
    ball_speed_1 = 4.5
    ball_speed_2 = 5.5
    ball_speed_3 = 6.5

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-550, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_b.penup()
paddle_b.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen for displaying the score and time
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 345)
pen.write(f"Time: 00:00", align="center", font=("Arial", 30, "bold"))
pen.goto(text_pos_1, text_pos_3)
pen.write(f"Player A: 0", align="left", font=("Arial", 34, "bold"))
pen.goto(text_pos_2, text_pos_3)
pen.write(f"Player B: 0", align="right", font=("Arial", 34, "bold"))

# Initialize the time variables
minutes = 0
seconds = 0

# Function to update the score and time
def update_score_time():
    global minutes, seconds

    # Update the time
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0

    # Clear the previous text and write the updated score and time
    pen.clear()
    pen.goto(0, 345)
    pen.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Arial", 30, "bold"))
    pen.goto(text_pos_1, text_pos_3)
    pen.write(f"Player A: {score_a}", align="left", font=("Arial", 34, "bold"))
    pen.goto(text_pos_2, text_pos_3)
    pen.write(f"Player B: {score_b}", align="right", font=("Arial", 34, "bold"))
    # Update the score and time again after 1000ms (1 second)
    turtle.ontimer(update_score_time, 1000)


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 299.5:
        y += paddle_speed
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -299.5:
        y -= paddle_speed
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 299.5:
        y += paddle_speed
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -299.5:
        y -= paddle_speed
    paddle_b.sety(y)


def change_ball_color():
    ball.color(random.choice(color_list))


def play_audio_file(file_path):
    command = f'afplay "{file_path}"'
    subprocess.Popen(command, shell=True)


def play_bounce():
    play_audio_file(bounce_sound)


def play_score():
    play_audio_file(score_sound)


def play_win():
    play_audio_file(win_sound)


def exit_the_game():
    os._exit(os.EX_OK)


def flash_score(player):
    original_color = pen.color()
    if player == "A":
        pen.color("red")
        wn.ontimer(lambda: pen.color(original_color[0]), 400)  # Flash for 500 milliseconds
    elif player == "B":
        pen.color("red")
        wn.ontimer(lambda: pen.color(original_color[0]), 400)  # Flash for 500 milliseconds


# Personalizing the game for the user

# Difficulty
difficulty = turtle.textinput("Select Difficulty\n", "1 for easy,  2 for medium, 3 for hard." "\nif your paddle stops moving just click your button again")
if difficulty == "1":
    ball.dx = ball_speed_1
    ball.dy = -ball_speed_1
    paddle_speed = paddle_speed_1

elif difficulty == "2":
    ball.dx = ball_speed_2
    ball.dy = -ball_speed_2
    paddle_speed = paddle_speed_2

elif difficulty == "3":
    ball.dx = ball_speed_3
    ball.dy = -ball_speed_3
    paddle_speed = paddle_speed_3

else:
    ball.dx = ball_speed_2
    ball.dy = -ball_speed_2
    paddle_speed = paddle_speed_2

# Color Theme
color = turtle.textinput("Select your Color Pattern\n", "1 for default, 2 for Red White, 3 for Blue White")


def set_color(paddle_a_color, paddle_b_color, ball_color, bg_color, textcolor="white"):
    pen.color(textcolor)
    paddle_a.color(paddle_a_color)
    paddle_b.color(paddle_b_color)
    ball.color(ball_color)
    wn.bgcolor(bg_color)

if color == "1":
    set_color("#d6d4d4", "#d6d4d4", "#d6d4d4", "#131313")
    
elif color == "2":
    set_color("#f5f0f0", "#f5f0f0", "#f5f0f0", "#e33232")

elif color == "3":
    set_color("white", "white", "white", "#5413d6")

else:
    set_color("black", "black", "black", "white", "black")

# Keyboard binding
wn.listen()

wn.onkeypress(exit_the_game, "F1")

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "S")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Activate the timer
update_score_time()

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
        change_ball_color()
        play_bounce()

    elif ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
        change_ball_color()
        play_bounce()

    # Give a point to Player A
    elif ball.xcor() > 630:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        flash_score("A")
        pen.clear()
        pen.goto(0, 345)
        pen.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Arial", 30, "bold"))
        pen.goto(text_pos_1, text_pos_3)
        pen.write(f"Player A: {score_a}", align="left", font=("Arial", 34, "bold"))
        pen.goto(text_pos_2, text_pos_3)
        pen.write(f"Player B: {score_b}", align="right", font=("Arial", 34, "bold"))
        change_ball_color()
        play_score()

    # Give a point to Player B
    elif ball.xcor() < -630:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        flash_score("B")
        pen.clear()
        pen.goto(0, 345)
        pen.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Arial", 30, "bold"))
        pen.goto(text_pos_1, text_pos_3)
        pen.write(f"Player A: {score_a}", align="left", font=("Arial", 34, "bold"))
        pen.goto(text_pos_2, text_pos_3)
        pen.write(f"Player B: {score_b}", align="right", font=("Arial", 34, "bold"))
        change_ball_color()
        play_score()

    # Paddle and ball collisions
    elif ball.xcor() > 544 and ball.xcor() > 544 and (
            ball.ycor() < paddle_b.ycor() + 57 and ball.ycor() > paddle_b.ycor() - 57):
        play_bounce()
        ball.setx(545)
        ball.dx *= -1
        change_ball_color()

    elif ball.xcor() < -544 and ball.xcor() < -544 and (
            ball.ycor() < paddle_a.ycor() + 57 and ball.ycor() > paddle_a.ycor() - 57):
        play_bounce()
        ball.setx(-545)
        ball.dx *= -1
        change_ball_color()
    # Exit the loop if either player reaches 10 points
    if score_a == 10:
        play_win()
        prompt_1 = turtle.textinput("Yay! Player A won the match!",
                                    "Type 1 to quit or type 2 restart, typing anything else will quit the game.")
        if prompt_1 == "1":
            break
        elif prompt_1 == "2":
            os.system('python3 Pong Test Version.py')
        else:
            break

    if score_b == 10:
        play_win()
        prompt_2 = turtle.textinput("Yay! Player B won the match!",
                                    "Type 1 to quit or type 2 restart, typing anything else will quit the game.")
        if prompt_2 == "1":
            break
        elif prompt_2 == "2":
            os.system('python3 Pong Test Version.py')
        else:
            break

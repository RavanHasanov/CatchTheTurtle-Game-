import random
import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("CatchTheTurtle")
game_over = False
score = 0
grid_size = 10
FONT = ('Arial', 30, 'normal')

# turtle list
turtle_list = []

# countdown turtle
count_down_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()

# win score
winScore = 3


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2  # positive height/2 is the top of the screen
    y = top_height - top_height * 0.2  # decreasing a bit so text will be visible
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [15, 5, -5, -15]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 1000)


def countdown(time):
    global game_over
    global score
    global winScore
    top_height = screen.window_height() / 2
    y = top_height - top_height * 0.2
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 35)
    count_down_turtle.clear()

    if time > 0 and winScore >= score:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)

        if winScore <= score:
            game_over = True
            count_down_turtle.clear()
            hide_turtles()
            count_down_turtle.goto(0, 0)
            count_down_turtle.write(f"You Win!, Score:{score}", align='center', font=FONT)

    else:
        game_over = True
        difference = winScore - score
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.goto(0, 0)
        count_down_turtle.write(f"Game Over!, Score:{score}, next time increase {difference}", align='center', font=FONT)


def start_game_up():
    global game_over
    game_over = False

    turtle.tracer(0)

    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()

    turtle.tracer(1)

    screen.ontimer(lambda: countdown(5), 10)


start_game_up()
turtle.mainloop()
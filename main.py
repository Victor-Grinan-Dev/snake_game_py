import turtle
import time
import random

score = 0
high_score = 0
delay = 0.15
width, height = 620, 630

win = turtle.Screen()
win.setup(width, height)
win.title("Snake")
win.bgcolor("black")
win.tracer(0)

# screen border
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.setposition(width / 2 - 20, height / 2 - 40)
pen.pendown()
for _ in range(4):
    pen.right(90)
    pen.fd(width - 40)

# score
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(0, height / 2 - 30)
score_pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 18, "normal"))

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0, 0)
head.direction = "right"

# segments
segments = []


# food = turtle.Turtle()
# food.speed(0)
# food.shape("circle")
# food.color("red")
# food.penup()
# foodx = random.randint(-250, 250)
# foody = random.randint(-250, 250)
# food.goto(foodx, foody)


# function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def is_collision(other):
    a = head.xcor() - other.xcor()
    b = head.ycor() - other.ycor()
    distance = ((a ** 2) + (b ** 2)) ** 0.5

    if distance < 20:
        return True
    else:
        return False


def spawn_food():
    food_ = turtle.Turtle()
    food_.speed(0)
    food_.shape("circle")
    food_.color("red")
    food_.penup()
    foodx_ = random.randint(-250, 250)
    foody_ = random.randint(-250, 250)
    food_.goto(foodx_, foody_)
    return food_


def reset_game():
    global score, delay
    delay = 0.15
    score = 0
    score_pen.clear()
    score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    for segment_ in segments:
        segment_.setposition(2000, 2000)
        segments.clear()
    head.goto(0, 0)
    head.direction = "stop"


win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

food = spawn_food()

while True:
    time.sleep(delay)

    # check the borders
    if head.xcor() > 270 or head.xcor() < -270 or head.ycor() > 270 or head.ycor() < - 270:
        reset_game()

    # movement
    # move segments in reverse order
    for index in range(len(segments) - 1, 0, - 1):
        segment_x = segments[index - 1].xcor()
        segment_y = segments[index - 1].ycor()
        segments[index].goto(segment_x, segment_y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if is_collision(segment):
            reset_game()

    # move the food randomly
    if is_collision(food):
        print("yeah")

        # create segment
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segments.append(segment)

        # handle food
        foodx = random.randint(-250, 250)
        foody = random.randint(-250, 250)
        food.goto(foodx, foody)

        # increase score
        score += 10
        if score > high_score:
            high_score = score

        score_pen.clear()
        score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))
        delay -= 0.01
    win.update()

# win.mainloop()

import turtle
import random

# set up the screen
window = turtle.Screen() # creates a window
window.title("Likun's Snake Game") # give title to the window
window.bgcolor("black") # set the background color
window.setup(width=600, height=600) # sets the window dimensions
window.tracer(0) # turns off the screen updates

# create snake's head
head = turtle.Turtle() # create a turtle (python notation)
head.speed(0) # we don't want the head to move
head.shape("square") # set the head shape
head.color("white") # set the head color
head.penup() # we don't want the path to be drawn
head.goto(0, 100) # position of the snake's head
head.direction = "stop"

# functions to move the snake
def move():
    if head.direction == "up":
        y = head.ycor() # y coordinate of the turtle
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor() # y coordinate of the turtle
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor() # x coordinate of the turtle
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor() # x coordinate of the turtle
        head.setx(x-20)

import time # to represent time in code
delay = 0.1

def move_up():
    # the snake cannot go up from down and vica-versa
    if head.direction != "down":
        head.direction = "up"

def move_down():
    # the snake cannot go down from up and vica-versa
    if head.direction != "up":
        head.direction = "down"

def move_right():
    # the snake cannot go right from left and vica-versa
    if head.direction != "left":
        head.direction = "right"

def move_left():
    # the snake cannot go left from right and vica-versa
    if head.direction != "right":
        head.direction = "left"

# keyboard bindings
window.listen() # the program now listens to key press
# assigning keys to function calls
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_right, "Right")
window.onkey(move_left, "Left")

# food for our snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50) # stretch value in width and length
food.goto(0, 0)

# initialize an empty list for snake's body
segs = []

# scores
c_score = 0
high_score = 0

# scoring system
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))



# main game loop
while True:
    window.update()

    time.sleep(delay)
    # sleep function in time module adds delay to the code
    # halts the excecution of the program for the given no of secs

    # when snake eats the food
    if head.distance(food) < 15.75:
        # relocate the food to a random position
        # randomization
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y) # relocate coordinates

        # add a segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        # elongation of snake's body
        segs.append(new_seg)

        # as the snake eats food, it's speed increases
        delay -= 0.001

        # update current score
        c_score = c_score+10

        if c_score > high_score:
            high_score = c_score

        # update score tab
        score.clear()
        score.write("Score: {} High Score: {}".format(c_score, high_score), align="center", font=("Courier", 20, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segs)-1, 0, -1):
        x = segs[index-1].xcor()
        y = segs[index-1].ycor()
        segs[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segs) > 0:
        x = head.xcor()
        y = head.ycor()
        segs[0].goto(x, y)

    # case handling for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # relocate the segments outside the window coordinates
        for s in segs:
            s.goto(1000, 1000)

        # clear the segs list
        segs.clear()

        # reset current score
        c_score = 0

        # reset delay
        delay = 0.1

        # update score tab
        score.clear()
        score.write("Score: {} High Score: {}".format(c_score, high_score), align="center", font=("Courier", 20, "normal"))

    move()

    # when snake bites itself
    for segment in segs:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for segment in segs:
                segment.goto(1000, 1000)

            # clear the segments list
            segs.clear()

            # reset current score
            c_score = 0

            # reset delay
            delay = 0.1

            # update score tab
            score.clear()
            score.write("Score: {} High Score: {}".format(c_score, high_score), align="center", font=("Courier", 20, "normal"))


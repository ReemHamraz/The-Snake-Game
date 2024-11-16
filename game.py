import turtle
import time
import random

# Screen setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off screen updates for smooth gameplay

# Snake setup
snake = []
for i in range(3):
    segment = turtle.Turtle("circle")
    segment.color("limegreen")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# Food setup
food = turtle.Turtle("circle")
food.color("gold")
food.penup()
food.shapesize(1.2, 1.2)  # Larger food size
food.goto(0, 100)

# Food shimmer effect
food_shimmer = ["gold", "yellow", "orange", "red"]

# Score setup
score = 0
high_score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Movement variables
direction = "stop"

# Functions to change direction
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# Key bindings
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

# Move the snake
def move():
    x, y = snake[0].pos()
    if direction == "up":
        snake[0].goto(x, y + 20)
    if direction == "down":
        snake[0].goto(x, y - 20)
    if direction == "left":
        snake[0].goto(x - 20, y)
    if direction == "right":
        snake[0].goto(x + 20, y)

# Main game loop
def game_loop():
    global score, high_score

    while True:
        window.update()
        time.sleep(0.1)

        # Add shimmer effect to food
        food.color(random.choice(food_shimmer))

        # Move the body
        for i in range(len(snake) - 1, 0, -1):
            x, y = snake[i - 1].pos()
            snake[i].goto(x, y)

        # Move the head
        move()

        # Check collision with food
        if snake[0].distance(food) < 15:
            # Move food to a new random location
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            score += 10
            if score > high_score:
                high_score = score
            score_display.clear()
            score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

            # Add a new segment to the snake
            new_segment = turtle.Turtle("circle")
            new_segment.color("limegreen")
            new_segment.penup()
            snake.append(new_segment)

        # Check collision with walls
        x, y = snake[0].pos()
        if x > 290 or x < -290 or y > 290 or y < -290:
            reset_game()

        # Check collision with self
        for segment in snake[1:]:
            if snake[0].distance(segment) < 10:
                reset_game()

def reset_game():
    global score
    time.sleep(1)
    for segment in snake:
        segment.goto(1000, 1000)
    snake.clear()
    for i in range(3):
        segment = turtle.Turtle("circle")
        segment.color("limegreen")
        segment.penup()
        segment.goto(-20 * i, 0)
        snake.append(segment)
    score = 0
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Start the game
game_loop()

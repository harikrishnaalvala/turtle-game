from turtle import Turtle, Screen
from random import randint

# Set up the screen
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race")
screen.bgcolor("lightblue")  # Background color for better visuals

# Ask the user to place a bet
bet = screen.textinput("Turtle Race", "Which turtle will win? (red, blue, green, orange): ").lower()

# Draw start & finish lines
def draw_lines():
    start_line = Turtle()
    start_line.speed(0)
    start_line.penup()
    start_line.goto(-200, 150)
    start_line.pendown()
    start_line.color("black")
    start_line.pensize(4)
    start_line.right(90)
    start_line.forward(300)
    start_line.penup()
    start_line.goto(-220, 160)
    start_line.write("START", font=("Arial", 14, "bold"))

    finish_line = Turtle()
    finish_line.speed(0)
    finish_line.penup()
    finish_line.goto(150, 150)
    finish_line.pendown()
    finish_line.color("black")
    finish_line.pensize(4)
    finish_line.right(90)
    finish_line.forward(300)
    finish_line.penup()
    finish_line.goto(130, 160)
    finish_line.write("FINISH", font=("Arial", 14, "bold"))

# Create turtles
def create_turtle(color, y_position):
    t = Turtle()
    t.color(color)
    t.shape('turtle')
    t.shapesize(1.5)  # Slightly bigger turtles
    t.penup()
    t.goto(-200, y_position)  # Start at 0th line
    t.pendown()
    return t

# Retry function
def retry():
    screen.clearscreen()
    main()  # Restart the game

# Cancel function
def cancel():
    screen.bye()  # Close the game window

# Main function
def main():
    screen.bgcolor("lightblue")
    
    draw_lines()
    players = {
        "red": create_turtle('red', 100),
        "blue": create_turtle('blue', 70),
        "green": create_turtle('green', 40),
        "orange": create_turtle('orange', 10)
    }

    # Start the race
    race_on = True
    while race_on:
        for color, player in players.items():
            move_distance = randint(2, 10)  # Increased speed range
            player.forward(move_distance)
            
            if player.xcor() >= 150:  # Finish line
                race_on = False
                winner = color
                break

    # Announce the winner
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(-150, -130)  # Position at the bottom
    result_turtle.color("green")
    if bet == winner:
        result_turtle.write(f"🎉 Congratulations! The {winner} turtle wins! You guessed right! 🎉", font=("Arial", 12, "bold"))
    else:
        result_turtle.write(f"😢 Sorry, you lost. The {winner} turtle won the race.", font=("Arial", 12, "bold"))

    # Retry Button
    retry_button = Turtle()
    retry_button.penup()
    retry_button.goto(-70, -170)
    retry_button.shape("square")
    retry_button.shapesize(2, 6)  # Size of the button
    retry_button.fillcolor("green")
    retry_button.onclick(lambda x, y: retry())  # Bind function
    retry_text = Turtle()
    retry_text.hideturtle()
    retry_text.penup()
    retry_text.goto(-80, -180)
    retry_text.write("RETRY", font=("Arial", 12, "bold"), align="left")

    # Cancel Button
    cancel_button = Turtle()
    cancel_button.penup()
    cancel_button.goto(70, -170)
    cancel_button.shape("square")
    cancel_button.shapesize(2, 6)
    cancel_button.fillcolor("red")
    cancel_button.onclick(lambda x, y: cancel())  # Bind function
    cancel_text = Turtle()
    cancel_text.hideturtle()
    cancel_text.penup()
    cancel_text.goto(60, -180)
    cancel_text.write("CANCEL", font=("Arial", 12, "bold"), align="left")

screen.listen()  # Listen for button clicks
main()  # Start the game

screen.mainloop()

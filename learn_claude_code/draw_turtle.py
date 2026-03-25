# -*- coding: utf-8 -*-
# Draw a cute little turtle
import turtle
import math

def draw_turtle():
    # Set up screen
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    
    # Create turtle object
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(5)
    
    # Draw shell - main oval body
    def draw_shell():
        turtle_obj.penup()
        turtle_obj.goto(0, 0)
        turtle_obj.setheading(0)
        turtle_obj.pendown()
        turtle_obj.fillcolor("#228B22")  # Forest green
        turtle_obj.begin_fill()
        
        # Draw oval shell
        for i in range(360):
            angle = math.radians(i)
            x = 100 * math.cos(angle)
            y = 70 * math.sin(angle)
            turtle_obj.goto(x, y)
        turtle_obj.end_fill()
        
        # Draw shell border
        turtle_obj.penup()
        turtle_obj.goto(0, 0)
        turtle_obj.pendown()
        turtle_obj.pencolor("#145214")
        for i in range(360):
            angle = math.radians(i)
            x = 85 * math.cos(angle)
            y = 55 * math.sin(angle)
            turtle_obj.goto(x, y)
    
    # Draw shell pattern (hexagon)
    def draw_shell_pattern():
        turtle_obj.penup()
        turtle_obj.goto(0, 0)
        turtle_obj.setheading(90)
        turtle_obj.pendown()
        turtle_obj.pencolor("#145214")
        turtle_obj.pensize(2)
        
        # Center hexagon
        for _ in range(6):
            turtle_obj.forward(30)
            turtle_obj.right(60)
        
        # Radial lines from center to edge
        for i in range(6):
            turtle_obj.penup()
            turtle_obj.goto(0, 0)
            turtle_obj.setheading(90 + i * 60)
            turtle_obj.pendown()
            turtle_obj.forward(65)
    
    # Draw head - oval on the right side of shell
    def draw_head():
        turtle_obj.penup()
        turtle_obj.goto(95, 0)
        turtle_obj.pendown()
        turtle_obj.fillcolor("#32CD32")  # Light green
        turtle_obj.begin_fill()
        
        # Draw head oval
        for i in range(360):
            angle = math.radians(i)
            x = 95 + 35 * math.cos(angle)
            y = 25 * math.sin(angle)
            turtle_obj.goto(x, y)
        turtle_obj.end_fill()
    
    # Draw eyes - on both sides of head
    def draw_eyes():
        # Left eye
        turtle_obj.penup()
        turtle_obj.goto(75, 15)
        turtle_obj.pendown()
        turtle_obj.fillcolor("white")
        turtle_obj.begin_fill()
        turtle_obj.circle(10)
        turtle_obj.end_fill()
        turtle_obj.penup()
        turtle_obj.goto(75, 15)
        turtle_obj.dot(5, "black")
        
        # Right eye
        turtle_obj.penup()
        turtle_obj.goto(115, 15)
        turtle_obj.pendown()
        turtle_obj.fillcolor("white")
        turtle_obj.begin_fill()
        turtle_obj.circle(10)
        turtle_obj.end_fill()
        turtle_obj.penup()
        turtle_obj.goto(115, 15)
        turtle_obj.dot(5, "black")
    
    # Draw mouth
    def draw_mouth():
        turtle_obj.penup()
        turtle_obj.goto(120, -5)
        turtle_obj.setheading(0)
        turtle_obj.pendown()
        turtle_obj.pencolor("#145214")
        turtle_obj.pensize(2)
        turtle_obj.circle(8, 180)  # Smile
    
    # Draw legs - on both sides of shell
    def draw_legs():
        leg_color = "#32CD32"
        turtle_obj.fillcolor(leg_color)
        
        # Front right leg
        turtle_obj.penup()
        turtle_obj.goto(60, 50)
        turtle_obj.setheading(45)
        turtle_obj.pendown()
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.forward(25)
            turtle_obj.right(90)
            turtle_obj.forward(12)
            turtle_obj.right(90)
        turtle_obj.end_fill()
        
        # Back right leg
        turtle_obj.penup()
        turtle_obj.goto(60, -50)
        turtle_obj.setheading(-45)
        turtle_obj.pendown()
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.forward(25)
            turtle_obj.right(90)
            turtle_obj.forward(12)
            turtle_obj.right(90)
        turtle_obj.end_fill()
        
        # Front left leg
        turtle_obj.penup()
        turtle_obj.goto(-60, 50)
        turtle_obj.setheading(135)
        turtle_obj.pendown()
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.forward(25)
            turtle_obj.right(90)
            turtle_obj.forward(12)
            turtle_obj.right(90)
        turtle_obj.end_fill()
        
        # Back left leg
        turtle_obj.penup()
        turtle_obj.goto(-60, -50)
        turtle_obj.setheading(-135)
        turtle_obj.pendown()
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.forward(25)
            turtle_obj.right(90)
            turtle_obj.forward(12)
            turtle_obj.right(90)
        turtle_obj.end_fill()
    
    # Draw tail - on the left side of shell
    def draw_tail():
        turtle_obj.penup()
        turtle_obj.goto(-95, 0)
        turtle_obj.setheading(180)
        turtle_obj.pendown()
        turtle_obj.fillcolor("#32CD32")
        turtle_obj.begin_fill()
        turtle_obj.forward(30)
        turtle_obj.right(90)
        turtle_obj.forward(8)
        turtle_obj.right(90)
        turtle_obj.forward(30)
        turtle_obj.end_fill()
    
    # Execute drawing
    draw_shell()          # Draw shell first (bottom layer)
    draw_shell_pattern()  # Shell pattern
    draw_legs()           # Legs on both sides
    draw_tail()           # Tail behind shell
    draw_head()           # Head in front
    draw_eyes()           # Eyes on head
    draw_mouth()          # Mouth
    
    # Hide turtle
    turtle_obj.hideturtle()
    
    # Click to close
    screen.exitonclick()

if __name__ == "__main__":
    draw_turtle()

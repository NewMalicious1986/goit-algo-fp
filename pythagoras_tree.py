import turtle
import math

def draw_background(screen):
    canvas = screen.getcanvas()

def draw_tree(t, length, level):
    if level == 0:
        t.pensize(2)  # Leaves are thin
        t.color("green")  # Leaves are green
        t.forward(length)
        t.backward(length)
        t.color("brown")  # Reset color to brown for branches
        return
    
    t.pensize(level + 3)  # Set thickness based on recursion depth
    
    # Draw trunk
    t.forward(length)
    
    # Save current position and angle
    start_pos = t.position()
    start_heading = t.heading()
    
    # Draw left branch
    t.left(45)
    draw_tree(t, length * math.sqrt(0.5), level - 1)
    
    # Return to start position and heading
    t.penup()
    t.setposition(start_pos)
    t.setheading(start_heading)
    t.pendown()
    
    # Draw right branch
    t.right(45)
    draw_tree(t, length * math.sqrt(0.5), level - 1)
    
    # Return to start position
    t.penup()
    t.setposition(start_pos)
    t.setheading(start_heading)
    t.pendown()
    
    # Move back to original position
    t.backward(length)

def pythagoras_tree(level):
    screen = turtle.Screen()
    screen.title("Pythagorean Tree Fractal")
    screen.setup(width=1000, height=800)
    
    draw_background(screen)  # Draw the custom background
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("brown")  # Set initial color to brown for the tree trunk
    t.pensize(level + 3)  # Set initial thickness for the trunk
    
    # Position turtle at bottom center
    t.penup()
    t.goto(0, -250)
    t.setheading(90)  # Point upwards
    t.pendown()
    
    # Start drawing
    draw_tree(t, 150, level)
    
    screen.mainloop()

if __name__ == "__main__":
    try:
        level = int(input("Enter recursion depth (e.g., 5-10): "))
        pythagoras_tree(level)
    except ValueError:
        print("Please enter a valid integer.")
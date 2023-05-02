import pygame

# Define the size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the color of the canvas
CANVAS_COLOR = (255, 255, 255)

# Define the color of the brush
BRUSH_COLOR = (0, 0, 0)

# Define the size of the brush
BRUSH_SIZE = 5

# Define a list to store the points of the drawing
drawing = []

# Create a surface to hold the drawing
drawing_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

# Define a function to draw a line between two points
def draw_line(start, end):
    pygame.draw.line(drawing_surface, BRUSH_COLOR, start, end, BRUSH_SIZE)

# Game loop
drawing_allowed = True # Set drawing_allowed to True at the start of the game
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and drawing_allowed: # Only draw when left mouse button is pressed and drawing_allowed is True
                # Add the starting point of a new line to the drawing list
                drawing.append(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: # Only draw when left mouse button is pressed
                # Add the current point of the line to the drawing list
                drawing.append(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing_allowed: # Only draw when left mouse button is released and drawing_allowed is True
                # Draw the lines on the drawing surface when the mouse button is released
                drawing.append(pygame.mouse.get_pos())
                for i in range(len(drawing) - 1):
                    draw_line(drawing[i], drawing[i+1])
                print(drawing)
                drawing_allowed = False # Set drawing_allowed to False after the first line is drawn

    # Clear the screen
    screen.fill(CANVAS_COLOR)

    # Draw the drawing surface onto the screen
    screen.blit(drawing_surface, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

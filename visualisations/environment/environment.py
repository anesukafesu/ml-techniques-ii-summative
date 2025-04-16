import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Define vertices for a unit cube
def cube_vertices(x, y, z, size):
    return np.array([
        [x, y, z],
        [x + size, y, z],
        [x + size, y + size, z],
        [x, y + size, z],
        [x, y, z + size],
        [x + size, y, z + size],
        [x + size, y + size, z + size],
        [x, y + size, z + size]
    ], dtype=np.float32)

# Define cube edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Function to draw a cube
def draw_cube(vertices):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Function to draw a main cube with smaller subcubes
def draw_subdivided_cube(grid_size=2):
    cube_size = 2.0  # Total cube size
    sub_size = cube_size / grid_size  # Size of each subcube
    start = -cube_size / 2  # Center the cube at origin

    for i in range(grid_size):
        for j in range(grid_size):
            for k in range(grid_size):
                x, y, z = start + i * sub_size, start + j * sub_size, start + k * sub_size
                draw_cube(cube_vertices(x, y, z, sub_size))

# Main OpenGL loop
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Move back for visibility
    glEnable(GL_DEPTH_TEST)

    running = True
    angle = 0

    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 1, 1, 1)  # Rotate for better visibility

        draw_subdivided_cube(grid_size=4)  # Change grid_size for more subcubes

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(100)
        angle += 1  # Rotation speed

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
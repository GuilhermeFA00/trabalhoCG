from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_quad():
    """
    Function to draw a quad using OpenGL.

    This function sets up the OpenGL context, creates a window, and draws a quad.

    Returns:
    - None
    """

    # Initialize GLUT
    glutInit()

    # Set up the display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set up the window size and position
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    # Create the window
    glutCreateWindow(b"OpenGL Quad")

    # Set the background color
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Set up the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    # Set up the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set up the viewport
    glViewport(0, 0, 500, 500)

    # Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # Set the color for the quad
    glColor3f(1.0, 0.0, 0.0)

    # Draw the quad
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

    # Flush the OpenGL pipeline
    glFlush()

    # Enter the main loop
    glutMainLoop()

# Call the draw_quad function to draw the quad
draw_quad()

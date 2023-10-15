import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np

class Janela:
    def __init__(self, titulo, largura, altura):
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
        glut.glutInitWindowSize(largura, altura)
        glut.glutCreateWindow(titulo)
        glut.glutDisplayFunc(self.draw)
    
    def draw(self, draw_function):
        draw_function()
    def run(self):
        glut.glutMainLoop()

def transform_to_ndc(coordinates, width, height):
    viewport_width = width
    viewport_height = height
    
    ndc_coordinates = []
    for x, y in coordinates:
        ndc_x = 2 * x / viewport_width - 1
        ndc_y = 2 * y / viewport_height - 1
        ndc_coordinates.append([ndc_x, ndc_y])
    
    return ndc_coordinates
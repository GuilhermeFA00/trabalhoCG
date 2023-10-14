# Importar o módulo OpenGL
import OpenGL.GL as gl
import OpenGL.GLUT as glut

# Criar uma classe que representa uma janela com openGL e python
class Janela:
    # Inicializar a janela com o título, a largura e a altura
    def __init__(self, titulo, largura, altura, desenho_func):
        # Inicializar o GLUT
        glut.glutInit()
        # Criar uma janela com o título dado
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
        glut.glutInitWindowSize(largura, altura)
        glut.glutCreateWindow(titulo)
        # Definir a função que desenha a janela como a função de exibição
        glut.glutDisplayFunc(self.draw)
    
    # Definir a função que desenha a janela
    def draw(self):
      self.desenho_func
      
    
    # Definir a função que inicia o loop principal do GLUT
    def run(self):
        glut.glutMainLoop()

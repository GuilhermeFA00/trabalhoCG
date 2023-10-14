# Importar as bibliotecas necessárias
import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

# Definir as cores dos quadrados
VERMELHO = (1.0, 0.0, 0.0)
CINZA = (0.5, 0.5, 0.5)

# Definir o tamanho dos quadrados
TAMANHO = 0.2

# Definir as posições iniciais dos quadrados
POSICAO_VERMELHO = (-0.5, 0.0)
POSICAO_CINZA = (0.5, 0.0)

# Definir uma variável para armazenar o quadrado selecionado
SELECIONADO = None

# Definir uma função para desenhar um quadrado
def desenhar_quadrado(x, y, cor):
    # Definir a cor do quadrado
    gl.glColor3f(*cor)
    # Iniciar o desenho do quadrado
    gl.glBegin(gl.GL_QUADS)
    # Definir os vértices do quadrado
    gl.glVertex2f(x - TAMANHO, y - TAMANHO)
    gl.glVertex2f(x + TAMANHO, y - TAMANHO)
    gl.glVertex2f(x + TAMANHO, y + TAMANHO)
    gl.glVertex2f(x - TAMANHO, y + TAMANHO)
    # Terminar o desenho do quadrado
    gl.glEnd()

# Definir uma função para verificar se um ponto está dentro de um quadrado
def ponto_dentro_quadrado(x, y, qx, qy):
    # Retornar verdadeiro se o ponto está dentro do quadrado, falso caso contrário
    return qx - TAMANHO <= x <= qx + TAMANHO and qy - TAMANHO <= y <= qy + TAMANHO

# Definir uma função para lidar com o evento de clique do mouse
def mouse(clique, estado, x, y):
    # Converter as coordenadas do mouse para o sistema de coordenadas da janela
    x = x / (LARGURA / 2) - 1
    y = 1 - y / (ALTURA / 2)
    # Verificar se o botão esquerdo do mouse foi pressionado
    if clique == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
        global SELECIONADO, POSICAO_VERMELHO, POSICAO_CINZA
        if ponto_dentro_quadrado(x, y, *POSICAO_VERMELHO):
            # Selecionar o quadrado vermelho
            SELECIONADO = VERMELHO
            print(SELECIONADO)
        elif ponto_dentro_quadrado(x, y, *POSICAO_CINZA):
            # Selecionar o quadrado cinza
            SELECIONADO = CINZA
            print(SELECIONADO)
        elif SELECIONADO == VERMELHO or SELECIONADO == CINZA:
            print("Selecionado is not none", SELECIONADO)
            # Trocar a posição do quadrado selecionado com o outro quadrado
            if SELECIONADO == VERMELHO:
                print("O selecionado é vermelho")
                POSICAO_VERMELHO, POSICAO_CINZA = POSICAO_CINZA, POSICAO_VERMELHO
            else:
                print("O selecionado é cinza")
                POSICAO_CINZA, POSICAO_VERMELHO = POSICAO_VERMELHO, POSICAO_CINZA
            glut.glutPostRedisplay()
            # Desmarcar o quadrado selecionado
            SELECIONADO = None
"""def motion(mousex, mousey):
    global quads
    # Converter as coordenadas do mouse para o sistema de coordenadas do OpenGL
    x = mousex
    y = TAMANHO - mousey
    print(x, y)
    # Se há um quadrilátero selecionado
    if SELECIONADO is not None:
        print("selected is not none ", SELECIONADO)
        # Obter o índice do quadrilátero selecionado
        i, j = SELECIONADO
        # Atualizar a posição do quadrilátero selecionado com as coordenadas do mouse
        quads[i][j] = (x, y)
        # Redesenhar os quadriláteros
        glut.glutPostRedisplay()
"""
# Definir uma função para desenhar a cena na janela
def desenhar():
    # Limpar a janela com a cor preta
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    # Desenhar os dois quadrados na janela
    desenhar_quadrado(*POSICAO_VERMELHO, VERMELHO)
    desenhar_quadrado(*POSICAO_CINZA, CINZA)
    # Atualizar a janela na tela
    glut.glutSwapBuffers()

# Definir as dimensões da janela em pixels
LARGURA = 800
ALTURA = 600

# Inicializar o GLUT e criar a janela
glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(LARGURA, ALTURA)
glut.glutCreateWindow("Janela com quadrados")

# Definir as funções de callback para os eventos
glut.glutDisplayFunc(desenhar)
glut.glutMouseFunc(mouse)

# Entrar no loop principal do GLUT
glut.glutMainLoop()

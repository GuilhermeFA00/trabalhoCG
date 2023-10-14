# Importar as bibliotecas necessárias
import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

# Definir as dimensões da janela em pixels
LARGURA = 800
ALTURA = 600
#spacing = 0.1 * min(LARGURA, ALTURA)
#size = (min(LARGURA, ALTURA) - (3 + 1) * spacing) / 3

# Definir as cores dos quadrados
VERMELHO = (1.0, 0.0, 0.0)
CINZA = (0.5, 0.5, 0.5)
AZUL = (0.0, 0.0, 1.0)

# Definir o tamanho dos quadrados
TAMANHO = 0.2

# Definir as posições iniciais dos quadrados
POSICAO_VERMELHO = (-0.5, 0.0)
POSICAO_CINZA = (0.5, 0.0)
POSICAO_AZUL = (0.0, 0.5)
"""colors = [[1.0, 0.0, 0.0],
          [0.5, 0.5, 0.5],
          [0.0, 0.0, 1.0]]
posicoes = [[-0.5, 0.0],
            [0.5, 0.0],
            [0.0, 0.5]]"""
#p1, p2, p3, p4, p5, p6, p7, p8, p9 = [[30.0, 30.0], [120.0, 30.0], [210.0, 30.0], [30.0, 120.0], [120.0, 120.0], [210.0, 120.0], [30.0, 210.0], [120.0, 210.0], [210.0, 210.0]]
p1, p2, p3, p4, p5, p6, p7, p8, p9 = [[-0.7142857142857143, -0.7142857142857143], [-0.1428571428571429, -0.7142857142857143], [0.4285714285714286, -0.7142857142857143], [-0.7142857142857143, -0.1428571428571429], [-0.1428571428571429, -0.1428571428571429], [0.4285714285714286, -0.1428571428571429], [-0.7142857142857143, 0.4285714285714286], [-0.1428571428571429, 0.4285714285714286], [0.4285714285714286, 0.4285714285714286]]
p1_color = [1.0, 0.5, 0.0]
p2_color = [0.5, 1.0, 0.0]
p3_color = [0.5, 1.0, 0.5]
p4_color = [0.0, 0.5, 0.0]
p5_color = [0.0, 1.0, 1.0]
p6_color = [1.0, 0.0, 1.0]
p7_color = [1.0, 0.0, 0.0]
p8_color = [0.0, 1.0, 0.0]
p9_color = [0.0, 0.0, 1.0]

colors = [p1_color, p2_color, p3_color, p4_color, p5_color, p6_color, p7_color, p8_color, p9_color]
posicoes = [p1, p2, p3, p4, p5, p6, p7, p8, p9]


# Definir uma variável para armazenar o quadrado selecionado
SELECIONADO = None
P_SELECIONADO = None

# Definir uma função para desenhar um quadrado
def desenhar_quadrado(x, y, cor):
    global size
    # Definir a cor do quadrado
    gl.glColor3f(*cor)
    # Iniciar o desenho do quadrado
    gl.glBegin(gl.GL_QUADS)
    # Definir os vértices do quadrado
    gl.glVertex2f(x - 0.25, y - 0.25)
    gl.glVertex2f(x + 0.25, y - 0.25)
    gl.glVertex2f(x + 0.25, y + 0.25)
    gl.glVertex2f(x - 0.25, y + 0.25)
    # Terminar o desenho do quadrado
    gl.glEnd()

# Definir uma função para verificar se um ponto está dentro de um quadrado
def ponto_dentro_quadrado(x, y, qx, qy):
    # Retornar verdadeiro se o ponto está dentro do quadrado, falso caso contrário
    return qx - 0.25 <= x <= qx + 0.25 and qy - 0.25 <= y <= qy + 0.25

# Definir uma função para lidar com o evento de clique do mouse
"""def mouse(clique, estado, x, y):
    # Converter as coordenadas do mouse para o sistema de coordenadas da janela
    x = x / (LARGURA / 2) - 1
    y = 1 - y / (ALTURA / 2)
    # Verificar se o botão esquerdo do mouse foi pressionado
    if clique == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
        global SELECIONADO, POSICAO_VERMELHO, POSICAO_CINZA, POSICAO_AZUL, P_SELECIONADO
        if ponto_dentro_quadrado(x, y, *POSICAO_VERMELHO):
            # Selecionar o quadrado vermelho
            SELECIONADO = VERMELHO
            print("Vermelho selecionado")
        if ponto_dentro_quadrado(x, y, *POSICAO_CINZA):
            # Selecionar o quadrado cinza
            SELECIONADO = CINZA
            print("Cinza selecionado")
        if ponto_dentro_quadrado(x, y, *POSICAO_AZUL):
            # Selecionar o quadrado cinza
            SELECIONADO = AZUL
            print("Azul selecionado")
        elif SELECIONADO != None:
            print("Selecionado is not none", SELECIONADO)
            # Trocar a posição do quadrado selecionado com o outro quadrado
            if SELECIONADO == VERMELHO:
                print("O selecionado é vermelho")
                if ponto_dentro_quadrado(x, y, *POSICAO_CINZA):
                    # Selecionar o quadrado cinza
                    P_SELECIONADO = CINZA
                    print("Cinza selecionado")
                if ponto_dentro_quadrado(x, y, *POSICAO_AZUL):
                    # Selecionar o quadrado cinza
                    P_SELECIONADO = AZUL
                    print("Azul selecionado")
                elif P_SELECIONADO != None:
                    if P_SELECIONADO == CINZA:
                        POSICAO_VERMELHO, POSICAO_CINZA = POSICAO_CINZA, POSICAO_VERMELHO
                    if P_SELECIONADO == AZUL:
                        POSICAO_VERMELHO, POSICAO_AZUL = POSICAO_AZUL, POSICAO_VERMELHO
            
            if SELECIONADO == CINZA:
                print("O selecionado é cinza")
                POSICAO_CINZA, POSICAO_VERMELHO = POSICAO_VERMELHO, POSICAO_CINZA
            glut.glutPostRedisplay()
            # Desmarcar o quadrado selecionado
            SELECIONADO = None"""

def mouse(clique, estado, x, y):
    # Converter as coordenadas do mouse para o sistema de coordenadas da janela
    x = x / (LARGURA / 2) - 1
    y = 1 - y / (ALTURA / 2)
    # Verificar se o botão esquerdo do mouse foi pressionado
    if clique == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
        print("boton selected")
        print(x, y)
        global SELECIONADO, POSICAO_VERMELHO, POSICAO_CINZA, POSICAO_AZUL, AUXILIAR
        # Verificar se nenhum quadrado foi selecionado anteriormente
        if SELECIONADO is None:
            # Percorrer a lista de posições dos quadrados
            for i in range(9):
                # Verificar se o clique foi dentro do quadrado i
                if ponto_dentro_quadrado(x, y, *posicoes[i]):
                    # Selecionar o quadrado i e armazenar seu índice na variável auxiliar
                    SELECIONADO = i
                    AUXILIAR = i
                    print("Quadrado", i, "selecionado")
                    # Sair do loop
                    break
        else:
            # Percorrer a lista de posições dos quadrados
            for i in range(9):
                # Verificar se o clique foi dentro do quadrado i e se ele não estava selecionado
                if ponto_dentro_quadrado(x, y, *posicoes[i]) and SELECIONADO != i:
                    # Trocar a posição do quadrado selecionado com o quadrado clicado
                    posicoes[SELECIONADO], posicoes[i] = posicoes[i], posicoes[SELECIONADO]
                    print("Quadrados", AUXILIAR, "e", i, "trocaram de posição")
                    # Desmarcar o quadrado selecionado e limpar a variável auxiliar
                    SELECIONADO = None
                    AUXILIAR = None
                    # Sair do loop
                    break
            # Atualizar a janela
            glut.glutPostRedisplay()


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

def redimensionaJanela(largura, altura):
    janelaLargura = largura
    janelaAltura = altura

    gl.glViewport(0,0,largura,altura)
    glut.glutPostRedisplay()

# Definir uma função para desenhar a cena na janela
def desenhar():
    # Limpar a janela com a cor preta
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    # Desenhar os dois quadrados na janela
    for pos, col in zip(posicoes, colors):
        desenhar_quadrado(*pos, col)
    """desenhar_quadrado(*POSICAO_VERMELHO, VERMELHO)
    desenhar_quadrado(*POSICAO_CINZA, CINZA)
    desenhar_quadrado(*POSICAO_AZUL, AZUL)"""
    """desenhar_quadrado(*p1, p1_color)
    desenhar_quadrado(*p2, p2_color)
    desenhar_quadrado(*p3, p3_color)
    desenhar_quadrado(*p4, p4_color)
    desenhar_quadrado(*p5, p5_color)
    desenhar_quadrado(*p6, p6_color)
    desenhar_quadrado(*p7, p7_color)
    desenhar_quadrado(*p8, p8_color)
    desenhar_quadrado(*p9, p9_color)"""
    # Atualizar a janela na tela
    glut.glutSwapBuffers()


# Inicializar o GLUT e criar a janela
glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(LARGURA, ALTURA)
glut.glutCreateWindow("Janela com quadrados")

# Definir as funções de callback para os eventos
glut.glutDisplayFunc(desenhar)
glut.glutReshapeFunc(redimensionaJanela)
glut.glutMouseFunc(mouse)

# Entrar no loop principal do GLUT
glut.glutMainLoop()


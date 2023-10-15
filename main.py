#Guilherme Frutuoso
#João Victor
#Jônathas Nobre

import sys
from OpenGL.GL import *
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from PIL import Image       
from random import shuffle, sample
import copy
from texture import Texture
from draws import NonCurveDraws
from glutils import transform_to_ndc

# Definir as dimensões da janela em pixels
LARGURA = 800
ALTURA = 600
#spacing = 0.1 * min(LARGURA, ALTURA)
#size = (min(LARGURA, ALTURA) - (3 + 1) * spacing) / 3

PosicoesIniciais = NonCurveDraws()
PosIniList = PosicoesIniciais.init_quads()
listoflist = []
for l in PosIniList:
    for t in l:
        t = list(t)
        listoflist.append(t)

p1, p2, p3, p4, p5, p6, p7, p8, p9 =  listoflist
results = transform_to_ndc(listoflist, 300, 300)
p1, p2, p3, p4, p5, p6, p7, p8, p9 = results
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


SELECIONADO = None
P_SELECIONADO = None

def desenhar_quadrado(x, y, cor, t):
    global size
    gl.glColor3f(*cor)
    # Iniciar o desenho do quadrado
    glBindTexture(GL_TEXTURE_2D, t) 
    gl.glBegin(gl.GL_QUADS)
    # Definir os vértices do quadrado
    glTexCoord2f(0,0) 
    gl.glVertex2f(x - 0.25, y - 0.25)
    glTexCoord2f(1,0) 
    gl.glVertex2f(x + 0.25, y - 0.25)
    glTexCoord2f(1,1) 
    gl.glVertex2f(x + 0.25, y + 0.25)
    glTexCoord2f(0,1) 
    gl.glVertex2f(x - 0.25, y + 0.25)
    # Terminar o desenho do quadrado
    gl.glEnd()

def ponto_dentro_quadrado(x, y, qx, qy):
    # Retornar verdadeiro se o ponto está dentro do quadrado, falso caso contrário
    return qx - 0.25 <= x <= qx + 0.25 and qy - 0.25 <= y <= qy + 0.25


def mouse(clique, estado, x, y):
    x = x / (LARGURA / 2) - 1
    y = 1 - y / (ALTURA / 2)
    # Verificar se o botão esquerdo do mouse foi pressionado
    if clique == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
        print("boton selected")
        global SELECIONADO,  AUXILIAR
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
                    break
        else:
            for i in range(9):
                # Verificar se o clique foi dentro do quadrado i e se ele não estava selecionado
                if ponto_dentro_quadrado(x, y, *posicoes[i]) and SELECIONADO != i:
                    # Trocar a posição do quadrado selecionado com o quadrado clicado
                    posicoes[SELECIONADO], posicoes[i] = posicoes[i], posicoes[SELECIONADO]
                    print("Quadrados", AUXILIAR, "e", i, "trocaram de posição")
                    # Desmarcar o quadrado selecionado e limpar a variável auxiliar
                    SELECIONADO = None
                    AUXILIAR = None
                    break
            for i in range(len(tid_list_random)):
                relacao_sampled[tid_list_random[i]] = posicoes[i]
            #print(relacao_sampled)
            glut.glutPostRedisplay()
            verificar_vitoria()



def redimensionaJanela(largura, altura):
    janelaLargura = largura
    janelaAltura = altura

    gl.glViewport(0,0,largura,altura)
    glut.glutPostRedisplay()

def desenhar():
    gl.glClearColor(1.0, 1.0, 0.5, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    for pos, col, t in zip(posicoes, colors, tid_list_random):
        desenhar_quadrado(*pos, col, t)
    glut.glutSwapBuffers()

def verificar_vitoria():
    global posicoes, tid_list
    print("função chm")
    for i in range(9):
        print("entrou no for")
        print(relacao[i+1])
        print(relacao_sampled[i+1])
        if relacao[i+1] != relacao_sampled[i+1]:
            return False
    print("Parabéns! Você completou o quebra-cabeça!")
    return True

glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(LARGURA, ALTURA)
glut.glutCreateWindow("Janela com quadrados")

texture = Texture(posicoes)
tid_list, tid_list_random, relacao, relacao_sampled = texture.text_inicio()
tid_list_comp = copy.deepcopy(tid_list_random)

glut.glutDisplayFunc(desenhar)
glut.glutReshapeFunc(redimensionaJanela)
glut.glutMouseFunc(mouse)

glut.glutMainLoop()

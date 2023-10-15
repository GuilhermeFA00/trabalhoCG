# Importar as bibliotecas necessárias
import sys
from OpenGL.GL import *
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from PIL import Image       # módulo responsável por carregar imagens JPG, PNG, etc.
from random import shuffle, sample
import copy

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

t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0   # identificadores das texturas

#Função responsável por carregar uma textura a partir do nome do arquivo
def carregaTextura(filename):
    #carregamento da textura feita pelo módulo PIL
    img = Image.open(filename)                  #abrindo o arquivo da textura
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  #espelhando verticalmente a textura (normalmente, a coordenada y das imagens cresce de cima para baixo)
    imgData = img.convert("RGBA").tobytes()     #convertendo a imagem carregada em bytes que serão lidos pelo OpenGL

    #criando o objeto textura dentro da máquina OpenGL
    texId = glGenTextures(1)                                                                                #criando um objeto textura
    glBindTexture(GL_TEXTURE_2D, texId)                                                                     #tornando o objeto textura recém criado ativo
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)                                        #definindo que textura será suavizada ao ser aplicada no objeto
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)                                              #definindo que a cor da textura substituirá a cor do polígono
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,  img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgData)  #enviando os dados lidos pelo módulo PIL para a OpenGL
    glBindTexture(GL_TEXTURE_2D, 0)                                                                         #tornando o objeto textura inativo por enquanto

    #retornando o identificador da textura recém-criada
    return texId

#Função de inicialização da aplicação
def text_inicio():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9                            #definindo a cor de fundo da tela
    glEnable(GL_TEXTURE_2D)                             #habilitando o uso de texturas
    glEnable(GL_BLEND);                                 #habilitando a funcionalidade de mistura (necessário para objetos transparentes)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   #definindo como a mistura entre objetos transparência deve ser realizada
    t1 = carregaTextura('/home/gfa/PycharmProjects/cg/peca1.png')             #carregando textura 1 e guardando seu identificador em t1
    t2 = carregaTextura('/home/gfa/PycharmProjects/cg/peca2.png')
    t3 = carregaTextura('/home/gfa/PycharmProjects/cg/peca3.png')                   #carregando textura 2 e guardando seu identificador em t2
    t4 = carregaTextura('/home/gfa/PycharmProjects/cg/peca4.png') 
    t5 = carregaTextura('/home/gfa/PycharmProjects/cg/peca5.png') 
    t6 = carregaTextura('/home/gfa/PycharmProjects/cg/peca6.png') 
    t7 = carregaTextura('/home/gfa/PycharmProjects/cg/peca7.png') 
    t8 = carregaTextura('/home/gfa/PycharmProjects/cg/peca8.png') 
    t9 = carregaTextura('/home/gfa/PycharmProjects/cg/peca9.png')

    tid_list = [t7, t8, t9, t6, t5, t4, t1, t2, t3]
    relacao = {}
    relacao_sampled = {}
    # Percorrer as listas de texturas e posicoes e adicionar os pares ao dicionario
    for i in range(len(tid_list)):
        relacao[tid_list[i]] = posicoes[i]

    tid_list_random = sample(tid_list, len(tid_list))
    for i in range(len(tid_list_random)):
        relacao_sampled[tid_list_random[i]] = posicoes[i]

    return tid_list, tid_list_random, relacao, relacao_sampled

# Definir uma função para desenhar um quadrado
def desenhar_quadrado(x, y, cor, t):
    global size
    # Definir a cor do quadrado
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

# Definir uma função para verificar se um ponto está dentro de um quadrado
def ponto_dentro_quadrado(x, y, qx, qy):
    # Retornar verdadeiro se o ponto está dentro do quadrado, falso caso contrário
    return qx - 0.25 <= x <= qx + 0.25 and qy - 0.25 <= y <= qy + 0.25


def mouse(clique, estado, x, y):
    # Converter as coordenadas do mouse para o sistema de coordenadas da janela
    x = x / (LARGURA / 2) - 1
    y = 1 - y / (ALTURA / 2)
    # Verificar se o botão esquerdo do mouse foi pressionado
    if clique == glut.GLUT_LEFT_BUTTON and estado == glut.GLUT_DOWN:
        print("boton selected")
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

# Definir uma função para desenhar a cena na janela
def desenhar():
    # Limpar a janela com a cor preta
    gl.glClearColor(1.0, 1.0, 0.5, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    # Desenhar os dois quadrados na janela
    for pos, col, t in zip(posicoes, colors, tid_list_random):
        desenhar_quadrado(*pos, col, t)
    # Atualizar a janela na tela
    glut.glutSwapBuffers()

def verificar_vitoria():
    global posicoes, tid_list
    # Definir a lista de posições corretas das texturas
    #posicoes_corretas = [[-0.1428571428571429, -0.7142857142857143], [-0.7142857142857143, -0.7142857142857143], [0.4285714285714286, -0.7142857142857143], [-0.7142857142857143, -0.1428571428571429], [-0.1428571428571429, -0.1428571428571429], [0.4285714285714286, -0.1428571428571429], [-0.7142857142857143, 0.4285714285714286], [-0.1428571428571429, 0.4285714285714286], [0.4285714285714286, 0.4285714285714286]]
    # Comparar as posições atuais das texturas com as posições corretas
    print("função chm")
    for i in range(9):
        print("entrou no for")
        # Se alguma posição estiver diferente, retornar falso e sair da função
        print(relacao[i+1])
        print(relacao_sampled[i+1])
        if relacao[i+1] != relacao_sampled[i+1]:
            return False
    # Se todas as posições estiverem iguais, retornar verdadeiro e imprimir uma mensagem de parabéns na tela
    print("Parabéns! Você completou o quebra-cabeça!")
    return True

# Inicializar o GLUT e criar a janela
glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(LARGURA, ALTURA)
glut.glutCreateWindow("Janela com quadrados")

tid_list, tid_list_random, relacao, relacao_sampled = text_inicio()
print(relacao)
print(relacao_sampled)
tid_list_comp = copy.deepcopy(tid_list_random)

# Definir as funções de callback para os eventos
glut.glutDisplayFunc(desenhar)
glut.glutReshapeFunc(redimensionaJanela)
glut.glutMouseFunc(mouse)
#verificar_vitoria()

# Entrar no loop principal do GLUT
glut.glutMainLoop()


"""
{3: [0.4285714285714286, 0.4285714285714286], 2: [-0.1428571428571429, 0.4285714285714286], 4: [0.4285714285714286, -0.1428571428571429], ] 
9: [0.4285714285714286, -0.7142857142857143], 8: [-0.1428571428571429, -0.7142857142857143], 1: [-0.7142857142857143, 0.4285714285714286], 
5: [-0.1428571428571429, -0.1428571428571429], 6: [-0.7142857142857143, -0.1428571428571429], 7: [-0.7142857142857143, -0.7142857142857143]}

{7: [-0.7142857142857143, -0.7142857142857143], 8: [-0.1428571428571429, -0.7142857142857143], 9: [0.4285714285714286, -0.7142857142857143], 
6: [-0.7142857142857143, -0.1428571428571429], 5: [-0.1428571428571429, -0.1428571428571429], 4: [0.4285714285714286, -0.1428571428571429], 
1: [-0.7142857142857143, 0.4285714285714286], 2: [-0.1428571428571429, 0.4285714285714286], 3: [0.4285714285714286, 0.4285714285714286]}
"""

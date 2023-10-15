# Reúso do código fornecido pelo professor Rafael Ivo com alterações para mapear as coordenadas das posições com os ids das texturas

from OpenGL.GL import *
from PIL import Image       # módulo responsável por carregar imagens JPG, PNG, etc.
from random import shuffle, sample
import copy

t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0 

class Texture:
    def __init__(self, posicoes):
        self.posicoes = posicoes

    def carregaTextura(self, filename):
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
    def text_inicio(self):
        global t1, t2, t3, t4, t5, t6, t7, t8, t9                            #definindo a cor de fundo da tela
        glEnable(GL_TEXTURE_2D)                             #habilitando o uso de texturas
        glEnable(GL_BLEND);                                 #habilitando a funcionalidade de mistura (necessário para objetos transparentes)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   #definindo como a mistura entre objetos transparência deve ser realizada
        t1 = self.carregaTextura('peca1.png')             #carregando textura 1 e guardando seu identificador em t1
        t2 = self.carregaTextura('peca2.png')
        t3 = self.carregaTextura('peca3.png')                   #carregando textura 2 e guardando seu identificador em t2
        t4 = self.carregaTextura('peca4.png') 
        t5 = self.carregaTextura('peca5.png') 
        t6 = self.carregaTextura('peca6.png') 
        t7 = self.carregaTextura('peca7.png') 
        t8 = self.carregaTextura('peca8.png') 
        t9 = self.carregaTextura('peca9.png')

        tid_list = [t7, t8, t9, t6, t5, t4, t1, t2, t3]
        relacao = {}
        relacao_sampled = {}
        # Percorrer as listas de texturas e posicoes e adicionar os pares ao dicionario
        for i in range(len(tid_list)):
            relacao[tid_list[i]] = self.posicoes[i]

        tid_list_random = sample(tid_list, len(tid_list))
        for i in range(len(tid_list_random)):
            relacao_sampled[tid_list_random[i]] = self.posicoes[i]

        return tid_list, tid_list_random, relacao, relacao_sampled
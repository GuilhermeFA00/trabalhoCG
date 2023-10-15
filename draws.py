import OpenGL.GL as gl
import OpenGL.GLUT as glut

quads = []

class NonCurveDraws:

    def __init__(self) -> None:
        # Definir as variáveis globais
        self.rows = 3 # Número de linhas de quadriláteros
        self.cols = 3 # Número de colunas de quadriláteros
        self.color_list = [0, 0, 0] # Cor dos quadriláteros (preta)
        self.colors_lists = [[1.0, 0.5, 0.0], [0.5, 1.0, 0.0], [0.5, 1.0, 0.5], [0.0, 0.5, 0.0], [0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        self.width = 300 # Largura da janela
        self.height = 300 # Altura da janela
        self.spacing = 0.1 * min(self.width, self.height) # Espaçamento entre os quadriláteros
        self.size = (min(self.width, self.height) - (self.rows + 1) * self.spacing) / self.rows # Tamanho dos quadriláteros
        self.size = int(self.size)
        self.quads = [] # Lista que armazena as posições dos quadriláteros
        self.selected = None # Variável que armazena o índice do quadrilátero selecionado

    def quads_grid_draw(self, rows_number=3, cols_number=3, color_list=[0, 0, 0], width=300, height=300):
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        rows = rows_number
        cols = cols_number
        width = 300
        height = 300
        # Definir o espaçamento entre os quadriláteros como 10% da largura e da altura da janela
        spacing = 0.1 * min(width, height)
        # Calcular o tamanho dos quadriláteros como a diferença entre a largura ou a altura da janela e o espaçamento total, dividida pelo número de linhas ou colunas
        size = (min(width, height) - (rows + 1) * spacing) / rows
        # Desenhar os quadriláteros em um loop aninhado
        for i, cs in zip(range(rows), range(0, len(self.colors_lists), 3)):
            for j, l in zip(range(cols), range(cs, len(self.colors_lists), 1)):
                # Calcular as coordenadas do canto inferior esquerdo do quadrilátero atual
                x = spacing + j * (size + spacing)
                y = spacing + i * (size + spacing)
                x = int(x)
                y = int(y)
                size = int(size)
                r, g, b = self.colors_lists[l]
                print(r, g, b)
                gl.glColor3f(r, g, b)
                gl.glBegin(gl.GL_QUADS)
                gl.glVertex2i(x, y)
                gl.glVertex2i(x + size, y)
                gl.glVertex2i(x + size, y + size)
                gl.glVertex2i(x, y + size)
                gl.glEnd()
        # Forçar a execução dos comandos de desenho
        gl.glFlush()

    def init_quads(self):
        global quads
        # Inicializar a lista de quadriláteros como uma matriz vazia
        quads = [[] for _ in range(self.rows)]
        # Calcular as posições iniciais dos quadriláteros em um loop aninhado
        for i in range(self.rows):
            for j in range(self.cols):
                # Calcular as coordenadas do canto inferior esquerdo do quadrilátero atual
                x = self.spacing + j * (self.size + self.spacing)
                y = self.spacing + i * (self.size + self.spacing)
                # Adicionar as coordenadas à lista de quadriláteros
                quads[i].append((x, y))
        return quads
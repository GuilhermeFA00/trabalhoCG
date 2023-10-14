# Importar o módulo OpenGL
import OpenGL.GL as gl
import OpenGL.GLUT as glut

class NonCurveDraws:

    def __init__(self) -> None:
        pass

    def quads_grid_draw(self, rows_number, cols_number, color_list, width, height):
        # Limpar a tela com a cor branca
        gl.glClearColor(1.0, 1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        # Definir a cor dos quadriláteros como preta
        r, g, b = color_list[0], color_list[1], color_list[2]
        gl.glColor3f(r, g, b)
        # Definir o número de linhas e colunas de quadriláteros como 3
        rows = rows_number
        cols = cols_number
        # Definir a largura e a altura da janela como 300
        width = 300
        height = 300
        # Definir o espaçamento entre os quadriláteros como 10% da largura e da altura da janela
        spacing = 0.1 * min(width, height)
        # Calcular o tamanho dos quadriláteros como a diferença entre a largura ou a altura da janela e o espaçamento total, dividida pelo número de linhas ou colunas
        size = (min(width, height) - (rows + 1) * spacing) / rows
        # Desenhar os quadriláteros em um loop aninhado
        for i in range(rows):
            for j in range(cols):
                # Calcular as coordenadas do canto inferior esquerdo do quadrilátero atual
                x = spacing + j * (size + spacing)
                y = spacing + i * (size + spacing)
                x = int(x)
                y = int(y)
                size = int(size)
                # Desenhar o quadrilátero atual usando vértices relativos ao canto inferior esquerdo
                gl.glBegin(gl.GL_QUADS)
                gl.glVertex2i(x, y)
                gl.glVertex2i(x + size, y)
                gl.glVertex2i(x + size, y + size)
                gl.glVertex2i(x, y + size)
                gl.glEnd()
        # Forçar a execução dos comandos de desenho
        gl.glFlush()
  def rectangle_grid():
    # Limpar a tela com a cor preta
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    # Definir as coordenadas dos vértices do retângulo
    x1 = 50
    y1 = 50
    x2 = 150
    y2 = 150
    # Definir o número de linhas e colunas da grade
    rows = 3
    cols = 3
    # Definir a cor do retângulo como azul
    gl.glColor3f(0.5,0.5,0.5)

    # Desenhar o retângulo usando vértices no plano cartesiano
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x2, y1)
    gl.glVertex2f(x2, y2)
    gl.glVertex2f(x1, y2)
    gl.glEnd()
    # Definir a cor da grade como branca
    gl.glColor3f(0.0, 0.0, 0.0)

    # Desenhar as linhas horizontais da grade usando vértices no plano cartesiano
    gl.glBegin(gl.GL_LINES)
    for i in range(rows + 1):
        y = y1 + i * (y2 - y1) / rows
        gl.glVertex2f(x1, y)
        gl.glVertex2f(x2, y)
    gl.glEnd()
    # Desenhar as linhas verticais da grade usando vértices no plano cartesiano
    gl.glBegin(gl.GL_LINES)
    for i in range(cols + 1):
        x = x1 + i * (x2 - x1) / cols
        gl.glVertex2f(x, y1)
        gl.glVertex2f(x, y2)
    gl.glEnd()
    # Forçar a execução dos comandos de desenho
    gl.glFlush()

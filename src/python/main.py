from primitives import *
from camera import Camera
from shapes import *
import matplotlib.pyplot as plt


def main():
    # Configuração da câmera
    camera_pos = Point3(2, 2, 4) 
    camera_mira = Point3(0, 0, -2)  
    camera_up = Vector3(0, 1, 0)
    distancia_tela = 1.0
    altura_resolucao = 500
    largura_resolucao = 500

    camera = Camera(camera_pos, camera_mira, camera_up, distancia_tela, altura_resolucao, largura_resolucao)

    # Definição dos vértices de uma pirâmide com base quadrada
    vertices = [
        Point3(-1, -1, -3),  # Base inferior esquerda
        Point3(1, -1, -3),   # Base inferior direita
        Point3(1, -1, -5),   # Base superior direita
        Point3(-1, -1, -5),  # Base superior esquerda
        Point3(0, 1, -4)     # Ponto do topo
    ]

    # Definição dos triângulos
    triangulos = [
        (0, 1, 4),  # Face frontal
        (1, 2, 4),  # Face lateral direita
        (2, 3, 4),  # Face traseira
        (3, 0, 4),  # Face lateral esquerda
        (0, 1, 2),  # Base inferior (metade 1)
        (2, 3, 0)   # Base inferior (metade 2)
    ]

    # Cores para cada triângulo
    cores = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.WHITE, Color.BLACK]

    # Normais de cada triângulo
    normais = []
    for t in triangulos:
        v0, v1, v2 = vertices[t[0]], vertices[t[1]], vertices[t[2]]
        normal = (v1 - v0).cross(v2 - v0).normalize()
        normais.append(normal)

    # Malha triangular da pirâmide
    piramide = TriangleMesh(len(triangulos), len(vertices), vertices, triangulos, normais, [], cores[0])

    # Plano de fundo
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))

    # Objetos na cena
    objetos = [piramide, plano]

    # Renderização
    imagem = camera.draw(objetos)

    # Salvamento e exibição da imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("image.png", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
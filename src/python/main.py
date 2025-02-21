from primitives import *
from camera import Camera
from shapes import *
import matplotlib.pyplot as plt


def main():
    # Configuração da câmera
    camera_pos = Point3(0, 0, 3)
    camera_mira = Point3(0, 0, -1)
    camera_up = Vector3(0, 1, 0)
    distancia_tela = 1.0
    altura_resolucao = 500
    largura_resolucao = 500

    camera = Camera(camera_pos, camera_mira, camera_up, distancia_tela, altura_resolucao, largura_resolucao)

    # Definição dos vértices (inclinação para o lado)
    vertices = [
        Point3(-0.5, -1, -3),  
        Point3(1.5, -1, -3), 
        Point3(0.5, 1, -3),    
        Point3(0, -1, -5),    
        Point3(-0.2, 2, -4)    
    ]

    # Definição dos triângulos (índices dos vértices)
    triangulos = [
        (0, 1, 2),  # Triângulo base
        (0, 1, 3),
        (1, 2, 4),
        (2, 0, 4),
        (0, 3, 4),
        (1, 3, 4)
    ]

    # Cores
    cores = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.WHITE, Color.BLACK]

    # Calcular as normais de cada triângulo
    normais = []
    for t in triangulos:
        v0, v1, v2 = vertices[t[0]], vertices[t[1]], vertices[t[2]]
        normal = (v1 - v0).cross(v2 - v0).normalize()
        normais.append(normal)

    # Criar a malha triangular
    piramide = TriangleMesh(len(triangulos), len(vertices), vertices, triangulos, normais, [], cores[0])

    # Plano de fundo
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))

    # Lista de objetos na cena
    objetos = [piramide, plano]

    # Renderizar a cena
    imagem = camera.draw(objetos)

    # Salvar a imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("image.png", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
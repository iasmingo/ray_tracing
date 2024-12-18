from primitives import *
from camera import Camera
from shapes import *
import matplotlib.pyplot as plt


def main():
    # Configuração da câmera
    camera_pos = Point3(0, 0, 0)
    camera_mira = Point3(0, 0, -1)
    distancia_tela = 1.0
    altura_resolucao = 500
    largura_resolucao = 500

    camera = Camera(altura_resolucao, largura_resolucao, distancia_tela, camera_pos, camera_mira)

    # Configuração dos objetos
    sphere1 = Sphere(Point3(0, 0, -3), 1, Color.RED)  # Sphere vermelha
    sphere2 = Sphere(Point3(2, 0, -4), 1, Color.GREEN)  # Sphere verde
    plane = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))  # Plane cinza

    objetos = [sphere1, sphere2, plane]

    # Renderizar a cena
    imagem = camera.draw(objetos)

    # Salvar a imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("render.png", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
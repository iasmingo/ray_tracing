from primitives import *
from camera import Camera
from shapes import *
import matplotlib.pyplot as plt


def main():
    # Configuração da câmera
    camera_pos = Point3(0, 0, 0)
    camera_mira = Point3(0, 0, -1)
    camera_up = Vector3(0, 1, 0)
    distancia_tela = 1.0
    altura_resolucao = 500
    largura_resolucao = 500

    camera = Camera(camera_pos, camera_mira, camera_up, distancia_tela, altura_resolucao, largura_resolucao)

    #Cena inicial
    # esfera1 = Sphere(Point3(0, 0, -3), 1, Color.RED) 
    # esfera2 = Sphere(Point3(2, 0, -4), 1, Color.GREEN)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5)) 

    # objetos = [esfera1, esfera2, plano]

    mesh = TriangleMesh(1, 3, [Point3(0, 0, -3), Point3(1, -1, -4), Point3(2, 0, -3)], [(0, 1, 2)], [Vector3(0, -2, 2)], [], Color.RED)
    # esfera1 = Sphere(Point3(0, 0, -3), 1, Color.RED)
    objetos = [mesh, plano]
    #objetos = [esfera1]
    # Renderizar a cena
    imagem = camera.draw(objetos)

    # Salvar a imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("image.png", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
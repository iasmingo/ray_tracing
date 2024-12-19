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

    # Cena inicial
    esfera1 = Sphere(Point3(0, 0, -3), 1, Color.RED) 
    esfera2 = Sphere(Point3(2, 0, -4), 1, Color.GREEN)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5)) 

    objetos = [esfera1, esfera2, plano]

    # Esfera vermelha na frente da esfera verde
    esfera1 = Sphere(Point3(0, 0, -3), 1, Color.RED)  
    esfera2 = Sphere(Point3(0, 0, -6), 1, Color.GREEN)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))  

    objetos = [esfera1, esfera2, plano]

    # Esferas lado a lado
    esfera1 = Sphere(Point3(-1.5, 0, -3), 1, Color.RED)  
    esfera2 = Sphere(Point3(1.5, 0, -3), 1, Color.GREEN)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))  

    objetos = [esfera1, esfera2, plano]

    # Esferas parcialmente sobrepostas
    esfera1 = Sphere(Point3(0, 0, -3), 1, Color.RED)  
    esfera2 = Sphere(Point3(0.5, 0, -3.5), 1, Color.GREEN)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))

    objetos = [esfera1, esfera2, plano]

    # Esfera flutuante acima do plano
    esfera1 = Sphere(Point3(0, 1, -3), 1, Color.RED)  
    plano = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5))  

    objetos = [esfera1, plano]

    # Plano vertical como parede
    plano = Plane(Point3(0, 0, -5), Vector3(0, 0, 1), Color(0.8, 0.8, 0.2)) 
    objetos = [plano]

    # Plano horizontal e plano vertical (chão e parede)
    plano_chao = Plane(Point3(0, -1, 0), Vector3(0, 1, 0), Color(0.5, 0.5, 0.5)) 
    plano_parede = Plane(Point3(0, 0, -5), Vector3(0, 0, 1), Color(0.8, 0.8, 0.2)) 
    objetos = [plano_chao, plano_parede]

    # Plano inclinado
    plano = Plane(Point3(0, -1, 0), Vector3(1, 1, 0).normalize(), Color(0.2, 0.6, 0.8)) 
    objetos = [plano]

    # Renderizar a cena
    imagem = camera.draw(objetos)

    # Salvar a imagem
    plt.imshow(imagem)
    plt.axis('off')
    plt.savefig("image.png", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
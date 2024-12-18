from primitives import *
from shapes import Color, Intersectable

class Camera:
    """
    ### Camera
    Câmera móvel
    
    #### Atributos:
        - position (Point3): posição da câmera
        - target (Point3): posição da tela
        - u (Vector3): Vetor que aponta para cima da câmera
        - v (Vector3): Vetor que aponta para a frente da câmera
        - w (Vector3): Vetor que aponta para a direita da câmera
        - d (cython.double): distacia de position para target
        - height (cython.int): altura da tela em pixels
        - width (cython.int): largura da tela em pixels
    """
    def __init__(self, height: int, width: int, distance: float, position: Point3, target: Point3 = None):
        self.position = position
        if target is None:
            self.target = position.translate(Vector3(0, 0, 10))
        else:
            self.target = target

        self.v: Vector3 = position.to(self.target)
        self.d: float = distance # = self.v.norm()
        self.v = self.v.normalized()
        self.w = -(self.v).cross(Vector3.j)
        self.u = self.v.cross(self.w)
        self.height = height
        self.width = width

        # Dimensões dos pixels
        self.pixel_h = 1 / width
        self.pixel_v = 1 / height

    def __str__(self):
        return (
            "Camera:\n"
            f"  Position: {self.position}\n"
            f"  Target: {self.target}"
        )

    def translate(self, v: Vector3) -> None:
        """
        Executa uma tranformação de translação sobre a camera
        """
        self.position = self.position.translate(v)
        self.target = self.target.translate(v)

    def calculate_point_screen(self, i, j):
        """
        Calcula a posição do centro do pixel (i, j) na tela.
        i: linha do pixel (0 é o pixel mais alto)
        j: coluna do pixel (0 é o pixel mais à esquerda)
        Retorna um ponto 3D na tela no espaço do mundo.
        """
        if not (0 <= i < self.height and 0 <= j < self.width):
            raise ValueError("Índices do pixel fora do intervalo da resolução da tela.")

        # Centro da tela no espaço do mundo
        center = self.position.translate(- self.v.scale(self.d))

        # Vetor para o pixel na direção horizontal e vertical
        delta_h = self.w.scale((j - (self.width - 1) / 2) * self.pixel_h)
        delta_v = self.u.scale(((self.height - 1) / 2 - i) * self.pixel_v)

        return center.translate(delta_h).translate(delta_v)


    def draw(self, objects):
        width = self.width
        height = self.height

        image = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                pixel_pos = self.calculate_point_screen(i, j)
                direction = (self.position.to(pixel_pos).normalized())

                pixel_color: Color = Color.BLACK
                min_dist = float('inf')

                for obj in objects:
                    distance = obj.intersects(self.position, direction)

                    if distance is not None and distance < min_dist:
                        min_dist = distance
                        pixel_color = obj.color

                image[i][j] = (pixel_color.r, pixel_color.g, pixel_color.b)

        return image
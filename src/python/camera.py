from primitives import *
from shapes import Color, Intersectable


class Camera:
    def __init__(self, 
                 position: Point3, 
                 target: Point3, 
                 vector_up: Vector3, 
                 dist_screen: float, 
                 height_resolution: int, 
                 width_resolution: int):

        if vector_up.magnitude() == 0:
            raise ValueError("O vetor para cima (vector_up) não pode ser nulo.")

        self.position = position
        self.target = target
        self.vector_up = vector_up.normalize()
        self.dist_screen = dist_screen
        self.height_resolution = height_resolution
        self.width_resolution = width_resolution

        # Vetores ortonormais
        self.w = (self.position - self.target).normalize()
        self.u = self.vector_up.cross(self.w).normalize()
        self.v = self.w.cross(self.u).normalize()

        # Dimensões dos pixels
        self.pixel_size_h = 1 / width_resolution
        self.pixel_size_v = 1 / height_resolution

    def __str__(self):
        return (
            "Camera:\n"
            f"  Position: {self.position}\n"
            f"  Target: {self.target}"
        )

    def calculate_point_screen(self, i, j):
        """
        Calcula a posição do centro do pixel (i, j) na tela.
        i: linha do pixel (0 é o pixel mais alto)
        j: coluna do pixel (0 é o pixel mais à esquerda)
        Retorna um ponto 3D na tela no espaço do mundo.
        """
        if not (0 <= i < self.height_resolution and 0 <= j < self.width_resolution):
            raise ValueError("Índices do pixel fora do intervalo da resolução da tela.")

        # Centro da tela no espaço do mundo
        screen_center = self.position - self.w * self.dist_screen

        # Vetor para o pixel na direção horizontal e vertical
        delta_h = self.u * (j - (self.width_resolution - 1) / 2) * self.pixel_size_h
        delta_v = self.v * ((self.height_resolution - 1) / 2 - i) * self.pixel_size_v

        return screen_center + delta_h + delta_v

    def draw(self, objects):
        width = self.width_resolution
        height = self.height_resolution

        image = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                pixel_pos = self.calculate_point_screen(i, j)
                direction = (pixel_pos - self.position).normalize()

                pixel_color: Color = Color.BLACK
                min_dist = float('inf')

                for obj in objects:
                    distance = obj.intersects(self.position, direction)

                    if distance is not None and distance < min_dist:
                        min_dist = distance
                        pixel_color = obj.color

                image[i][j] = (pixel_color.r, pixel_color.g, pixel_color.b)

        return image
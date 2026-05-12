from clases_libro.libro import Libro
from clases_prestamo.prestamo import Prestamo

class CopiaLibro:
    def __init__(self, codigo_copia: int, fecha_ingreso: str, valoracion: float, estado: str, libro: Libro, prestamos: list[Prestamo]):
        self.codigo_copia = codigo_copia
        self.fecha_ingreso = fecha_ingreso
        self.valoracion = valoracion
        self.estado = estado
        self.libro = libro
        self.prestamos = prestamos
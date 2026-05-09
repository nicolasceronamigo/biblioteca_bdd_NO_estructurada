from clases_libro.libro import Libro
from clases_prestamo.prestamo import Prestamo

class CopiaLibro:
    def __init__(self, id_copia: str, fecha_ingreso: str, estado: str, valoracion: float, libro: Libro, historial_prestamos: list[Prestamo]):
        self.__id_copia = id_copia
        self.__fecha_ingreso = fecha_ingreso
        self.__estado = estado
        self.__valoracion = valoracion
        self.__libro = libro
        self.__historial_prestamos = historial_prestamos
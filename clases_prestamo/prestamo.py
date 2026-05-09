from clases_prestamo.usuario import Usuario 

class Prestamo:
    def __init__(self, id_prestamo: str, usuario: Usuario, fecha_prestamo: str, fecha_limite: str, fecha_devolucion: str, estado: str) -> None:
        self.__id_prestamo = id_prestamo
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_limite = fecha_limite
        self.__fecha_devolucion = fecha_devolucion
        self.__estado = estado
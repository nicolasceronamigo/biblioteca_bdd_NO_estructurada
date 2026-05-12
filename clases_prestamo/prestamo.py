from clases_prestamo.usuario import Usuario 

class Prestamo:
    def __init__(self, usuario: Usuario, fecha_prestamo: str, fecha_limite: str, fecha_devolucion: str, estado: str) -> None:
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_limite = fecha_limite
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado
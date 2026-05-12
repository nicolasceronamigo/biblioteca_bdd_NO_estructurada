from clases_libro.autor import Autor
from clases_libro.edicion import Edicion

class Libro:
    def __init__(self, titulo: str, anno: int, categoria: str, autor: Autor, edicion: Edicion):
        self.titulo = titulo
        self.anno = anno
        self.categoria = categoria
        self.autor = autor
        self.edicion = edicion


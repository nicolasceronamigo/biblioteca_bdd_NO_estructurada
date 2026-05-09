from clases_libro.autor import Autor
from clases_libro.edicion import Edicion

class Libro:
    def __init__(self, titulo: str, anno: int, categorias: list[str], autores: list[Autor], edicion: Edicion):
        self.__titulo = titulo
        self.__anno = anno
        self.__categorias = categorias
        self.__autor = autores
        self.__edicion = edicion


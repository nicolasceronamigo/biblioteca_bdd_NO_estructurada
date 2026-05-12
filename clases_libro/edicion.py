from clases_libro.editorial import Editorial

class Edicion:
    def __init__(self, numero: int, anno: int, isbn: str, idioma: str, formato: str, editorial: Editorial):
        self.numero = numero
        self.anno = anno
        self.isbn = isbn
        self.idioma = idioma
        self.formato = formato
        self.editorial = editorial
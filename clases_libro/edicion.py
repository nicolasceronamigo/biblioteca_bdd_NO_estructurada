from editorial import Editorial

class Edicion:
    def __init__(self, numero: int, anno: int, isbn: str, idioma: str, formato: str, editorial: Editorial):
        self.__numero = numero
        self.__anno = anno
        self.__isbn = isbn
        self.__idioma = idioma
        self.__formato = formato
        self.__editorial = editorial
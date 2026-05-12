from clases_menu.menu import Menu

from herramientas.herramientas import mostrar_elementos

from pprint import pprint

class MenuListar(Menu):
    def mostrar_copias(self):
        documentos = list(self.coleccion.find({}))
        mostrar_elementos(documentos)           
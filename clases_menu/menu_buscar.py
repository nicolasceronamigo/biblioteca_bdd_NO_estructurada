from clases_menu.menu import Menu

from herramientas.herramientas import mostrar_elementos

from pprint import pprint
from datetime import datetime


class MenuBuscar(Menu):
    def buscar_valoracion_minima(self):
        try:
            valoracion = float(input("Ingrese la valoración mínima buscada: "))
            documentos = list(self.coleccion.find({"valoracion": {"$gte": valoracion}}, {"_id": 0, "codigo_copia": 1, "libro.titulo": 1, "valoracion": 1}))
            mostrar_elementos(documentos)
        except:
            print("Error. La valoración tiene que ser un número decimal.")

    def buscar_antes_anno(self):
        try:
            anno = int(input("Ingrese el año máximo deseado: "))
            documentos = list(self.coleccion.find({"libro.anio_publicacion": {"$lte": anno}}, {"_id": 0, "codigo_copia": 1, "libro.titulo": 1, "libro.anio_publicacion": 1}))
            mostrar_elementos(documentos)
        except:
            print("Error. El año tiene que ser un número entero.")
    
    def buscar_coincidencia_nombre_copia(self):
        nombre = input("Ingrese la palabra clave para el titulo del libro: ")
        documentos = list(self.coleccion.find({"libro.titulo": {"$regex": nombre, "$options": "i"}}, {"_id": 0, "codigo_copia": 1, "libro.titulo": 1}))
        mostrar_elementos(documentos)
    
    def buscar_rango_fecha_prestamo(self):
        fecha_inicial = input("Ingrese desde que fecha (inclusive) quiere buscar en formato YYYY-MM-DD: ")
        fecha_final = input("Ingrese hasta que fecha (no inclusive) quiere buscar en formato YYYY-MM-DD: ")
        try:
            date_fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d")
            date_fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
            documentos = list(self.coleccion.find({"prestamos": {"$elemMatch": {"fecha_prestamo": {"$gte": date_fecha_inicial, "$lt": date_fecha_final}}}}, {"_id": 0, "codigo_copia": 1, "libro.titulo": 1, "prestamos.fecha_prestamo": 1}))
            mostrar_elementos(documentos)
        except:
            print("Error. Formato incorrecto de fecha.")
    
    def buscar_copias_usuario(self):
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        documentos = list(self.coleccion.find({"prestamos.usuario.nombre": nombre_usuario}, {"_id": 0, "codigo_copia": 1, "libro.titulo": 1, "prestamos.usuario.nombre": 1}))
        mostrar_elementos(documentos)
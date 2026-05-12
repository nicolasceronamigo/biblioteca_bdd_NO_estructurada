from pymongo import DESCENDING

from clases_menu.menu import Menu
from clases_libro.libro import Libro
from clases_libro.autor import Autor
from clases_libro.editorial import Editorial
from clases_libro.edicion import Edicion
from clases_prestamo.prestamo import Prestamo
from clases_prestamo.usuario import Usuario
from clases_libro.copia_libro import CopiaLibro

from datetime import datetime, timedelta
from herramientas.herramientas import to_dicc


class MenuRegistrar(Menu):
    def crear_copia(self):
        ultimo_codigo_copia = self.coleccion.find_one(sort = [("codigo_copia", DESCENDING)])["codigo_copia"]
        codigo_copia = ultimo_codigo_copia + 1
        fecha_ingreso = datetime.now()
        valoracion = 0
        estado = "Disponible"

        titulo = input("Ingrese el título del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        try:
            anno_publicacion = int(input("Ingrese el año de publicación del libro: "))
        except:
            print("Error, el año de publicación debe ser un número entero")
            return
        nombre_autor = input("Ingrese el nombre del autor del libro: ")
        nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")
        nombre_editorial = input("Ingrese la editorial del libro: ")
        pais_editorial = input("Ingrese el pais de la editorial: ")
        editorial = Editorial(nombre_editorial, pais_editorial)
        try:
            numero_edicion = int(input("Ingrese el número de la edición: "))
        except:
            print("Error, el número de la edición debe ser un número entero")
            return
        try:
            anio_edicion = int(input("Ingrese el año de la edición: "))
        except:
            print("Error, el año de la edición debe ser un número entero")
            return
        formato = input("Ingrese formato de la edición: ")
        idioma = input("Ingrese el idioma de la edición: ")
        isbn = input("Ingrese el isbn de la edición: ")
        edicion = Edicion(numero_edicion, anio_edicion, isbn, idioma, formato, editorial)
        autor = Autor(nombre_autor, nacionalidad_autor)
        libro = Libro(titulo, anno_publicacion, categoria, autor, edicion)
        try:
            num_prestamos = int(input("Ingrese el número de préstamos: "))
        except:
            print("Error, el número de préstamos debe ser un número entero")
            return
        prestamos = []
        for n in range(num_prestamos):
            rut_usuario = input("Ingrese el rut del usuario: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(rut_usuario, nombre_usuario)
            fecha_prestamo = input("Ingrese la fecha del prestamo en formato YYYY-MM-DD: ")
            try:
                date_fecha_prestamo = datetime.strptime(fecha_prestamo, "%Y-%m-%d")
            except:
                print("Error. Formato incorrecto de fecha.")
                return 
            fecha_limite = date_fecha_prestamo + timedelta(days = 7)
            fecha_devolucion = input("Ingrese la fecha de devolucion en formato YYYY-MM-DD: ")
            try:
                date_fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d")
            except:
                print("Error. Formato incorrecto de fecha.")
                return
            estado = input("Ingrese el estado de la devolución: ")
            prestamo = Prestamo(usuario, date_fecha_prestamo, fecha_limite, date_fecha_devolucion, estado)
            prestamos.append(prestamo)
        copia_libro = CopiaLibro(codigo_copia, fecha_ingreso, valoracion, estado, libro, prestamos)
        return to_dicc(copia_libro)
    
    def registrar_copia(self):
        copia = self.crear_copia()
        self.coleccion.insert_one(copia)

    def crear_copias(self):
        try:
            num_copias = int(input("Ingrese la cantidad de copias a registrar: "))
        except:
            print("Error. Solo puede ingresar un numero entero")
            return
        arr_copias = []
        for num in range(num_copias):
            arr_copias.append(self.crear_copia())
        return arr_copias

    def registrar_copias(self):
        copias = self.crear_copias()
        self.coleccion.insert_many(copias)
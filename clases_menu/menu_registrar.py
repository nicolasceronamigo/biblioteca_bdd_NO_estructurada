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
    def crear_copia(self, cod = 0):
        ultimo_documento = self.coleccion.find_one(sort = [("codigo_copia", DESCENDING)])
        if ultimo_documento and cod == 0:
            codigo_copia = ultimo_documento["codigo_copia"] + 1
        elif cod != 0:
            codigo_copia = cod
        else:
            codigo_copia = 1
        fecha_ingreso = datetime.now()
        try:
            valoracion = float(input("Ingrese la valoración de la copia: "))
        except:
            print("Error. La valoración debe ser un número decimal. \n")
            return
        #estado = input("Ingrese el estado de la copia: ")
        titulo = input("Ingrese el título del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        try:
            anno_publicacion = int(input("Ingrese el año de publicación del libro: "))
        except:
            print("Error, el año de publicación debe ser un número entero. \n")
            return
        nombre_autor = input("Ingrese el nombre del autor del libro: ")
        nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")
        nombre_editorial = input("Ingrese la editorial del libro: ")
        pais_editorial = input("Ingrese el pais de la editorial: ")
        editorial = Editorial(nombre_editorial, pais_editorial)
        try:
            numero_edicion = int(input("Ingrese el número de la edición: "))
        except:
            print("Error, el número de la edición debe ser un número entero. \n")
            return
        try:
            anio_edicion = int(input("Ingrese el año de la edición: "))
        except:
            print("Error, el año de la edición debe ser un número entero. \n")
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
            print("Error, el número de préstamos debe ser un número entero. \n")
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
                print("Error. Formato incorrecto de fecha.\n")
                return 
            fecha_limite = date_fecha_prestamo + timedelta(days = 7)
            fecha_devolucion = input("Ingrese la fecha de devolucion en formato YYYY-MM-DD: ")
            try:
                date_fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d")
            except:
                print("Error. Formato incorrecto de fecha.\n")
                return
            #estado_prestamo = input("Ingrese el estado de la devolución: ")
            if date_fecha_devolucion <= fecha_limite:
                estado_prestamo = "Devuelto"
            elif date_fecha_devolucion > fecha_limite:
                estado_prestamo = "Atrasado"
            elif date_fecha_devolucion > datetime.now():
                print("Error. La fecha de devolución tiene que ser anterior a la fecha actual.\n")
                return
            prestamo = Prestamo(usuario, date_fecha_prestamo, fecha_limite, date_fecha_devolucion, estado_prestamo)
            prestamos.append(prestamo)
        estado = "Disponible"
        copia_libro = CopiaLibro(codigo_copia, fecha_ingreso, valoracion, estado, libro, prestamos)
        return to_dicc(copia_libro)
    
    def registrar_copia(self):
        copia = self.crear_copia()
        if copia:
            self.coleccion.insert_one(copia)
            print("Copia registrada correctamente. \n")
        else:
            print("Error al crear la copia. No se creo la copia.\n")

    def crear_copias(self):
        try:
            num_copias = int(input("Ingrese la cantidad de copias a registrar: "))
        except:
            print("Error. Solo puede ingresar un numero entero.\n")
            return
        arr_copias = []
        ultimo_documento = self.coleccion.find_one(sort = [("codigo_copia", DESCENDING)])
        ultimo_codigo = ultimo_documento["codigo_copia"]
        for num in range(num_copias):
            ultimo_codigo += 1
            copia = self.crear_copia(ultimo_codigo)
            if copia:
                arr_copias.append(copia)
        return arr_copias

    def registrar_copias(self):
        copias = self.crear_copias()
        if copias:
            self.coleccion.insert_many(copias)
            print("Copias registradas correctamente.\n")
        else:
            print("Error al crear las copias. No se creo ninguna copia.\n")
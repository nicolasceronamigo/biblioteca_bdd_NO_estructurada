from pymongo import MongoClient, DESCENDING

from clases_menu.menu import Menu
from clases_menu.menu_registrar import MenuRegistrar
from clases_menu.menu_listar import MenuListar
from clases_menu.menu_buscar import MenuBuscar
from clases_menu.menu_editar import MenuEditar
from clases_menu.menu_eliminar import MenuEliminar

from clases_libro.copia_libro import CopiaLibro

from datetime import datetime
from pprint import pprint

client = MongoClient('mongodb+srv://nicolasceronamigo_db_user:RMBUKyPWUzuTsIrC@cluster0.qfeimjz.mongodb.net/')
db = client['biblioteca']
coleccion = db['copiasLibros']

menu_principal = Menu("Biblioteca - Menu Principal", coleccion)

menu_registrar = MenuRegistrar("Biblioteca - Registrar Copia", coleccion)
menu_listar = MenuListar("Biblioteca - Listar Copias", coleccion)
menu_buscar = MenuBuscar("Biblioteca - Buscar Copias", coleccion)
menu_editar = MenuEditar("Biblioteca - Editar Copia", coleccion)
menu_eliminar = MenuEliminar("Biblioteca - Eliminar Copia", coleccion)

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Registrar Copia", menu_registrar.ciclo_menu)
menu_principal.agregar_opcion(2, "Listar Copias", menu_listar.ciclo_menu)
menu_principal.agregar_opcion(3, "Buscar Copia", menu_buscar.ciclo_menu)
menu_principal.agregar_opcion(4, "Editar Copia", menu_editar.ciclo_menu)
menu_principal.agregar_opcion(5, "Eliminar Copia", menu_eliminar.ciclo_menu)

menu_registrar.agregar_opcion(0, "Salir", menu_registrar.salir)
menu_registrar.agregar_opcion(1, "Registrar una Copia", menu_registrar.registrar_copia)
menu_registrar.agregar_opcion(2, "Registrar muchas Copias", menu_registrar.registrar_copias)

menu_listar.agregar_opcion(0, "Salir", menu_listar.salir)
menu_listar.agregar_opcion(1, "Listar todas las copias", menu_listar.mostrar_copias)

menu_buscar.agregar_opcion(0, "Salir", menu_buscar.salir)
menu_buscar.agregar_opcion(1, "Buscar copias publicadas antes de un año", menu_buscar.buscar_antes_anno)
menu_buscar.agregar_opcion(2, "Buscar copias por valoración mínima", menu_buscar.buscar_valoracion_minima)
menu_buscar.agregar_opcion(3, "Buscar copia por coincidencia en título", menu_buscar.buscar_coincidencia_nombre_copia)
menu_buscar.agregar_opcion(4, "Buscar copia por rango de préstamo", menu_buscar.buscar_rango_fecha_prestamo)
menu_buscar.agregar_opcion(5, "Buscar copias prestadas a un usuario", menu_buscar.buscar_copias_usuario)

menu_editar.agregar_opcion(0, "Salir", menu_editar.salir)
menu_editar.agregar_opcion(1, "Prestar copia", menu_editar.prestar_copia)
menu_editar.agregar_opcion(2, "Devolver copia", menu_editar.devolver_copia)
menu_editar.agregar_opcion(3, "Cambiar estado", menu_editar.cambiar_estado)

menu_eliminar.agregar_opcion(0, "Salir", menu_eliminar.salir)
menu_eliminar.agregar_opcion(1, "Eliminar una copia", menu_eliminar.eliminar_copia)


menu_principal.ciclo_menu()

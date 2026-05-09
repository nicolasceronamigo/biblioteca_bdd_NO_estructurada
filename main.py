from pymongo import MongoClient

client = MongoClient('mongodb+srv://nicolasceronamigo_db_user:RMBUKyPWUzuTsIrC@cluster0.qfeimjz.mongodb.net/')
db = client['biblioteca']
coleccion = db['copiasLibros']


from clases_menu.menu import Menu
from clases_menu.menu_registrar import MenuRegistrar
from clases_menu.menu_listar import MenuListar
from clases_menu.menu_buscar import MenuBuscar
from clases_menu.menu_editar import MenuEditar
from clases_menu.menu_eliminar import MenuEliminar

from clases_libro.copia_libro import CopiaLibro


menu_principal = Menu("Biblioteca - Menu Principal")
menu_crear = MenuRegistrar("Biblioteca - Menu Principal")
menu_listar = MenuListar("Biblioteca - Menu Principal")
menu_buscar = MenuBuscar("Biblioteca - Menu Principal")
menu_actualizar = MenuEditar("Biblioteca - Menu Principal")
menu_eliminar = MenuEliminar("Biblioteca - Menu Principal")

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Crear Copia", menu_crear.ciclo_menu)
menu_principal.agregar_opcion(2, "Listar Copias", menu_listar.ciclo_menu)
menu_principal.agregar_opcion(3, "Buscar Copia", menu_buscar.ciclo_menu)
menu_principal.agregar_opcion(4, "Actualizar Copia", menu_actualizar.ciclo_menu)
menu_principal.agregar_opcion(5, "Eliminar Copia", menu_eliminar.ciclo_menu)


print(coleccion.find_one({"codigo_copia": "COPLIB-0001"}))
from clases_menu.menu import Menu

from pprint import pprint

class MenuEliminar(Menu):
    def eliminar_copia(self):
        try:
            codigo_copia = int(input("Ingrese el codigo de la copia a eliminar: "))
        except:
            print("Error. El codigo debe ser un número entero")
            return
        copia_eliminar = self.coleccion.find_one({"codigo_copia": codigo_copia})
        if copia_eliminar:
            print("Copia a eliminar: ")
            pprint(copia_eliminar)
            opcion = input("Confirme si desea eliminar la copia [y/n]: ")
            if opcion == "y":
                self.coleccion.delete_one({"codigo_copia": codigo_copia})
                print("Copia borrada con éxito")
            elif opcion == "n":
                print("Operación abortada.")
            else:
                print("Error. Solo se aceptan las opciones [y] o [n]")
        else:
            print("No hay copias con ese codigo")

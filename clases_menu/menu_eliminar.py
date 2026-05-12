from clases_menu.menu import Menu

from pprint import pprint

class MenuEliminar(Menu):
    def eliminar_copia(self):
        try:
            codigo_copia = int(input("Ingrese el codigo de la copia a eliminar: "))
        except:
            print("Error. El codigo debe ser un número entero.\n")
            return
        copia_eliminar = self.coleccion.find_one({"codigo_copia": codigo_copia})
        if copia_eliminar:
            print("Copia a eliminar: \n")
            pprint(copia_eliminar, sort_dicts = False)
            opcion = input("Confirme si desea eliminar la copia [y/n]: ")
            if opcion == "y":
                self.coleccion.delete_one({"codigo_copia": codigo_copia})
                print("Copia borrada con éxito.\n")
            elif opcion == "n":
                print("Operación abortada.\n")
            else:
                print("Error. Solo se aceptan las opciones [y] o [n].\n")
        else:
            print(f"No hay copias con codigo {codigo_copia}.\n")

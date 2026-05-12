
class Menu:
    def __init__(self, titulo: str, coleccion):
        self.titulo = titulo
        self.coleccion = coleccion
        self.dicc_opciones = {}
    
    def agregar_opcion(self, num_opcion: int, txt_opcion: str, func_opcion):
        self.dicc_opciones[str(num_opcion)] = {"txt_opcion": txt_opcion, "func_opcion": func_opcion}
    
    def selecc_opcion(self):
        num_opcion = input("Seleccione una opción digitando el número: ")
        if num_opcion not in self.dicc_opciones.keys():
            print(f"Opcion {num_opcion} no existe. Intente nuevamente.")
            return self.selecc_opcion()
        funcion = self.dicc_opciones[num_opcion]["func_opcion"]()
        return funcion

    def mostrar_menu(self):
        menu = self.titulo + "\n\n"
        for key_opcion in self.dicc_opciones.keys():
            menu += f"({key_opcion}) {self.dicc_opciones[key_opcion]["txt_opcion"]} \n"
        return menu
    
    def salir(self):
        return False
    
    def ciclo_menu(self):
        seguir = True
        while seguir:
            print("----------------------------------------------------------------------------------------")
            print(self.mostrar_menu())
            print("----------------------------------------------------------------------------------------")
            seguir = self.selecc_opcion()
            print("\n")
            if seguir == None:
                seguir = True
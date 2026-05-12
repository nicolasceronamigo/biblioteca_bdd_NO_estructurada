from clases_menu.menu import Menu

from pprint import pprint

from datetime import datetime, timedelta

class MenuEditar(Menu):
    def prestar_copia(self):
        try:
            codigo_copia = int(input("Ingrese el código de la copia: "))
        except:
            print("Error. El codigo de la copia es un número entero.\n")
            return
        documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
        if documento:
            if documento["estado"] != "Disponible":
                print(f"Copia codigo {codigo_copia} no se encuentra disponible.\n")
            else:
                print("Documento a prestar: \n")
                pprint(documento, sort_dicts = False)
                rut_usuario = input("Ingrese el rut del usuario: ")
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                fecha_prestamo = datetime.now()
                fecha_limite = fecha_prestamo + timedelta(days = 7)
                self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"estado": "Prestado"}})
                usuario = {"rut": rut_usuario, "nombre": nombre_usuario}
                prestamo = {"usuario": usuario, "fecha_prestamo": fecha_prestamo, "fecha_limite": fecha_limite, "estado": "Prestado"}
                self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$push": {"prestamos": prestamo}})
                nuevo_documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
                print("Prestamo registrado: \n")
                pprint(nuevo_documento, sort_dicts = False)
        else:
            print(f"No se encontró la copia de código {codigo_copia}.\n")

    def devolver_copia(self):
        try:
            codigo_copia = int(input("Ingrese el código de la copia: "))
        except:
            print("Error. El codigo de la copia es un número entero.\n")
            return
        documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
        if documento:
            if documento["estado"] == "Disponible":
                print(f"Copia codigo {codigo_copia} no se ha prestado. \n")
                return
            else:
                print("Documento a devolver: \n")
                pprint(documento, sort_dicts = False)
                fecha_devolucion = datetime.now()
                ultimo_prestamo = documento["prestamos"][-1]
                fecha_prestamo = ultimo_prestamo["fecha_prestamo"]
                fecha_limite = ultimo_prestamo["fecha_limite"]
                if fecha_devolucion > fecha_limite:
                    self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"prestamos.$[prest].estado": "Atrasado"}}, array_filters = [{"prest.fecha_prestamo": fecha_prestamo}])
                elif fecha_devolucion <= fecha_limite:
                    self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"prestamos.$[prest].estado": "Devuelto"}}, array_filters = [{"prest.fecha_prestamo": fecha_prestamo}])
                self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"estado": "Disponible"}})
                self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"prestamos.$[prest].fecha_devolucion": fecha_devolucion}}, array_filters = [{"prest.fecha_prestamo": fecha_prestamo}], upsert = True)
                nuevo_documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
                print("Prestamo registrado: \n")
                pprint(nuevo_documento, sort_dicts = False)
        else:
            print(f"No se encontró la copia de código {codigo_copia}.\n")

    def cambiar_estado(self):
        try:
            codigo_copia = int(input("Ingrese el código de la copia: "))
        except:
            print("Error. El codigo de la copia es un número entero.\n")
            return
        documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
        if documento:
            print("Documento a cambiar: \n")
            pprint(documento, sort_dicts = False)
            nuevo_estado = input("Ingrese el nuevo estado de la copia: ")
            self.coleccion.update_one({"codigo_copia": codigo_copia}, {"$set": {"estado": nuevo_estado}})
            nuevo_documento = self.coleccion.find_one({"codigo_copia": codigo_copia})
            print("Documento cambiado: \n")
            pprint(nuevo_documento, sort_dicts = False)
        else:
            print(f"No se encontró la copia de código {codigo_copia}.\n")
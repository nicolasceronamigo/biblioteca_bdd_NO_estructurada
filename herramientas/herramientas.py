from pprint import pprint

def to_dicc(objeto):
    dicc = {}
    for k, v in objeto.__dict__.items():
        try:
            if type(v) == list:
                arr = []
                for obj in v:
                    arr.append(to_dicc(obj))
                dicc[k] = arr
            else:
                dicc[k] = to_dicc(v)
        except:
            dicc[k] = v
    return dicc

def mostrar_elementos(lista):
    if lista:
        for elemento in lista:
            print("----------------------------------------------------------------------------------------")
            pprint(elemento, sort_dicts = False)
    else:
        print("No se encontraron elementos")

'''
def mostrar_objeto(objeto):
        resultado = ""
        if type(objeto) == dict:
            resultado += "{\n"
            for k, v in objeto.items():
                resultado += f"{k}: {mostrar_objeto(v)}"
            resultado += "}\n"
        elif type(objeto) == list:
            resultado += "[\n"
            for elem in objeto:
                resultado += f"{mostrar_objeto(elem)}"
            resultado += "]\n"
        else:
            resultado += str(objeto) + ", \n"
        return resultado
'''

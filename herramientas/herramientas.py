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
        print("No se encontraron elementos.\n")

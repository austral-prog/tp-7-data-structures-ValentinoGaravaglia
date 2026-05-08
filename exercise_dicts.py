def create_inventory(items):

    diccionario = {}

    for valor in items:
        diccionario[valor] = items.count(valor)

    return diccionario



def add_items(inventario, items):

    for valor in items:
        if valor in inventario:
            inventario[valor] += 1
        else:
            inventario[valor] = 1

    return inventario

def decrement_items(inventario, items):

    for valor in items:
        if valor in inventario:
            if inventario[valor]>0:
                inventario[valor] -= 1

    return inventario



def remove_item(inventario, item):

    if item in inventario:
        del inventario[item]

    return inventario

def list_inventory(inventario):

    lista = []

    for valor in inventario:
        if inventario[valor]>0:
            lista.append((valor, inventario[valor]))

    return lista


def find_max_value(diccionario):

    if diccionario == {}:
        return ""

    numeros = diccionario.values()
    maximo = max(numeros)

    for clave in diccionario:
        if diccionario[clave] == maximo:
            return clave

def reverse_dict(diccionario):

    inv_diccionario = {}

    for clave in diccionario:
        valor = diccionario[clave]
        if valor in inv_diccionario:
            inv_diccionario[valor] = inv_diccionario[valor] + clave
        else:
            inv_diccionario[valor] = clave
    return inv_diccionario

def word_frequency(palabras):

    if palabras == []:
        return {}

    diccionario = {}
    for valor in palabras:
        diccionario[valor] = palabras.count(valor)

    return diccionario


def find_biggest_expense(gastos):

    avg = 0
    valor = ""

    for clave in gastos:
        lista = gastos[clave]
        if (sum(lista) / len(lista)) > avg:
            avg = sum(lista) / len(lista)
            valor = clave
    return valor

def sum_expenses(gastos):

    for clave in gastos:
        lista = gastos[clave]
        gastos[clave] = sum(lista)

    return gastos


def sum_expenses_by_type(gastos):

    result = {}

    for clave in gastos:
        for tipo, monto in gastos[clave]:
            if tipo in result:
                result[tipo] += monto
            else:
                result[tipo] = monto

    return result
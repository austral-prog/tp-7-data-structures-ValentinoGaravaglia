def get_coordinate(registro):

    tesoro, coordenada = registro
    return coordenada

def convert_coordinate(coordenada):

    return (coordenada[0], coordenada[-1])

def create_record(registro_azara, registro_rui):

    a, b = registro_rui[1]
    c = a + b

    if registro_azara[-1] == c:
        return registro_azara + registro_rui
    else:
        return "not a match"



def sum_tuple(numeros):

    result = 0

    for num in numeros:
        result += num

    return result


def count_occurrences(tupla, elemento):

    contador = 0
    for num in tupla:
        if num == elemento:
            contador += 1

    return contador


def find_index(tupla, elemento):

    for i, num in enumerate(tupla):
        if num == elemento:
            return i
    return -1



def filter_positives(numeros):

    tupla = []

    for num in numeros:
        if num > 0:
            tupla.append(num)

    return tuple(tupla)


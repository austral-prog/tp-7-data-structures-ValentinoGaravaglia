ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):


    set_de_ingredientes_sin_duplicados = set(ingredientes)

    return (nombre_plato, set_de_ingredientes_sin_duplicados)

def check_drinks(nombre_bebida, ingredientes):

    for valor in ingredientes:
        if valor in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"

def unique_chars(texto):

    return set(texto)


def sum_set(numeros):

    result = 0

    for num in numeros:
        result += num

    return result

def common_elements(set_a, set_b):


    result = set()

    for num in set_a:
        if num in set_b:
            result.add(num)

    return result

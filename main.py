def suma(x,y):
    """
    Función que toma 2 argumentos y devuelve la suma de los mismos
    Args:
        x(int/float): Primer valor a sumar
        y(int/float): Segundo valor a sumar
    
    return: x + y
    """
    return(x + y)

def invertir(cadena):
    """
    Función que toma una cadena y devuelve la misma pero invertida
    Args:
        cadena(String): Cadena a invertir

        return: cadena invertida
    """
    c = 0
    cadena_invertida = ""
    tamano = len(cadena)
    while c < tamano:
        cadena_invertida = cadena[c] + cadena_invertida
        c = c + 1
    return(cadena_invertida)

def palindroma(cadena):
    """
    Función que toma una cadena y devuelve un mensaje si es palindroma o no
    Args:
        cadena(String): Cadena a comprobar

        return: si es o no palindroma
    """
    normal = cadena
    c = 0
    cadena_invertida = ""
    tamano = len(cadena)
    while c < tamano:
        cadena_invertida = cadena[c] + cadena_invertida
        c = c + 1
    if(normal==cadena_invertida):
        return 'La cadena es palindroma'
    else:
        return 'La cadena no es palindroma'

def arraySuma(ar):
    """
    Función que recibe un array y devulve la suma de cada uno de sus elementos
    Args:
        ar(array[]):
    
    return: res
    """
    res = 0
    for i in ar:
        res = res + i
    return(res)

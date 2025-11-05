
def is_int(lines_qty: str) -> bool:
    """ Verifica si el valor ingresado es un número entero
    Args:
        lines_qty (str): Cantidad de líneas ingresadas
    Returns:
        bool: Condición de valor entero
    """
    
    try:
        int(lines_qty)
        return True
    except ValueError:
        return False

def in_range(lines_qty: str, range_bottom: int, range_top: int) -> bool:
    """ Verifica si el valor ingresado está dentro del rango
    Args:
        lines_qty (str): Cantidad de líneas ingresadas
        range_bottom (int): Valor mínimo del rango
        range_top (int): Valor máximo del rango
    Returns:
        bool: Condición de valor dentro del rango
    """
    
    if range_bottom <= int(lines_qty) <= range_top:
        return True
    else:
        return False

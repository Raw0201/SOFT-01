from common_tools import is_int, in_range

range_bottom = 0
range_top = 50
error_msg = "El dato de entrada no es válido"

def points_calc(lines_qty: str) -> int:
    """ Calcula el puntaje obtenido por cantidad de líneas
    Args:
        lines_qty (str): Cantidad de líneas ingresadas
    Returns:
        int: Puntaje obtenido
    """
    
    n = int(lines_qty)
    return int((5/2)*n*(n + 1))

def run_exercise():
    """Ejecuta el ejercicio de puntaje acumulado"""
    lines_qty = input("Ingrese la cantidad de líneas: ")

    if is_int(lines_qty) and in_range(lines_qty, range_bottom, range_top):
        points = points_calc(lines_qty)
        print(f"Puntaje: {points}")
    else:
        print("El dato de entrada no es válido")


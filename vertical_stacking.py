from common_tools import is_int, in_range

min_value = 0
max_value = 20
error_msg = "El dato de entrada no es válido"

def game_state(vertical_stacking: str, min_value: int, max_value: int) -> str:
    """ Determina el estado del juego según el apilamiento vertical
    Args:
        vertical_stacking (str): Apilamiento vertical
        min_value (int): Valor mínimo del rango = 0
        max_value (int): Valor máximo del rango = 20
    Returns:
        str: Mensaje del estado del juego
    """

    match int(vertical_stacking):
        case vertical_stacking if vertical_stacking == max_value:
            return "Fin de la partida"
        case vertical_stacking if vertical_stacking < max_value and vertical_stacking >= min_value:
            return "El juego se encuentra en curso"

def run_exercise():
    """Ejecuta el ejercicio de apilamiento vertical"""
    vertical_stacking = input("Ingrese la cantidad del apilamiento vertical: ")

    if is_int(vertical_stacking) and in_range(vertical_stacking, min_value, max_value):
        state = game_state(vertical_stacking, min_value, max_value)
        print(state)
    else:
        print(error_msg)

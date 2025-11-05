import os
from common_tools import is_int

valid_orientations = ["A", "d", "a", "i"]
new_orientation = ""

def show_message(message) -> None:
    os.system("cls")
    print(f"*** {message} ***")

def orientation_finder(initial, right, left) -> str:
    initial_index = valid_orientations.index(initial)
    new_index = (initial_index + int(right) - int(left))%4
    new_orientation = valid_orientations[new_index]
    return(new_orientation)

def turn_piece() -> str:
    while True:
        option = input("""
        Ingrese la letra de acuerdo con la orientación inicial de la pieza:

                                (A) Arriba
                (i) Izquierda                  (d) Derecha 
                                (a) Abajo
            
        O digite (f) para salir. Opción: """)

        if option in ("f", "F"):
            show_message("Gracias por usar el programa")
            break

        elif option in valid_orientations:
            turn_right = input("\nIngrese la cantidad de rotaciones hacia la derecha: ")

            if is_int(turn_right):
                turn_left = input("\nIngrese la cantidad de rotaciones hacia la izquierda: ")

                if is_int(turn_left):
                    new_orientation = orientation_finder(option, turn_right, turn_left)
                    return new_orientation
                
                else:
                    show_message("Error en giro a la izquierda. Por favor ingrese un dato válido")

            else:
                show_message("Error en giro a la derecha. Por favor ingrese un dato válido")
        
        else:
            show_message("Error en orientación inicial. Por favor ingrese un dato válido")

def run_exercise():
    """Ejecuta el ejercicio de rotar figura"""
    new_orientation = turn_piece()
    if new_orientation:
        print(f"\nNueva orientación de la pieza: {new_orientation}")
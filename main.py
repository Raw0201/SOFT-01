from common_tools import is_int, in_range
import vertical_stacking
import lines
import shapes
import rotation

def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("")
    print("**********************************")
    print("*                                *")
    print("*\tMenú de opciones:        *")
    print("*                                *")
    print("**********************************")
    print("")
    print("1. Apilamiento vertical")
    print("2. Puntaje acumulado")
    print("3. Mostrar Figura")
    print("4. Rotar Figura")
    print("0. Salir")

def main():
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        print("")
        try:
            opcion_input = input("Selecciona una opción: ")
            if is_int(opcion_input):
                opcion = int(opcion_input)
            else:
                print("Por favor, ingresa un número válido.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            # Ejercicio 1 - Apilamiento vertical
            vertical_stacking.run_exercise()
        elif opcion == 2:
            # Ejercicio 2 - Puntaje acumulado
            lines.run_exercise()
        elif opcion == 3:
            # Ejercicio 3 - Mostrar Figura
            shapes.run_exercise()
        elif opcion == 4:
            # Ejercicio 4 - Rotar Figura
            rotation.run_exercise()
        elif opcion == 0:
            print("Saliendo del programa... ¡Hasta luego!")
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":

    main()

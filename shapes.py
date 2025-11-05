chr = "*"
spc = " "

O_shape = f"{chr}{chr}\n{chr}{chr}"
I_shape = f"{chr}\n{chr}\n{chr}"
S_shape = f"{spc}{chr}{chr}\n{chr}{chr}"
Z_shape = f"{chr}{chr}\n{spc}{chr}{chr}"
L_shape = f"{chr}\n{chr}\n{chr}{chr}"
J_shape = f"{spc}{chr}\n{spc}{chr}\n{chr}{chr}"
T_shape = f"{chr}{chr}{chr}\n{spc}{chr}"


def shape_symbol(piece: str) -> str:
    """ Devuelve con símbolos la forma seleccionada por el usuario
    Args:
        piece (str): Forma seleccionada por el usuario
    Returns:
        str: Forma con símbolos
    """

    if piece not in ("o", "l", "s", "z", "L", "J", "T"):
        return("El dato de entrada no es válido")

    return(globals()[f"{piece}_shape"])


def run_exercise():
    """Ejecuta el ejercicio de mostrar figura"""
    piece = input("Ingrese la figura a seleccionar(o, l, s, z, L, J, T): ").upper()
    shape = shape_symbol(piece)
    print(shape)
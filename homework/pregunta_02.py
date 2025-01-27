"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4
"""

import pandas as pd

def pregunta_02():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    num_columnas = df.shape[1]

    return num_columnas

if __name__ == "__main__":
    print(pregunta_02())

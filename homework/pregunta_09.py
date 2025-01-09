"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    1    1  A   2  1999-10-28  1999
    2    2  B   5  1998-05-02  1998
    ...
    36  36  B   8  1997-05-21  1997
    37  37  C   9  1997-07-22  1997
    38  38  E   1  1999-09-28  1999
    39  39  E   5  1998-01-26  1998
"""
import pandas as pd

def pregunta_09():
    df = pd.read_csv(r"files/input/tbl0.tsv", sep="\t")

    if 'suma' in df.columns:  
         df = df.drop(columns=['suma'])
    
    # Identificar filas con fechas inválidas al intentar convertirlas
    invalid_dates = df[~pd.to_datetime(df['c3'], errors="coerce").notna()]
    
    if not invalid_dates.empty:
        print("Fechas inválidas detectadas, extrayendo solo el año:")
        print(invalid_dates)
    
    # Extraer el año de fechas válidas y manejar fechas inválidas
    df['year'] = pd.to_datetime(df['c3'], errors="coerce").dt.year.astype('Int64')  # Año para fechas válidas
    df['year'] = df['year'].fillna(df['c3'].str[:4])  # Rellenar años para fechas inválidas
    
    # Convertir a texto
    df['year'] = df['year'].astype('str')
    
    # Guardar el DataFrame actualizado
    df.to_csv(r"files/input/tbl0.tsv", sep="\t", index=False)
    
    return df

if __name__ == "__main__":
    pregunta_09()

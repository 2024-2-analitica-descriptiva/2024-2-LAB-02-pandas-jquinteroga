import pandas as pd

def eliminar_columna():
    # Leer el archivo tbl0.tsv
    df = pd.read_csv(r"files/input/tbl0.tsv", sep="\t")
    
    # Especificar la columna que deseas eliminar
    columna_a_eliminar = "year"  # Reemplaza "nombre_columna" por el nombre de la columna a eliminar
    
    # Verificar si la columna existe y eliminarla
    if columna_a_eliminar in df.columns:
        df = df.drop(columns=[columna_a_eliminar])
        print(f"Columna '{columna_a_eliminar}' eliminada correctamente.")
    else:
        print(f"La columna '{columna_a_eliminar}' no existe en el archivo.")
    
    # Guardar los cambios en el archivo
    df.to_csv(r"files/input/tbl0.tsv", sep="\t", index=False)

if __name__ == "__main__":
    eliminar_columna()


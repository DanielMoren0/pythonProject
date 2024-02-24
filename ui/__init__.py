from tabulate import tabulate

def mostrar_datos(data_frame):
    lista = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]
    print(tabulate(data_frame[lista], tablefmt="github", headers=
    ["Numero de registro", "Ciudad de ubicación", "Departamento", "Edad", "Tipo", "Estado", "Pais de Procedencia"]))

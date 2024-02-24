from api import obtener_datos_covid
from ui import mostrar_datos

def main():
    limite_registros = input("Digite el número de registros que desea consultar:")
    nombre_departamento = input("Ingrese el departamento que desea consultar:")
    data_frame = obtener_datos_covid(limite_registros, nombre_departamento.upper())
    mostrar_datos(data_frame)

if __name__=="__main__":
    main()
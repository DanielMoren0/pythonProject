from data_wrangling import dw
import matplotlib.pyplot as plt
from tabulate import tabulate
import pandas as pd
import matplotlib.dates as mdates


#solo admite bibliotecas
def impresion_datos_extraidos (results_df):

    print(tabulate(results_df, tablefmt="github", headers=results_df.keys()))

def imprimir_informacion_general_y_sumario_df (df):

    print("\nInformación general del dataframe:\n")
    print(dw.infomacion_general_df(df))

    print("\nColumnas con valores faltantes: \n" )
    print(dw.informacion_valores_faltantes(df))



    print("\nSumario del dataframe:\n")
    sumario = dw.sumario_df(df)
    print(tabulate(sumario, tablefmt="github", headers=sumario.columns.values.tolist()))
    print("\n")

def visualizar_datos_graficas(df):
    # Gráfico de dispersión: Edad vs. Fecha de inicio de síntomas
    plt.figure(figsize=(10, 6))
    plt.scatter(df["fecha_inicio_sintomas"], df["edad"], color="purple", alpha=0.5)
    plt.xlabel("Fecha de inicio de síntomas")
    plt.ylabel("Edad del individuo")
    plt.title("Gráfico de inicio de contagio y edad")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Gráfico de pastel: Estado de los individuos
    conteo_valores = df["estado"].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(conteo_valores, labels=conteo_valores.index, autopct="%1.1f%%", colors=["blue", "yellow", "green"])
    plt.axis("equal")
    plt.title("Distribución por estado de los individuos")
    plt.show()

    # Histograma: Distribución de los datos en municipios
    plt.figure(figsize=(12, 6))
    df["ciudad_municipio_nom"].hist(color="orange", bins=20)
    plt.title("Distribución de los casos por municipios")
    plt.xlabel("Municipio")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=90)
    plt.show()

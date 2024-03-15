from api import datos_covid as api
from ui import mostrar as ui
from data_wrangling import dw

print("\nDataFrame filtrado por el departamento de Risaralda (1000 primeros datos)\n\n")

# Extracción de datos filtrados por el departamento de Risaralda.
libreria_datos_extraidos = api.extraccion_datos_api("RISARALDA")
ui.impresion_datos_extraidos(libreria_datos_extraidos)

# Análisis inicial de los datos: información general y sumario estadístico.
ui.imprimir_informacion_general_y_sumario_df(libreria_datos_extraidos)

# Imputación de datos faltantes para mejorar la calidad de los datos.
dw.imputacion_datos_faltantes(libreria_datos_extraidos)

# Conversión de tipos de datos para permitir su uso en gráficas y análisis posteriores.
dw.typecasting_datos_requeridos(libreria_datos_extraidos)

print("\nDataFrame después de ser procesado con imputación y typecasting\n\n")
# Revisión del DataFrame tras la imputación de datos y conversión de tipos.
ui.impresion_datos_extraidos(libreria_datos_extraidos)

# Reevaluación de la información general y sumario estadístico después del procesamiento de datos.
ui.imprimir_informacion_general_y_sumario_df(libreria_datos_extraidos)

# Visualización de los resultados mediante gráficas.
ui.visualizar_datos_graficas(libreria_datos_extraidos)

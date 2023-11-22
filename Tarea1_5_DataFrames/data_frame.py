import pandas as pd
import warnings

warnings.filterwarnings('ignore')
df = pd.read_csv(
    'lista_ventas.csv',
    encoding='windows-1252',
    decimal=",",
    parse_dates=['FechaNacimiento', 'FechaCompra'
                 ]
)
print(df.head())
"""
Extracción de subconjunto

Imprime por pantalla:

Todas las filas de las columnas Edad y Número de elementos.
Valores de Edad y Artículos para el segundo y tercer registro.
Fecha de compra para los últimos 5 registros.

"""
print(f"{df['Edad']} y numero de elementos: {len(df['Edad'])}")

print(df.loc[1:2, ['Edad', 'Artículos']])

print(df['FechaCompra'].tail()) # Por defecto carga los últimos 5 si no tail(n)

"""
Carga de datos indicando los índices

Vuelve a cargar el dataframe de forma que tome el primer valor de cada registro como el índice.

Vuelve a ejecutar .info() para verificar que IDCliente ya no es una columna.
"""


df = pd.read_csv(
    'lista_ventas.csv',
    encoding='windows-1252',
    decimal=",",
    parse_dates=['FechaNacimiento', 'FechaCompra'
                 ],
    index_col=['IDCliente']
)

"""
Índice con mayor importe

Recupera el índice de la fila con el mayor importe.
"""

id_max = df['Importe'].idxmax()
imp_max = df['Importe'].max()
print(f"Codigo cliente: {id_max} con un importe de {imp_max}")

"""
Asignar un valor a varios elementos

Decides que aquellos clientes que tengan una compra inferior a 25€ les vas a poner un valor de 10.
"""
# Como el df.info() dice que importe es tipo object cambiamos a numeric:
df['Importe'] = pd.to_numeric(df['Importe'])
# Cambiamos con la condición
df.loc[df['Importe'] < 25, 'Importe'] = 10

"""
# 6- Ordenar el Dataframe
1. Ordenar las filas del dataframe de modo que el importe se muestre en orden descendente. 
2. Debes modificar el dataframe original para que este cambio sea definitivo. 
3. Imprime por pantalla el dataframe anterior, pero ordenado por el índice de forma ascendente (IDCliente).
En esta ordenación no debes modificar el dataframe original.
"""
df = df.sort_values(by=['Importe'], ascending=False)
print(df)

print(df.sort_values(by=['IDCliente'], ascending=True))
"""
Reindexar el dataframe

Modificar los índices del dataframe, añadiendo una “c” antes del número. 
Es decir, los índices de las filas serán: “c1, c2, ..., c10,...”. El cambio debe ser permanente.
"""

df = df.rename(index=lambda x: x.replace('0', ''))
print(df)

"""
Aplicar función a los datos de las columnas

Diferencia entre el máximo y el mínimo.
Debes hacerlo en el menor número de instrucciones posible.
"""


def calculate_difference(n1, n2):
    return n1 - n2


val1 = df['Importe'].max()
val2 = df['Importe'].min()

print(calculate_difference(val1, val2))

"""
Correlación entre las columnas

Obtén la correlación entre las diferentes columnas.
Relación completa entre ellas ??.
Modifica dataframe para borrar aquella que no aporta nueva información.
"""

correlation = df.corr()
print(correlation)
print(df.head())
print(df.info())

"""
Hay Correlación entre fecha de nacimiento y edad pues vemos que las variables tienen relación 
lineal.
Suprimiría la columna edad
"""
df.drop('Edad', axis=1, inplace=True)
print(df.head())
print(df.info())




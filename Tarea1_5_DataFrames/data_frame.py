import pandas as pd


pd.to_datetime("20/01/2023", format="%d/%m/%Y")
df = pd.read_csv(
    'lista_ventas.csv',
    encoding='windows-1252',
    decimal=",",
    parse_dates=['FechaNacimiento', 'FechaCompra'
                 ]
)
print(df.head())
print(df['Edad'])

print(f" Numero de elementos: {len(df['Edad'])}")
print(f"Edad segunda fila:{df['Edad'].loc[1]}\n"
      f"Edad tercera fila:{df['Edad'].loc[2]}")

row = len(df['Edad']) - 1
for i in range(5):
    print(f" Edad fila {row + 1} : {df['Edad'].loc[row]}")
    row -= 1

df = pd.read_csv(
    'lista_ventas.csv',
    encoding='windows-1252',
    decimal=",",
    parse_dates=['FechaNacimiento', 'FechaCompra'
                 ],
    index_col=['IDCliente']
)

print(df.tail())

id_max = df['Importe'].idxmax()
imp_max = df['Importe'].max()
print(f"Codigo cliente: {id_max} con un importe de {imp_max}")

df['Importe'] = pd.to_numeric(df['Importe'])
df.loc[df['Importe'] < 10, 'Importe'] = 10

df = df.sort_values(by=['Importe'], ascending=False)
print(df)

print(df.sort_values(by=['IDCliente'], ascending=True))

df_reindex = df.rename(index=lambda x: x.replace('0', ''))
print(df_reindex)


def calculate_difference(n1, n2):
    return n1 - n2


val1 = df['Importe'].max()
val2 = df['Importe'].min()

print(calculate_difference(val1, val2))

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




import pandas as pd
import numpy as np

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
df[df['Importe'] < 10].replace(10, inplace=True)



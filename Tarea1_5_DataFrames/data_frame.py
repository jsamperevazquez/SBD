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
df.loc[df['Importe'] < 10, 'Importe'] = 10

df = df.sort_values(by=['Importe'], ascending=False)
print(df)

print(df.sort_values(by=['IDCliente'], ascending=True))

index_df = np.array(df.index)
print(index_df)
for i in range(len(index_df)):
    index_df[i] = "c" + str(i + 1)

df['IDcliente'] = index_df
print(df.head())
df.reset_index(drop=True, inplace=True)
df.set_index('IDcliente', inplace=True)
print(df.head())
import pandas as pd
import csv

with open('fao.csv') as fao_file:
    reader = csv.reader(fao_file)
    headers = next(reader)

header_indices = [i for i, item in enumerate(headers) if item]

df_fao = pd.read_csv('fao.csv', usecols=header_indices, encoding='latin-1')
df_fao['Date'] = pd.to_datetime(df_fao['Date'])
df_fao.rename(columns={'Date': 'ID_YYYY'}, inplace=True)
print(df_fao)
print(df_fao.dtypes)
"""
Debe calcular la media anual del precio de cada producto 
en un nuevo dataframe añadiendo un ID adicional 
de la forma ID_YYYY, siendo YYYY el año para cada producto.
"""

# Calculo la media agrupando por la fecha
product_mean = df_fao.groupby(df_fao['ID_YYYY'].dt.year).mean().round(decimals=2)
print(product_mean)
product_mean.set_index('ID_YYYY', inplace=True)
product_mean.rename(index=lambda x: x.strftime('ID_%Y'), inplace=True)

print(product_mean)

# Con Excel
# Indico el nombre de la hoja que usaremos
sheet = 'Indices_Monthly_Real'
# Abro io con read_excel y hoja
df_faoxls = pd.read_excel('fao.xls',
                          keep_default_na=False, sheet_name=sheet)
# Convierto object a datetime
df_faoxls['Month'] = pd.to_datetime(df_faoxls['Month'])
# Cambio nombre de cabecera
df_faoxls.rename(columns={'Month': 'ID_YYYY'}, inplace=True)
# Calculo la media agrupando por la fecha
product_meanxls = df_fao.groupby(df_faoxls['ID_YYYY'].dt.year).mean().round(decimals=2)
# Establezco índice
product_meanxls.set_index('ID_YYYY', inplace=True)
# Creo lambda para cambiar nombre de índice del DF
product_meanxls.rename(index=lambda x: x.strftime('ID_%Y'), inplace=True)

print("EXCEL")
print(product_meanxls)

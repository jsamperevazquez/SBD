library(readxl)
ruta_archivo <- "Estadisticas_Netflix.xlsx"

nombre_hoja <- "Netflix annual subscribers"

hojas_disponibles <- excel_sheets(ruta_archivo)


if (nombre_hoja %in% hojas_disponibles) {
  datos_excel <- read_excel(ruta_archivo, sheet = nombre_hoja)
  print(datos_excel) }else
    {
  cat("La hoja", nombre_hoja, "no está presente en el archivo Excel.\n") }


# Filas de los años entre 2015 y 2016 inclusive.
datos_excel[datos_excel$Date == 2015 | datos_excel$Date == 2016,]

# Valores de los años 2018 y 2020
datos_excel$`Subscribers  (mm)`[datos_excel$Date == 2015 | datos_excel$Date == 2016]

# Los tres primeros registros
head(datos_excel, n=3)

nombre_hoja <- 'Netflix subscribers by areas'
datos_excel <- read_excel(ruta_archivo, sheet = nombre_hoja)
# Suma de columnas y añadimos fila a dataframe
suma_columnas <- colSums(datos_excel)
datos_excel = rbind(datos_excel, suma_columnas)
print(datos_excel)

nombre_hoja <- 'Netflix annual net incomeloss'
datos_excel <- read_excel(ruta_archivo, sheet = nombre_hoja)
print(tail(datos_excel, n=5))
# Suma de 5 últimas filas y añadimos fila a dataframe
suma_columnas <- sum(tail(datos_excel$`Net Income/Loss ($mm)`, n=5))
datos_excel = rbind(datos_excel[2],suma_columnas)
print(tail(datos_excel, n=6))

library('rlist')
datos_excel <- read_excel(ruta_archivo, sheet = nombre_hoja)
# Crear un vector para almacenar los valores
valores <- numeric(nrow(datos_excel))


options(warn=-1)
nombre_hoja <- 'Netflix subscribers by areas'
datos_excel <- read_excel(ruta_archivo, sheet = nombre_hoja)
for (n in colnames(datos_excel)){
  if (n == "Year"){
   next
  }else{
   df_sub_set <- datos_excel[,c('Year',n)]
   print(df_sub_set[order(df_sub_set[n] , decreasing = TRUE),])
  }
}

datos_excel_corr <- cor(datos_excel)
datos_excel_corr

library(ggplot2)

dat <- data.frame(
x = datos_excel[1],
y = datos_excel[3]
)
plot <- ggplot(dat, aes(x =Year , y = EMEA))
plot + geom_line(color = "red") + labs(title = "Evolución de Europa y África por año", x = "Año", y = "Valor")

dat <- data.frame(
x = datos_excel[1],
y = datos_excel[2]
)
plot <- ggplot(dat, aes(x = Year, y = US...Canada))
plot + geom_line(color = "blue") + labs(title = "Evolución de USA y Canada por año", x = "Año", y = "Valor")

dat <- data.frame(
x = datos_excel[1],
y = datos_excel[4]
)
plot <- ggplot(dat, aes(x = Year, y = Latin.America))
plot + geom_line(color = "green") + labs(title = "Evolución de América Látina por año", x = "Año", y = "Valor")

dat <- data.frame(
x = datos_excel[1],
y = datos_excel[5]
)
plot <- ggplot(dat, aes(x =Year , y = Asia.Pacific))
plot + geom_line(color = "yellow") + labs(title = "Evolución de Asia y Pacífico por año", x = "Año", y = "Valor")

library("reshape2")
# Convierto los nombres de las columnas para evitar problemas con los espacios
names(datos_excel) <- make.names(names(datos_excel))

# Cambio la forma del dataframe para que los años estén en una columna
data_l <- reshape2::melt(datos_excel, id.vars = "Year", variable.name = "Region", value.name = "Value")
ggplot(data_l, aes(x = Year, y = Value, color = Region)) +
  geom_line() +
  labs(title = "Evolución de las regiones por año", x = "Año", y = "Valor")

library(ggplot2)
df = data.frame(tail(datos_excel_sum[2:5], n=1))
# Dataframe transpuesto para obtener una fila con los nombres de las columnas como una variable
df <- t(df)
# Convierto la fila en un dataframe
data_l <- as.data.frame(df)
# Añado los nombres de las columnas como una columna "Region"
data_l$Region <- row.names(data_l)
# Renombro la columna con los valores
names(data_l)[1] <- "Value"
ggplot(data_l, aes(x = Region, y = Value, fill = Region)) +
  geom_bar(stat = "identity") +
  coord_polar() +
  labs(title = "Gráfico Radial de Valores", x = "", y = "") +
  theme_minimal()
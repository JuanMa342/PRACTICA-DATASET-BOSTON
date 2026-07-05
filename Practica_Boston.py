# Importo las librerías necesarias
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print('''
Vamos a hacer una serie de ejercicios de Visualización de Datos con Python con las librerías MATPLOTLIB y SEABORN.
Vamos a trabajar con un DataSet "Boston" que lo podemos operar desde los Sets de ejemplo de "Phsykitlearn".
''')

# Agregar el nombre de las columnas
column_names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']

# Cargar el archivo .CSV en un DataFrame
# df = pd.read_csv('housing.csv',header=None,delimiter=r"\s+",names=column_names)
df = pd.read_csv('https://raw.githubusercontent.com/digitalhouse-content/Recursos-descargables-visualizaci-n-de-datos-con-python/main/housing.csv',header=None,delimiter=r"\s+",names=column_names)

# Variables del DataSet
print('''
Variables del DataSet:
- CRIM: Tasa de criminalidad per cápita por ciudad.
- ZN: Proporción de terreno residencial dividido en zonas para lotes de más de 25.000 pies cuadrados.
- INDUS: Proporción de acres comerciales no minoristas por ciudad.
- CHAS: Variable ficticia Charles River (1 si el tramo limita con el Río; 0 en caso contrario).
- NOX: Concentración de óxidos nítricos (partes por 10 millones).
- RM: Número medio de habitaciones por vivienda.
- AGE: Proporción de unidades por propiestarios construidas antes de 1940.
- DIS: Distancias ponderadas a cinco centros de empleo de Boston.
- RAD: Índice de accesibilidad a carreteras radiales.
- TAX: Tasa de Impuesto a la propiedad de valor completo por $10.000.
- PTRATIO: Proporción alumno-maestro por ciudad.
- B: 1000 (bk-0.63) 2 1000 (Bk-0.63) 2 donde bk Bk es la proporción de personas negras por ciudad.
- LSTAT: Porcentaje de la población con estatus inferior.
- MEDV: Valor medio de las viviendas ocupadas por sus propietarios en $1000.
El DataSet "Boston" nos cuenta acerca del valor de las propiedades en la ciudad de Boston y distinta información 
de la ciudad y sus alrededores. Cada fila del DataSet representa una propiedad.
''')

# Visualizamos el DataSet
print(df)

# Vamos a desarmar el DataSet
df.head()
df.describe()
df.dtypes
df.info()

# Vamos a hacer un gráfico que nos muestre la correlación que nos muestre todas las variables numéricas del DataSet.
plt.figure(figsize=(8,6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix,annot=True,cmap='viridis')
plt.title('Mapa de Calor de correlación entre variables')
plt.show()
print('''
SIEMPRE debemos hacer la "Correlation Matrix" al empezar a analizar un DataSet para ver que variables tienen un alto índice 
de correlación y cuál no; Y se analizan Todas las variables Numéricas del DataSet.
''')

# Vamos a hacer un histograma
plt.hist(df['CRIM'],bins=20)
plt.title('Distribución por tasa de criminalidad')
plt.xlabel('Tasa de Criminalidad per cápita')
plt.ylabel('Frecuencia')
plt.show()

# Voy a hacer un Boxplot de Óxidos Nítricos
plt.boxplot(df['NOX'])
plt.title('Boxplot de Óxidos Nítricos')
plt.ylabel('Concentración')
plt.show()

# Vamos a hacer un Histograma de la variable 'Age'
plt.hist(df['AGE'],bins=20,edgecolor='black')
plt.title('Distribución de la edad de las viviendas')
plt.xlabel('Proporción de unidades construídas antes de 1940')
plt.ylabel('Frecuencia')
plt.show()

# Vamos a ver la Accesibilidad a carreteras radiales, oséa ver cómo se distribuye esta variable
plt.hist(df['RAD'],bins=20,edgecolor='black',color='orange')
plt.title('Accesibilidad a carreteras radiales')
plt.xlabel('Índice de accesibilidad')
plt.ylabel('Frecuencia')
plt.show()

# Vamos a ver si hay correlación entre "Índice de Accesibilidad" y "Valor Medio de las Viviendas"
plt.scatter(df['RAD'],df['MEDV'],alpha=0.5)
plt.title('Carreteras vs Precio Medio de las Viviendas')
plt.xlabel('Carreteras')
plt.ylabel('Precio Medio de las Viviendas')
plt.show()

# Vamos a ver si hay correlación entre la variable "Carreteras" y el "Número de habitaciones"
plt.scatter(df['RM'],df['MEDV'],alpha=0.5)
plt.title('Número de habitantes vs Precio Medio de las Viviendas')
plt.xlabel('número de habitaciones')
plt.ylabel('Precio Medio de las Viviendas')
plt.show()

# Vamos a ver si hay una correlación entre el precio de las viviendas y la distancia que hay a los Centros de Empleo
plt.scatter(df['DIS'],df['MEDV'],alpha=0.5,color='green')
plt.title('Distancia a Centros de Empleo vs Precio Medio de las Viviendas')
plt.xlabel('Distancia a Centros de Empleo')
plt.ylabel('Precio Medio de las Viviendas')
plt.show()

# Vamos  ver si hay correlación entre "Clase Social" y "Status"
plt.scatter(df['LSTAT'],df['MEDV'],alpha=0.5,color='purple')
plt.title('Porcentaje de "Status Inferior" vs Precio Medio de las Viviendas')
plt.xlabel('Porcentaje de "Status Inferior"')
plt.ylabel('Precio Medio de las Viviendas')
plt.show()

# Conclusiones Generales
print('''
Conclusiones Generales de lo analizado en este DataSet:
- A mayor Criminalidad, menor es el precio de las viviendas.
- Número de habitaciones aumenta el valor de las viviendas.
- Las viviendas más antiguas tienden a tener valores mas bajos.
- Accesibilidad: A mayor distancia de los Centros de Empleo (ó Zonas de Empresas y Fábricas), menos es 
el valor de las viviendas.
''')
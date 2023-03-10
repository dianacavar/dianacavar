# -*- coding: utf-8 -*-
"""UNP PROCESAMIENTO DATOS_SOLICITUDES_2020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NErNT8x4nVpGxLcvkNcV0lUaGwqEad7E

> UNP

# Librerias
"""

!pip install sodapy

import pandas as pd
from sodapy import Socrata
import numpy as np
import seaborn as sns

"""##Librerias para visualización"""

import matplotlib.pylab as plt # Herramienta principal de visualización https://matplotlib.org/stable/contents.html
import matplotlib.dates as mdates # Dentro de matplotlib, tenemos una herramienta para manejo de fechas 
import seaborn as sbn # Herramienta complementaria de visualización https://seaborn.pydata.org/

"""# Lectura de la fuente de datos (Publica)"""

client = Socrata("www.datos.gov.co", None)
results = client.get("mms4-vct3", limit=35000) # Con limite de 1.000 filas (Filas 3,98M)

df = pd.DataFrame.from_records(results)

"""# Limpieza de datos"""

# Convierte las columnas tipo objeto a fecha
df['fecha_de_registro_en_base'] = pd.to_datetime(df['fecha_de_registro_en_base'])
print(df.dtypes)

# Calcula algunas estadisticas descriptivas/ incluso las categoricas
print(df.describe(include="all"))

df.dtypes

# Crea la columna de año de la fecha de registro
df["anoregistro"] = df['fecha_de_registro_en_base'].dt.year
# Muestra cuantos años unicos hay en la columna
print(len(df["anoregistro"].unique()))
# Muestra cuales son los años unicos hay en la columna
print(df["anoregistro"].unique())

# Crea la columna de año de la fecha de registro
df["mesregistro"] = df['fecha_de_registro_en_base'].dt.month
# Muestra cuantos años unicos hay en la columna
print(len(df["mesregistro"].unique()))
# Muestra cuales son los años unicos hay en la columna
print(df["mesregistro"].unique())

# Muestra cuantos datos unicos hay en la columna
print(len(df['se_realiz_inicio_de_ruta'].unique()))
# Muestra cuales son los datos unicos que hay en la columna
print(df['se_realiz_inicio_de_ruta'].unique())
print(df['se_realiz_inicio_de_ruta'].value_counts())


# Obtener la matriz de conteo a nivel absoluto
a = pd.crosstab(index=df['se_realiz_inicio_de_ruta'], columns='count')
# Obtener la matriz de conteo a nivel relativo
b = pd.crosstab(index=df['se_realiz_inicio_de_ruta'], columns='count', normalize=True) * 100


# Imprimir los resultados
print(a)
print(round(b))

# Muestra cuantos datos unicos hay en la columna
print(len(df['departamento'].unique()))
# Muestra cuales son los datos unicos que hay en la columna
print(df['departamento'].value_counts())

# Unificar Departamentos Reemplaza numero
df['departamento'] = df['departamento'].replace('01. AMAZONAS','AMAZONAS')
df['departamento'] = df['departamento'].replace('02. ANTIOQUIA','ANTIOQUIA')
df['departamento'] = df['departamento'].replace('31. VALLE_DEL_CAUCA','VALLE DEL CAUCA')
df['departamento'] = df['departamento'].replace('07. BOLÍVAR','BOLÍVAR')
df['departamento'] = df['departamento'].replace('15. CÓRDOBA','CÓRDOBA')
df['departamento'] = df['departamento'].replace('06. BOGOTÁ_D.C','BOGOTÁ D.C')
df['departamento'] = df['departamento'].replace('09. CALDAS','CALDAS')
df['departamento'] = df['departamento'].replace('23. NARIÑO','NARIÑO')
df['departamento'] = df['departamento'].replace('13. CESAR','CESAR')
df['departamento'] = df['departamento'].replace('27. RISARALDA','RISARALDA')
df['departamento'] = df['departamento'].replace('24. NORTE_DE_SANTANDER','NORTE DE SANTANDER')
df['departamento'] = df['departamento'].replace('19. HUILA','HUILA')
df['departamento'] = df['departamento'].replace('22. META','META')
df['departamento'] = df['departamento'].replace('12. CAUCA','CAUCA')
df['departamento'] = df['departamento'].replace('05. ATLÁNTICO','ATLÁNTICO')
df['departamento'] = df['departamento'].replace('03. ARAUCA','ARAUCA')
df['departamento'] = df['departamento'].replace('14. CHOCÓ','CHOCÓ')
df['departamento'] = df['departamento'].replace('30. TOLIMA','TOLIMA')
df['departamento'] = df['departamento'].replace('29. SUCRE','SUCRE')
df['departamento'] = df['departamento'].replace('20. LA_GUAJIRA','LA GUAJIRA')
df['departamento'] = df['departamento'].replace('16. CUNDINAMARCA','CUNDINAMARCA')
df['departamento'] = df['departamento'].replace('28. SANTANDER','SANTANDER')
df['departamento'] = df['departamento'].replace('26. QUINDÍO','QUINDÍO')
df['departamento'] = df['departamento'].replace('21. MAGDALENA','MAGDALENA')
df['departamento'] = df['departamento'].replace('08. BOYACÁ','BOYACÁ')
df['departamento'] = df['departamento'].replace('11. CASANARE','CASANARE')
df['departamento'] = df['departamento'].replace('10. CAQUETÁ','CAQUETÁ')
df['departamento'] = df['departamento'].replace('18. GUAVIARE','GUAVIARE')
df['departamento'] = df['departamento'].replace('25. PUTUMAYO','PUTUMAYO')
df['departamento'] = df['departamento'].replace('33. VICHADA','VICHADA')
df['departamento'] = df['departamento'].replace('17. GUAINÍA','GUAINÍA')
df['departamento'] = df['departamento'].replace('32. VAUPÉS','VAUPÉS')
df['departamento'] = df['departamento'].replace('04. ARCHIPIÉLAGO_DE_SAN_ANDRÉS','ARCHIPIÉLAGO DE SAN ANDRÉS')
#Conteo municipio
print(df['departamento'].value_counts())

# Muestra cuantos datos unicos hay en la columna
print(len(df['municipio'].unique()))
# Contar
print(df['municipio'].value_counts())

# Muestra cuantos datos unicos hay en la columna
print(len(df['poblaci_n'].unique()))
# Contar
print(df['poblaci_n'].value_counts())

# Muestra cuantos datos unicos hay en la columna
print(len(df['poblaci_n_en_virtud_del_riesgo'].unique()))
df['poblaci_n_en_virtud_del_riesgo'] = df['poblaci_n_en_virtud_del_riesgo'].replace('20. No objeto','20. No Objeto')
# Contar
print(df['poblaci_n_en_virtud_del_riesgo'].value_counts())

# Muestra cuantos datos unicos hay en la columna
print(len(df['sub_poblaci_n_en_virtud_del'].unique()))
# Contar
print(df['sub_poblaci_n_en_virtud_del'].value_counts())

# Muestra cuantos datos unicos hay en la columna
print(len(df['g_nero'].unique()))
# Contar
print(df['g_nero'].value_counts())

"""#AGRUPAR"""

g2= df[['departamento','municipio']].value_counts()
g2

"""##VISUALIZACIÓN"""

labels_genero =df['g_nero'].unique()
genero = df['g_nero'].value_counts()
fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (18, 6))#dice cuantas cuadriculas y tamaño
axs[0].grid('on', linestyle = 'dashed', alpha = 0.5)
axs[0].set_title('Género de lxs Participantes')
axs[0].set_ylabel('Fracción')
axs[0].bar(x = [i for i in range(len(genero))], # Definimos la ubicación de las barras a lo largo del eje horizontal
           height = genero.values  / genero.values.sum(), # Definimos la altura de las barras
           color = plt.get_cmap('Set2').colors) #paleta de colores


axs[0].set_xticks([i for i in range(len(genero))])
axs[0].set_xticklabels(labels_genero, rotation = 90)
axs[0].set_yscale('log')
axs[0].tick_params(axis='both', which='major', labelsize = 12)

axs[1].pie(genero.values / genero.values.sum(),
           colors = plt.get_cmap('Set2').colors)
axs[1].legend(labels_genero, loc = (-0.12,-0.15))


plt.show()

#GRAFICAR CON SEABORN LA FRECUENCIA DE SOLICITUDES POR GENERO
sns.barplot( data=df , x=df.index , y=df["g_nero"] )

#GRAFICAR CON SEABORN LA FRECUENCIA DE SOLICITUDES POR POBLACION Y GENERO
sns.displot(df , x='poblaci_n' , hue="g_nero")

"""TABLA CRUZADA"""

# creación de la tabla cruzada
tabla1 = pd.crosstab(df['poblaci_n_en_virtud_del_riesgo'], df['se_realiz_inicio_de_ruta'])

# ordenamiento de la tabla cruzada
tabla1 = tabla1.sort_values(by='SI', ascending=False)

print(tabla1)

"""FILTROS DE QUIENES INICIARON RUTA DE PROTECCIÓN EN LA ENTIDAD"""

#De los que si iniciaron ruta, cual es el mayor departamento con casos 
departamento_si = df[df['se_realiz_inicio_de_ruta'] == "SI"]["departamento"].value_counts().head(5)
print("El departamento con mayor casos que iniciaron ruta de protección",departamento_si)

#De los que si  iniciaron ruta, cual es el mayor municipio con casos 
municipio_si = df[df['se_realiz_inicio_de_ruta'] == "SI"]["municipio"].value_counts().head(5)
print("El municipio con mayor casos que iniciaron ruta de protección",municipio_si)

#De los que si  iniciaron ruta, cual es la poblacion top 
poblacion_si = df[df['se_realiz_inicio_de_ruta'] == "SI"]["poblaci_n_en_virtud_del_riesgo"].value_counts().head(5)
print("La poblacion con mayor casos que iniciaron ruta de protección",poblacion_si)

#De los que  no iniciaron ruta, cual es la poblacion top 
poblacion_no = df[df['se_realiz_inicio_de_ruta'] == "NO"]["poblaci_n_en_virtud_del_riesgo"].value_counts().head(5)
print("La poblacion con mayor casos que no iniciaron ruta de protección",poblacion_no)

# creación de la tabla cruzada
tabla2 = pd.crosstab(df['departamento'], df['poblaci_n']).head(10)

# ordenamiento de la tabla cruzada
tabla2 = tabla2.sort_values(by='Líderes Sociales', ascending=False)
print(tabla2)

"""ANALISIS DE DEPENDENCIA"""

#ANALISIS DE DEPENDENCIA ENTRE INICIO DE RUTA Y POBLACION 
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(tabla1)

print("Chi-squared test statistic:", chi2)
print("p-value:", p)

#Si p-values es menor a 0,05 rechazo la hipotesis de dependencia
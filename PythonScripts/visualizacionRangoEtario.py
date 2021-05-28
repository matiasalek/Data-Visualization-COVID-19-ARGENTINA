import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# leo el archivo .csv que solo contiene los datos que voy a visualizar y/o analizar
casos_visualizacion = pd.read_csv('Covid19CasosCorregido.csv')

# extraigo los valores de la columna edad que cumplen la condicion a la cual hace referencia el nombre de la variable.
edad_0_20 = casos_visualizacion.loc[(casos_visualizacion['edad'] < 21) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_21_30 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 20) & (casos_visualizacion['edad'] < 31) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_31_40 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 30) & (casos_visualizacion['edad'] < 41) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_41_50 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 40) & (casos_visualizacion['edad'] < 51) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_51_60 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 50) & (casos_visualizacion['edad'] < 61) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_61_70 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 60) & (casos_visualizacion['edad'] < 71) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_71_80 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 70) & (casos_visualizacion['edad'] < 81) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_81_90 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 80) & (casos_visualizacion['edad'] < 91) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_91_100 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 90) & (casos_visualizacion['edad'] < 101) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']
edad_101 = casos_visualizacion.loc[(casos_visualizacion['edad'] > 100) & (casos_visualizacion['fallecido'] == 'SI'), 'edad']

# obtengo solo la longitud de cada rango etario
edad_0_20_list = edad_0_20.tolist()
edad_0_20_len = len(edad_0_20_list)

edad_21_30_list = edad_21_30.tolist()
edad_21_30_len = len(edad_21_30_list)

edad_31_40_list = edad_31_40.tolist()
edad_31_40_len = len(edad_31_40_list)

edad_41_50_list = edad_41_50.tolist()
edad_41_50_len = len(edad_41_50_list)

edad_51_60_list = edad_51_60.tolist()
edad_51_60_len = len(edad_51_60_list)

edad_61_70_list = edad_61_70.tolist()
edad_61_70_len = len(edad_61_70_list)

edad_71_80_list = edad_71_80.tolist()
edad_71_80_len = len(edad_71_80_list)

edad_81_90_list = edad_81_90.tolist()
edad_81_90_len = len(edad_81_90_list)

edad_91_100_list = edad_91_100.tolist()
edad_91_100_len = len(edad_91_100_list)

edad_101_list = edad_101.tolist()
edad_101_len = len(edad_101_list)

labels = ['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100', '100+']
muertos_rango_etario = [edad_0_20_len, edad_21_30_len, edad_31_40_len, edad_41_50_len, edad_51_60_len, edad_61_70_len, edad_71_80_len, edad_81_90_len, edad_91_100_len, edad_101_len]

x = np.arange(len(labels))
width = 0.35  # ancho de las barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, muertos_rango_etario, width)

# Añado titulo, ylabel, etc
ax.set_ylabel('Muertos')
ax.set_title('Muertos por COVID-19 en distintos rangos etarios')
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.bar_label(rects1, padding=1)
fig.tight_layout()

# guardo el plot y lo muestro
plt.savefig('MuertosRangoEtario.png')
plt.show()

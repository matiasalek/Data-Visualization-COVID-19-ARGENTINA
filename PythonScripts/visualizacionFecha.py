import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# cargo el archivo
archivo_csv = pd.read_csv('Covid19CasosCorregido.csv')

# extraigo la cantidad de casos en el mismo periodo
periodo_2020 = archivo_csv.loc[(archivo_csv['fecha_diagnostico'] > '2020-03-19') & (archivo_csv['fecha_diagnostico'] < '2020-05-26'), 'fecha_diagnostico']
periodo_2021 = archivo_csv.loc[(archivo_csv['fecha_diagnostico'] > '2021-03-19') & (archivo_csv['fecha_diagnostico'] < '2021-05-26'), 'fecha_diagnostico']

periodo_2020_list = periodo_2020.tolist()
periodo_2021_list = periodo_2021.tolist()

periodo_2020_casos = len(periodo_2020_list)
periodo_2021_casos = len(periodo_2021_list)


# empiezo con el ploteo
labels = ['2020', '2021']
casos_mismo_periodo = [periodo_2020_casos, periodo_2021_casos]

x = np.arange(len(labels))
width = 0.40  # ancho de las barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, casos_mismo_periodo, width)

# Añado titulo, ylabel, etc
ax.set_ylabel('Casos')
ax.set_title('Cantidad de casos COVID-19 en el mismo periodo 20-03 a 25-05')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
ax.bar_label(rects1, padding=1, fmt='%.2f')
fig.tight_layout()

# guardo el plot y lo muestro
plt.savefig('CasosMismaFecha.png')
plt.show()

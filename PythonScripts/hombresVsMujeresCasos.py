import pandas as pd
import matplotlib.pyplot as plt

# cargo el csv
covid_csv_casos = pd.read_csv('Covid19CasosCorregido.csv')

# extraigo los muertos hombres en la variable muertos_hombres y lo mismo para las mujeres en la variable muertos_mujeres
casos_hombres = covid_csv_casos.loc[(covid_csv_casos['sexo'] == 'M'), 'sexo']
casos_mujeres = covid_csv_casos.loc[(covid_csv_casos['sexo'] == 'F'), 'sexo']

casos_total = 3586736

casos_hombres_list = casos_hombres.tolist()
casos_mujeres_list = casos_mujeres.tolist()

casos_mujeres_total = len(casos_mujeres_list)
casos_hombres_total = len(casos_hombres_list)

casos_hombres_chart = casos_hombres_total * 100 / casos_total
casos_mujeres_chart = casos_mujeres_total * 100 / casos_total

labels = ['Hombres', 'Mujeres']
sizes = [casos_hombres_chart, casos_mujeres_chart]

fig, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
ax2.axis('equal')

# guardo el grafico en formato .png y lo muestro
plt.savefig('CasosHombresVsMujeres.png')
plt.show()

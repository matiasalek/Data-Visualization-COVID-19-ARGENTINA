import pandas as pd
import matplotlib.pyplot as plt

# cargo el csv
covid_csv = pd.read_csv('Covid19CasosCorregido.csv')

# extraigo los muertos hombres en la variable muertos_hombres y lo mismo para las mujeres en la variable muertos_mujeres
muertos_hombres = covid_csv.loc[(covid_csv['sexo'] == 'M') & (covid_csv['fallecido'] == 'SI'), 'sexo']
muertos_mujeres = covid_csv.loc[(covid_csv['sexo'] == 'F') & (covid_csv['fallecido'] == 'SI'), 'sexo']
muertos_total = 73067

muertos_hombres_list = muertos_hombres.tolist()
muertos_mujeres_list = muertos_mujeres.tolist()

muertos_hombres_total = len(muertos_hombres_list)
muertos_mujeres_total = len(muertos_mujeres_list)

muertos_hombres_chart = muertos_hombres_total * 100 / muertos_total
muertos_mujeres_chart = muertos_mujeres_total * 100 / muertos_total

# lo que va a mostrar el grafico Pie Chart
labels = ['Mujeres', 'Hombres']
sizes = [muertos_mujeres_chart, muertos_hombres_chart]

# creo el grafico
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
ax1.axis('equal')

# guardo el grafico en formato .png y lo muestro
plt.savefig('MuertosHombresVsMujeres.png')
plt.show()

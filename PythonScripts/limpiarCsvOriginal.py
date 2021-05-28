import pandas as pd

# cargo el csv de Casos Covid-19 en Argentina actualizado al 25/05/2021
covid_argentina = pd.read_csv('Covid19Casos.csv')

# elimino las filas donde el testeo seea Descartado o Sospechoso (no confirmado) o Sin clasificar
# me quedo, de esta forma, solo con los casos covid CONFIRMADOS
covid_argentina = covid_argentina.drop(covid_argentina[covid_argentina.clasificacion_resumen == 'Descartado'].index)
covid_argentina = covid_argentina.drop(covid_argentina[covid_argentina.clasificacion_resumen == 'Sospechoso'].index)
covid_argentina = covid_argentina.drop(covid_argentina[covid_argentina.clasificacion_resumen == 'Sin Clasificar'].index)

# Elimino todas las columnas que no voy a utilizar en el analisis y/o visualizacion de datos
del covid_argentina['id_evento_caso']
del covid_argentina['edad_años_meses']
del covid_argentina['residencia_pais_nombre']
del covid_argentina['residencia_departamento_nombre']
del covid_argentina['carga_provincia_nombre']
del covid_argentina['fecha_inicio_sintomas']
del covid_argentina['fecha_apertura']
del covid_argentina['sepi_apertura']
del covid_argentina['fecha_internacion']
del covid_argentina['cuidado_intensivo']
del covid_argentina['fecha_cui_intensivo']
del covid_argentina['fecha_fallecimiento']
del covid_argentina['asistencia_respiratoria_mecanica']
del covid_argentina['carga_provincia_id']
del covid_argentina['origen_financiamiento']
del covid_argentina['clasificacion']
del covid_argentina['residencia_provincia_id']
del covid_argentina['residencia_departamento_id']
del covid_argentina['ultima_actualizacion']

# exporto un csv nuevo llamado Covid19CasosCorregido.csv el cual contiene exlusivamente los datos que voy a utilizar
covid_argentina.to_csv('Covid19CasosCorregido.csv', index=False, float_format=int, header=['sexo', 'edad',
                                                                                           'residencia_provincia_nombre',
                                                                                           'fallecido',
                                                                                           'clasificacion_resumen',
                                                                                           'fecha_diagnostico'])

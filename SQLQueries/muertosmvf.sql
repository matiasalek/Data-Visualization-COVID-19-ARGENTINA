/* Consultas para extraer la cantidad de muertos vs hombres */

SELECT edad, residencia_provincia_nombre, fecha_diagnostico FROM Covid19Casos
WHERE sexo = 'M' AND fallecido = 'SI'

/* Resultado: 42.368 de los muertos (56,44% del total) son hombres. 
30.699 de los muertos (40.90% del total) son mujeres. A simple vista podemos extraer como conclusion que en el total de los casos positivos de COVID-19, son menos 
los hombres contagiados, sin embargo, la mayoria de los muertos son hombres. Por lo que aunque los hombres se contagien un poco menos, el virus suele ser mas mortal.*/

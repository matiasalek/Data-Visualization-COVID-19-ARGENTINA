/* Consulta para evaluar cantidad de casos detectados en el mismo periodo de tiempo del año 2020 y 2021. */
/* Cantidad de positivos entre el 20 de Marzo de 2020 y 25 de Mayo de 2020 */
SELECT edad, sexo, residencia_provincia_nombre FROM Covid19Casos
WHERE fecha_diagnostico > '2020-03-19' AND fecha_diagnostico < '2020-05-26'

/* Resultado: 13.083 casos positivos de covid en ese periodo 
Misma consulta con diferente fecha para obtener los datos de 2021 */

SELECT edad, sexo, residencia_provincia_nombre FROM Covid19Casos
WHERE fecha_diagnostico > '2021-03-19' AND fecha_diagnostico < '2021-05-26'

/* Resultado: 1.224.563 casos positivos de covid en ese periodo
Se puede observar claramente como el la circulacion de virus en un mismo periodo de tiempo (clima, restricciones similares) es mucho mas alta.
Tambien podemos observar que el 34,14% del total de los casos desde el inicio de la pandemia se concentran en los ultimos 2 meses y 5 dias.*/

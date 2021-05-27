/* Consultas para extraer la cantidad de muertos en distintos rangos de edad:
0 a 20 años.
21 a 30 años.
31 a 40 años.
41 a 50 años.
51 a 60 años.
61 a 70 años.
71 a 80 años.
81 a 90 años.
91 a 100 años.
100 años +
*/

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad < 21
/* 214 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 20 AND edad < 31
/* 513 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 30 AND edad < 41
/* 1363 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 40 AND edad < 51
/* 3631 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 50 AND edad < 61
/* 8627 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 60 AND edad < 71
/* 17.654 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 70 AND edad < 81
/* 21.076 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 80 AND edad < 91
/* 16.547 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 90 AND edad < 101
/* 5257 fallecidos */

SELECT edad, fecha_diagnostico FROM Covid19Casos
WHERE fallecido = 'SI' AND edad > 100
/* 149 fallecidos */

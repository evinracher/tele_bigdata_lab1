# Laboratorio
En este repositorio se presenta la evidencia y el código del laboratorio de Big Data para la materia de tópicos especiales en telemática. Se desarrollo el ejercicio número 1.

### Enunciado del ejercicio:

Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

+ La estructura del archivo es: (sececon: sector económico) (archivo: dataempleados.csv)
<pre>
idemp,sececon,salary,year
3233,1234,35000,1960
3233,5434,36000,1961
1115,3432,34000,1980
3233,1234,40000,1965
1115,1212,77000,1980
1115,1412,76000,1981s3://kaparrahdatasets/datasets/otros/dataempleados.csv
1116,1412,76000,1982
</pre>

+ Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

1. El salario promedio por Sector Económico (SE)
2. El salario promedio por Empleado
3. Número de SE por Empleado que ha tenido a lo largo de la estadística

## Solución

Para dar solución a estos requerimientos, se implementaron una serie de programas escritos en python 2, que utilizan la librería mrjob. A continuación se presenta como ejecutar estos programas y su el formato de salida:

### 1. El salario promedio por Sector Económico (SE)
Ejecutar:
<pre>
python average_salary_se.py dataempleados.csv
</pre>
La salida es una lista, donde cada elemento tiene el formato:
<pre>
"identificador_sector"  salario_promedio
</pre>
### 2. El salario promedio por Empleado
Ejecutar:
<pre>
python average_salary_emp.py dataempleados.csv
</pre>
La salidad es una lista, donde cada elemento tiene el formato:
<pre>
"identificador_empleado"  salario_promedio
</pre>
### 3. Número de SE por Empleado que ha tenido a lo largo de la estadística
Ejecutar:
<pre>
python se_by_emp.py dataempleados.csv
</pre>
La salidad es una lista, donde cada elemento tiene el formato:
<pre>
identificador_empleado  [ identificador_sector, ... ]
</pre>

Acá es de notar que el segundo elmento de la pareja es una lista, con todos los sectores en los que el empleado ha estado laborando durante el periodo de muestreo.
  
## Ejecutar en EMR

Para ejecutar en EMR se utilizó la librería: boto3, que permite conectar con s3 para extraer de allí los datos a procesar y guardar la salida. Se sigue comando para ejecutar:

<pre>python programa -c mrjob.conf -r emr s3://kaparrahdatasets/datasets/otros/dataempleados.csv --output-dir s3://kaparrahdatasets/datasets/otros/output_avg_sal_se.txt</pre>

Donde **programa** puede ser cualquiera de los siguientes:
<pre>
- average_salary_emp.py
- average_salary_se.py
- se_by_emp.py
</pre>

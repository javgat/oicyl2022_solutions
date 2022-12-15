# Calculando la carga óptima en un transporte de reparto

**Dificultad**: Difícil

Nuestro objetivo es llenar un camión con mercancías de forma que se maximice el beneficio obtenido al repartirlas.

Tenemos una lista de posibles paquetes que se encuentran en el punto de salida del transporte. Cada uno de los paquetes tiene un número que indica su peso y un valor que resume el beneficio obtenido por la empresa por su reparto en tiempo y forma.

### Formato de Entrada

En la primera línea está la capacidad de la caja del camión que hay que rellenar. En la segunda línea hay un número que indica el número de posibles paquetes a considerar. Después hay una línea para cada paquete. Cada línea tiene dos números separados por espacio. El primero es el peso del paquete y el segundo el beneficio obtenido si se reparte.

### Restricciones

1 <= peso <= 10000

1 <= valor <= 10000

### Formato de Salida

La salida debe mostrar un número con el máximo beneficio que se puede obtener en un viaje, cargando el camión como mucho hasta su máxima capacidad.

### Entrada de ejemplo

```
50
10
10 15
15 25
5 5
10 10
25 35
10 15
15 20
5 10
20 30
20 25
```

### Salida de ejemplo

```
80
```
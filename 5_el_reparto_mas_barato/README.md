# El reparto más barato

**Dificultad**: Media

***Nota**: Pese a ser considerado inicialmente de dificultad media, fue el problema menos resuelto de la edición.*

Para abaratar los repartos se ha decidido subcontratar a una empresa de repartidores autónomos. Las diferentes rutas de reparto de cada día ya están diseñadas, con el peso total de los paquetes de cada una también calculado. Cada repartidor puede realizar únicamente una ruta de reparto al día, y cada uno cobra un precio fijo por trabajar un día. No todos los repartidores pueden realizar todas las rutas, pues cada uno tiene un límite en el peso que puede llevar.

### Formato de Entrada

La primera línea de la entrada constará de dos números enteros: N el número de rutas del día, y M, el número de repartidores disponibles. A continuación, en la entrada habrá N líneas. Cada línea tendrá un número entero P que será el peso total de los paquetes asociados a la ruta. Después habrá M líneas con dos enteros cada una: la cantidad que cobra el repartidor, C, y la cantidad de peso, W, que puede llevar.

### Restricciones

0 <= N <= 100000

0 <= M <= 100000

0 <= P <= 100000

0 <= C <= 100000

0 <= W <= 100000

### Formato de Salida

La salida debe mostrar el precio más barato por el que se puede realizar el reparto ese día, o, en caso de no poderse realizar, la palabra "Imposible".

### Entrada de ejemplo 0

```
2 4
2
3
1 1
5 5
4 3
3 3
```

### Salida de ejemplo 0

```
7
```

### Entrada de ejemplo 1

```
3 1
3
2
2
10 10
```

### Salida de ejemplo 1

```
Imposible
```
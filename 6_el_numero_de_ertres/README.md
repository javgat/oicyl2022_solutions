# El Número de Ertres

**Dificultad**: Difícil

En nuestra tienda online compra todo tipo de personas, entre ellas el usuario anónimo Ertres, que ha gastado millones en compras el último año. Se ha vuelto tan popular que la gente ha inventado el Número de Ertres; cada cliente de la tienda online tiene uno. El Número de Ertres es muy sencillo: el propio Ertres tiene un número de Ertres de 0, y un cliente que ha comprado un producto igual que Ertres tiene un Número de Ertres de 1. Por otra parte, una persona que no ha comprado ningún producto igual que Ertres pero sí otro producto igual que una persona con Número de Ertres igual a 1 tiene un Número de Ertres igual a 2 y así sucesivamente.

### Formato de Entrada

En la primera línea aparece un entero 1 <= P <= 1000, siendo P el número de productos que ha comprado el usuario Ertres el último año. Le siguen P líneas, cada una con una cadena de texto correspondiente a un identificador de un producto que ha comprado Ertres. A continuación, aparece en una línea independiente un entero 1 <= C <= 1000, siendo C el número de clientes para los que se desea saber su Número de Ertres. Cada cliente se describe a continuación de la misma manera que Ertres, primero un entero 1 <= N <= 1000, correspondiente al número de productos que han comprado, seguido de N líneas con identificadores de productos.

### Restricciones

1 <= P <= 1000 1 <= C <= 1000 1 <= N <= 1000

### Formato de Salida

Se espera el menor número de Ertres de cada cliente en el orden de entrada o -1 si el cliente no tiene ninguna relación.

Nota: El Número de Ertres en este problema se ha inspirado en el Número de Erdős. Este número es un modo de describir la distancia colaborativa, en lo relativo a trabajos matemáticos entre un autor y Erdős. El término fue acuñado en honor al matemático húngaro Paul Erdős, uno de los escritores más prolíficos de trabajos matemáticos.

### Entrada de ejemplo

```
3
A
B
C
3
2
A
D
2
D
E
3
X
Y
Z
```

### Salida de ejemplo

```
1
2
-1
```
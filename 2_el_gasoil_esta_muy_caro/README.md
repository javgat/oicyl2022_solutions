# El gasoil está muy caro

**Dificultad**: Fácil

Estamos pensando en cambiar la flota de furgonetas actual, que funciona por gasoil, por furgonetas eléctricas. Para poder tomar bien esta decisión, primero necesitamos conocer el gasto anual de combustible de la empresa. El consumo de cada vehículo dependerá del número de kilómetros recorridos y su consumo por cada 100km. Para ello tenemos los datos de los kilómetros de todos los vehículos de la flota de cuando pasan la revisión en el taller.

Debido a ser una filial de una multinacional japonesa, necesitamos trabajar en yenes. Por eso el valor que queremos obtener es la cantidad de gasoil consumido por la flota y calculada a un precio de 170 yenes por litro.

### Formato de Entrada

La entrada consta de N <= 2000 líneas, cada una de ellas con 2 enteros, el primero de los cuales representa los kilómetros de uno de los vehículos de la flota y el segundo el consumo de gasolina de ese vehículo en litros por cada 100Km.

### Restricciones

100 <= kilómetros <= 500000

Los kilómetros siempre serán múltiplo de 100 debido a los momentos en que pasan la revisión

6 <= consumo por cada 100km <= 25

### Formato de Salida

El total de dinero en yenes gastado en gasoil

### Entrada de ejemplo

```
1400 8
200 10
1000 7
2500 11
500 20
1100 7
600 6
```

### Salida de ejemplo

```
117300
```
# Aumento de pedidos

**Dificultad**: Fácil

Para mejorar la logística de los repartos se decide hacer un análisis simple de la cantidad de pedidos. Para el análisis se utilizarán los informes de la cantidad de pedidos de cada día. A continuación, se muestra un informe de ejemplo.

109,116,112,140,120,120,102,100,98,114

Este informe indica que el primer día hubo 109 pedidos, el segundo 116, el tercero 112, etc. El análisis que se realizará requiere conocer la cantidad de veces que hay un aumento de pedidos de un día para otro durante un período, para saber si hará falta aumentar las capacidades del centro de logística responsable en caso de que aumente con mucha frecuencia. Para hacer esto será necesario contar la cantidad de veces que el número de pedidos de un día aumenta respecto al día anterior.

Respecto al ejemplo, los cambios de aumento o decrecimiento serían los siguientes:

109 - (no aplicable, primer día)

116 - Aumenta

112 - Decrece

140 - Aumenta

120 - Decrece

120 - Sin cambio

102 - Decrece

100 - Decrece

98 - Decrece

114 - Aumenta

En este ejemplo hay 3 días en los que la cantidad de pedidos ha aumentado respecto al anterior. Esa debe ser la salida del programa.

### Formato de Entrada

Una única línea que tenga las cantidades de pedidos de cada día en orden, separadas por comas.

### Restricciones

La cantidad de pedidos de un día siempre será estrictamente menor que 100000.

### Formato de Salida

Un entero que consista en la cantidad de días en los que la cantidad de pedidos ha aumentado respecto al anterior.

### Entrada de ejemplo

```
109,116,112,140,120,120,102,100,98,114
```

### Salida de ejemplo

```
3
```
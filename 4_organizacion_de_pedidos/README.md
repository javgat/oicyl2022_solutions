# Organización de pedidos

**Dificultad**: Media

Para determinado tipo de producto, los pedidos deben realizarse con tiempo suficiente para su producción y empaquetado, de forma que se conoce con antelación la lista de los pedidos que hay que repartir durante un mes.

No todos los productos de estos pedidos tienen la misma importancia: algunos tienen que ser entregados con más celeridad que otros. En el caso de nuestra plataforma, a cada pedido se le asigna un coeficiente de importancia C. Los pedidos con mayor coeficiente deben entregarse primero. Además, contamos con clientes “premium”, en cuyo contrato hay una cláusula que prioriza sus pedidos, por lo que si el cliente es premium todos los coeficientes de sus pedidos se incrementan en una unidad. El transportista solo puede entregar 10 paquetes diarios, por lo que este sistema podría hacer que un pedido de bajo coeficiente de importancia no se entregase nunca. Para evitarlo, el coeficiente de importancia se incrementa en 1 unidad por cada día completo que pasa en el almacén. Por otra parte, se dispone también de la información del día a partir del cual el pedido estará preparado en el almacén.

### Formato de Entrada

La primera línea de la entrada es un entero N <= 10000. N representa el número de pedidos del mes.

Esta primera línea vendrá seguida de N líneas, cada una de las cuales representa un pedido.

Las líneas de pedido contienen un entero 1 <= C <= 5 correspondiente a su coeficiente de importancia, el código de pedido, que es un identificador único formado por caracteres alfanuméricos sin espacios, un entero 1 <= D <= 30 que representa el día del mes en el que estará preparado el pedido y, por último, el carácter ‘P’ si el pedido es de un cliente premium o el carácter ‘N’ si es de un cliente normal.

Estas informaciones estarán separadas por un espacio en blanco. La lista de pedidos está ordenada según la fecha de reparto D, de menor a mayor.

### Restricciones

N <= 10000 1 <= C <= 5 1 <= D <= 30

### Formato de Salida

Se espera obtener por la salida estándar un listado de los pedidos que deben ser entregados durante el mes. Por cada día en el que haya entregas se imprimirá una línea con el número de día precedido del símbolo #; a continuación, una línea por cada pedido que deba entregarse ese día, con el código de producto, y respetando el orden en que aparecen los pedidos en la entrada en caso de coincidencia en prioridad. Los días que no se entreguen pedidos no deben mostrarse. Los días de entrega llegarán como máximo hasta el día 30 (incluido). También es posible que queden pedidos sin entregar al final del mes, pero no es necesario tenerlos en cuenta en este programa, ya que se dispone de un mecanismo excepcional que se encargará de ellos.

### Entrada de ejemplo

```
17
1 Ad 1 N
1 B 1 P
2 C 1 N
3 E 1 N
1 D 2 N
4 F 4 N
4 G 4 N
2 H 4 N
2 If 4 N
2 J 4 N
3 K 4 P
5 L 4 N
5 M 4 P
2 N 4 N
3 O 4 N
2 P 4 N
3 Q 5 N
```

### Salida de ejemplo

```
#1
E
B
C
Ad
#2
D
#4
M
L
F
G
K
O
H
If
J
N
#5
P
Q
```
#!/usr/bin/env python3

from random import randint

num_pedidos = randint(1, 10e4)
pedidos = []
for i in range(num_pedidos):
    pedidos.append(randint(0, 99999))

print(*pedidos, sep=',')
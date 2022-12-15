#!/usr/bin/env python3
from random import randint

cap_camion = randint(1,10000)
print(cap_camion)
n_paqs = randint(1,1000)
print(n_paqs)
for i in range(n_paqs):
    peso = randint(1,10000)
    valor = randint(1,10000)
    print(peso, valor)
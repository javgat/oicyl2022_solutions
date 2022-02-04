#!/usr/bin/env python3

from random import randint

num_vehicles = randint(1, 2000)
for i in range(num_vehicles):
    kms = randint(1, 5000)* 100
    litres = randint(6, 25)
    print(kms, litres)
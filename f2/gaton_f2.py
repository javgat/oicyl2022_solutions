#!/usr/bin/env python3

import sys
import math

def main():
    precio = 1.59
    consumo = 0
    for line in sys.stdin:
        linea_splitted = line.split()
        kms = int(linea_splitted[0])
        consumo_100 = int(linea_splitted[1])
        consumo = consumo + consumo_100 * kms/100
    consumo = consumo * precio
    consumo = math.ceil(consumo)
    print(consumo)


if __name__ == "__main__":
    main()
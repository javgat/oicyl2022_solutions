#!/usr/bin/env python3

import sys

def main():
    precio = 170
    consumo = 0
    for line in sys.stdin:
        linea_splitted = line.split()
        kms = int(linea_splitted[0])
        consumo_100 = int(linea_splitted[1])
        consumo = consumo + consumo_100 * kms/100
    consumo = consumo * precio
    print(int(consumo))


if __name__ == "__main__":
    main()
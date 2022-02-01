#!/usr/bin/env python3
import sys

def main():
    cabecera = input().split()
    num_rutas = int(cabecera[0]) # n
    num_repartidores = int(cabecera[1]) # m
    rutas = []
    repartidores = []
    # Lectura de los datos en O(n+m) (obviamente)
    # Las ordenaciones asumo que son en O(nlogn) y O(mlogm).
    for _ in range(num_rutas):
        ruta = int(input())
        rutas.append(ruta)
    rutas.sort()
    for _ in range(num_repartidores):
        rep_split = input().split()
        repartidor = (int(rep_split[0]), int(rep_split[1]))
        repartidores.append(repartidor)
    repartidores.sort()

    cuota_total = 0
    se_puede_realizar = False

    # Cálculo de la solucion en O(n*m) como peor caso
    for peso_ruta in rutas:
        se_puede_realizar = False
        for i in range(len(repartidores)):
            if peso_ruta <= repartidores[i][1]:
                cuota_total = cuota_total + repartidores[i][0]
                repartidores.pop(i)
                se_puede_realizar = True
                break
        if not se_puede_realizar:
            break
    if se_puede_realizar:
        print(cuota_total)
    else:
        print("Imposible")

    # El total es O(n+m) + O(nlogn) + O(mlogm) + O(n*m) = O(nlogn + mlogm + n*m)

if __name__ == "__main__":
    main()
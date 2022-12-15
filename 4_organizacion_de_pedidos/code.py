#!/usr/bin/env python3

def main():
    num_peds = int(input())
    peds: dict[int, list] = {}
    for index in range(num_peds):
        data = input().split()
        prioridad = int(data[0])
        codigo = data[1]
        dia = int(data[2])
        if (data[3] == 'P'):
            prioridad += 1
        if not dia in peds:
            peds[dia] = []
        peds[dia].append((prioridad, index, codigo))
    
    dias = list(peds.keys())
    dias.sort()

    for dia in dias:
        print("#{}".format(dia))
        peds_dia = peds[dia]
        peds_dia.sort(key=lambda x: (x[0], -x[1]) ,reverse=True)
        num_peds_dia = len(peds_dia)
        for i in range(min(10, num_peds_dia)):
            print(peds_dia[i][2])
        if num_peds_dia > 10:
            new_dia = dia+1
            if new_dia <= 30:
                if new_dia not in dias:
                    position = dias.index(dia) + 1
                    dias.insert(position, new_dia)
                    peds[new_dia] = []
                for i in range(10, num_peds_dia):
                    ped = peds_dia[i]
                    peds[new_dia].append((ped[0]+1, ped[1], ped[2]))

if __name__ == "__main__":
    main()
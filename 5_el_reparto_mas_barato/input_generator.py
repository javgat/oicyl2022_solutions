from random import randint

viajes = []
trabajadores = []

for i in range(randint(1, 10000)):
    viajes.append(randint(1, 100000))

for _ in range(randint(i, 100000)):
    trabajadores.append(f"{randint(1, 100000)} {randint(1, 100000)}")

print(len(viajes), len(trabajadores))
print(*viajes, sep='\n')
print(*trabajadores, sep='\n')


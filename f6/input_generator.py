from random import randint

num_pedidos = randint(1, 10e4)
pedidos = []
for i in range(num_pedidos):
    pedidos.append(randint(0, 10000))

print(*pedidos, sep=',')
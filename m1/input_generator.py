from random import randint, choice, shuffle
import string

def random_id():
    chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return ''.join(choice(chars) for _ in range(randint(1, 24)))

pedidos = []
ids = set([''])
for dia in range(1,31):
    if randint(1,10) > 8: continue
    for _ in range(1, 17):
        importancia = randint(1,5)
        id = ''
        while id in ids: id = random_id()
        ids.add(id)
        pedidos.append(f"{importancia} {id} {dia} {'P' if randint(1,10) >= 7 else 'N'}")

shuffle(pedidos)

print(len(pedidos))
print(*pedidos, sep='\n')

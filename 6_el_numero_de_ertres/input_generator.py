#!/usr/bin/env python3
from random import randint
import string
# len(string.ascii_letters) = 52
# 52 ^ 2 > 1000, enough id
def randChar():
    seed = randint(0, len(string.ascii_letters)-1)
    while True:
        yield string.ascii_letters[seed]
        seed += 1
        seed = seed % len(string.ascii_letters)
def uniqueid():
    seq1 = randChar()
    for i in range(len(string.ascii_letters)):
        c1 = next(seq1)
        seq2 = randChar()
        for j in range(len(string.ascii_letters)):
            c2 = next(seq2)
            yield c1 + c2

n_productos_ertres = randint(1,1000)
print(n_productos_ertres)
unique_seq = uniqueid()
for i in range(n_productos_ertres):
    print(next(unique_seq))
num_clients = randint(1,1000)
print(num_clients)
for i in range(num_clients):
    n_prod_client = randint(1,1000)
    print(n_prod_client)
    unique_seq_client = uniqueid()
    for j in range(n_prod_client):
        print(next(unique_seq_client))

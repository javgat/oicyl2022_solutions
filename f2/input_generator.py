from random import randint

num_vehicles = randint(1, 10e5)
for i in range(num_vehicles):
    kms = randint(50, 50000)
    litres = randint(3, 20)
    print(kms, litres)
#!/usr/bin/env python3

def main():
    capacidad = int(input())
    num_paqs = int(input())
    paqs = []
    for _ in range(num_paqs):
        data = input().split()
        paqs.append((int(data[0]), int(data[1])))

    # Algoritmo mochila (knapsack)
    m = [[0 for w in range(capacidad+1)] for i in range(num_paqs+1)]
    for i in range(num_paqs+1):
        for w in range(capacidad+1):
            if i == 0 or w == 0:
                continue
            elif paqs[i-1][0] > w:
                m[i][w] = m[i-1][w]
            else:
                m[i][w] = max(m[i-1][w], m[i-1][w-paqs[i-1][0]] + paqs[i-1][1])
    print(m[-1][-1])

if __name__ == "__main__":
    main()
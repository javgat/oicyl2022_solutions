#!/usr/bin/env python3
# Floyd warshall es demasiado lento, deberia hacer dijkstra

from math import inf as INF
from typing import List

def floyd_warshall(old_g: List[List[int]], nV: int) -> List[List[int]]:
    g = list(map(lambda i: list(map(lambda j: j, i)), old_g))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g

def make_bidirectional(gr: List[List[int]]) -> List[List[int]]:
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] != INF:
                gr[j][i] = gr[i][j]
    return gr

def get_initial_graph(clients_prods: List[List[str]]) -> List[List[int]]:
    grafo: List[List[int]] = []
    for i, cp in enumerate(clients_prods):
        grafo.append([])
        for j, cp2 in enumerate(clients_prods):
            linked = False
            if i == j:
                grafo[i].append(0)
                continue
            for prod_name in cp:
                if prod_name in cp2:
                    grafo[i].append(1)
                    linked = True
                    break
            if not linked:
                grafo[i].append(INF)
    return grafo

def main():
    # input
    tot_rico = int(input())
    rico_prods: List[str] = []
    for _ in range(tot_rico):
        rico_prods.append(input())
    num_clients = int(input())
    clients_prods: List[List[str]] = []
    for _ in range(num_clients):
        num_prods = int(input())
        prods: List[str] = []
        for _ in range(num_prods):
            prods.append(input())
        clients_prods.append(prods)

    clients_prods.insert(0, rico_prods)
    grafo: List[List[int]] = get_initial_graph(clients_prods)
    grafo = make_bidirectional(grafo)
    grafo = floyd_warshall(grafo, num_clients+1)

    clients_ricos: List[int] = [elem[0] for elem in grafo]
    clients_ricos.pop(0)
    for res in clients_ricos:
        if res == INF:
            print(-1)
        else:
            print(res)

if __name__ == "__main__":
    main()
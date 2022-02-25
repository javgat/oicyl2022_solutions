#!/usr/bin/env python3

from math import inf as INF
from typing import List, Set, Dict

def dijkstra_to_all(vecinos: List[Dict[int, int]], source_index: int) -> List[int]:
    distances: List[int] = [INF for _ in range(len(vecinos))]
    distances[source_index] = 0
    for target in range(len(vecinos)):
        visited: Set = {}
        visited.add(source_index)
        iter_source = source_index
        min_peso = INF
        chosen_vecino = -1
        prev_peso = 0
        for _ in range((len(vecinos))):
            for vecino in vecinos[iter_source]:
                peso = vecinos[iter_source][vecino]
                if peso < min_peso:
                    min_peso = peso
                    chosen_vecino = vecino
            if min_peso+prev_peso < distances[chosen_vecino]:
                prev_peso = min_peso + prev_peso
                distances[vecino] = prev_peso
            else:
                prev_peso = distances[vecino]
            visited.add(chosen_vecino)
            hay_libre = False
            if vecinos[chosen_vecino]:
                for vecino in vecinos[chosen_vecino]:
                    if vecino not in visited:
                        hay_libre = True
                        break
            if hay_libre:
                iter_source = chosen_vecino
            else:
                pass

    


def make_bidirectional(gr: List[List[int]]) -> List[List[int]]:
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] != INF:
                gr[j][i] = gr[i][j]
    return gr

def getShortestP(gr: List[List[int]], g: int, p_index: List[int]) -> int:
    p_g = [elem for i, elem in enumerate(gr[g]) if i in p_index]
    return min(p_g)

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

def get_vecinos(grafo: List[List[int]]) -> List[Dict[int, int]]:
    vecinos: List[Dict[int, int]] = []
    for i, elem in enumerate(grafo):
        vecinos.append({})
        for j, peso in enumerate(elem):
            if peso < INF:
                vecinos[i][j] = peso
    return vecinos

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
    vecinos: List[Dict[int, int]] = get_vecinos(grafo)

    clients_ricos: List[int] = [elem[0] for elem in grafo]
    clients_ricos.pop(0)
    for res in clients_ricos:
        if res == INF:
            print(-1)
        else:
            print(res)

if __name__ == "__main__":
    main()
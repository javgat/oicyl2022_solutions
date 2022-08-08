#!/usr/bin/env python3

from math import inf as INF
import heapq
from typing import List, Set, Dict


def dijkstra(graph, dists: List[int]):
    visited = [False for _ in range(len(graph))]
    pq = [(0, root) for root in range(1, len(dists))]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        for v, l in enumerate(graph[u]):
            # if the current node's distance + distance to the node we're visiting
            # is less than the distance of the node we're visiting on file
            # replace that distance and push the node we're visiting into the priority queue
            if dists[u] + l < dists[v]:
                dists[v] = dists[u] + l
                heapq.heappush(pq, (dists[v], v))


def make_bidirectional(gr: List[List[int]]) -> List[List[int]]:
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] != INF:
                gr[j][i] = gr[i][j]
    return gr

def get_initial_graph(clients_prods: List[Set[str]]) -> List[List[int]]:
    grafo: List[List[int]] = [[] for _ in clients_prods]
    for i, cp in enumerate(clients_prods):
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
    return make_bidirectional(grafo)

def get_initial_distances(grafo: List[List[int]]) -> List[int]:
    dists = []
    for peso in grafo[0]:
        dists.append(peso)
    return dists

def main():
    # input
    tot_rico = int(input())
    rico_prods: List[str] = []
    for _ in range(tot_rico):
        rico_prods.append(input())
    num_clients = int(input())
    clients_prods: List[Set[str]] = []
    for _ in range(num_clients):
        num_prods = int(input())
        prods: Set[str] = set()
        for _ in range(num_prods):
            prods.add(input())
        clients_prods.append(prods)

    clients_prods.insert(0, rico_prods)
    grafo: List[List[int]] = get_initial_graph(clients_prods)
    dists = get_initial_distances(grafo)
    dijkstra(grafo, dists)
    dists.pop(0)
    for res in dists:
        if res == INF:
            print(-1)
        else:
            print(res)

if __name__ == "__main__":
    main()
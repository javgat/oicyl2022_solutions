#!/usr/bin/env python3
# Esta implementacion es INEFICIENTE, sirve para comprobar que algunas tardarían demasiado en hackerrank

def main():
    # input
    tot_rico = int(input())
    rico_prods = []
    for _ in range(tot_rico):
        rico_prods.append(input())
    num_clients = int(input())
    clients_prods = []
    clients_ricos = []
    for _ in range(num_clients):
        num_prods = int(input())
        prods = []
        for _ in range(num_prods):
            prods.append(input())
        clients_prods.append(prods)
        # Obtiene el valor de Rico inicial para ese cliente
        value = -1
        for prod in prods:
            for rico_p in rico_prods:
                if prod == rico_p:
                    value = 1
        clients_ricos.append(value)

    cambio = True
    while cambio:
        cambio = False
        for i in range(len(clients_prods)):
            for j in range(len(clients_prods)):
                if clients_ricos[j] != -1 and (clients_ricos[i] == -1 or clients_ricos[i] > (clients_ricos[j] + 1)):
                    conecta = False
                    prods_base = clients_prods[i]
                    prods_other = clients_prods[j]
                    for p_base in prods_base:
                        for p_other in prods_other:
                            if p_base == p_other:
                                conecta = True
                                cambio = True
                                clients_ricos[i] = clients_ricos[j] + 1
                                break
                        if conecta:
                            break
                    if conecta:
                        break
    for res in clients_ricos:
        print(res)



if __name__ == "__main__":
    main()
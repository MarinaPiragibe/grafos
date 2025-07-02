def busca_profundidade(grafo, raiz, visitados):
    visitados[raiz] = 1
    filhos = grafo[raiz]
    passos = 0
    for filho in filhos:
        if visitados[filho] == 0:
            passos += 1
            passos += busca_profundidade(grafo, filho, visitados)
    return passos

def desenhar_labirinto():
    casos_teste = int(input())

    for caso in range(0, casos_teste):
        raiz = int(input())
        qtd_vertices, qtd_arestas = map(int, input().split())
        grafo = {vertice : [] for vertice in range(0, qtd_vertices)}

        for _ in range(0, qtd_arestas):
            no_origem, no_destino = map(int, input().split())
            
            if((no_origem not in grafo[no_destino]) and (no_destino not in grafo[no_origem])):
                grafo[no_origem].append(no_destino)
                grafo[no_destino].append(no_origem)

        visitados = [0] * qtd_vertices
        passos = busca_profundidade(grafo, raiz, visitados)
        print(passos * 2)

desenhar_labirinto()
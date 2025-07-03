import heapq

INFINITO = float('inf')

def dijkstra(grafo, raiz, destino, qtd_vertices, matriz_custo):
    distancias = [INFINITO] * qtd_vertices
    visitado = [False] * qtd_vertices
    distancias[raiz] = 0
    
    heap = [(0, raiz)] 

    while heap:
        custo_atual, atual = heapq.heappop(heap)

        if visitado[atual]:
            continue
        visitado[atual] = True

        for vizinho in grafo[atual]:
            custo = matriz_custo[atual][vizinho]
            if not visitado[vizinho] and distancias[vizinho] > custo_atual + custo:
                distancias[vizinho] = custo_atual + custo
                heapq.heappush(heap, (distancias[vizinho], vizinho))
    return distancias[destino] if distancias[destino] != INFINITO else -1


continua = True
while (continua):
    qtd_vertices, qtd_arestas = map(int, input().split())
    if(qtd_vertices == 0 and qtd_arestas == 0):
        break
    grafo = {vertice: [] for vertice in range(qtd_vertices)}

    matriz_custo = [
        [0 if i == j else INFINITO for j in range(qtd_vertices)]
        for i in range(qtd_vertices)
    ]
    
    arestas_custo = []
        
    for _ in range(qtd_arestas):
        no_origem, no_destino, custo = map(int, input().split())
        no_origem -= 1
        no_destino -= 1

        arestas_custo.append((no_origem, no_destino, custo))
        grafo[no_origem].append(no_destino)
        matriz_custo[no_origem][no_destino] = custo

    arestas = set((no_origem, no_destino) for no_origem, no_destino, _ in arestas_custo)
    for no_origem, no_destino, custo in arestas_custo:
        if (no_destino, no_origem) in arestas:
            matriz_custo[no_origem][no_destino] = 0
            matriz_custo[no_destino][no_origem] = 0

    casos_teste = int(input())

    for _ in range(casos_teste):
        no_origem, no_destino = map(int, input().split())
        total_horas = dijkstra(grafo, no_origem - 1, no_destino - 1, qtd_vertices, matriz_custo)
        print(total_horas if total_horas != -1 else "Nao e possivel entregar a carta")
    print()

def veirifica_ciclo(grafo, raiz, visitados, pilha):
    visitados[raiz] = 1  
    pilha[raiz] = 1   

    for vertice in grafo[raiz]:
        if visitados[vertice] == 0: 
            if veirifica_ciclo(grafo, vertice, visitados, pilha):
                return True 
        elif pilha[vertice] == 1: 
            return True
        
    pilha[raiz] = 0 
    return False

casos_teste = int(input())

for caso in range(0, casos_teste):
    qtd_vertices, qtd_arestas = map(int, input().split())
    grafo = {vertice : [] for vertice in range(0, qtd_vertices)}

    for _ in range(0, qtd_arestas):
        no_origem, no_destino = map(int, input().split())
        no_origem -= 1
        no_destino -= 1
        
        grafo[no_origem].append(no_destino)

    visitados = [0] * qtd_vertices
    pilha = [0] * qtd_vertices

    tem_ciclo = False

    for i in range(qtd_vertices):
        if visitados[i] == 0:
            tem_ciclo = veirifica_ciclo(grafo, i, visitados, pilha)
            if tem_ciclo:
                break
    
    print('SIM' if tem_ciclo else 'NAO')
from collections import deque


alfabeto_para_indice = {letra: idx for idx, letra in enumerate('abcdefghijklmnopqrstuvwxyz')}
indice_para_alfabeto = {idx: letra for letra, idx in alfabeto_para_indice.items()}

def imprime_resultado(lista):
    lista.sort()
    for i in range(len(lista)):
        print(f'{indice_para_alfabeto[lista[i]]},', end='')
    print()

def busca_largura(grafo, raiz, visitados):
    fila = deque()
    fila.append(raiz)
    if visitados[raiz] == 1:
        return []
    
    visitados[raiz] = 1
    ordem_visita = [raiz]  

    while fila:
        atual = fila.popleft()
        for vizinho in grafo[atual]:
            if visitados[vizinho] == 0:
                visitados[vizinho] = 1
                fila.append(vizinho)
                ordem_visita.append(vizinho)

    return ordem_visita
def busca_componentes_conexas():
    casos_teste = int(input())

    for caso in range(0, casos_teste):
        qtd_vertices, qtd_arestas = map(int, input().split())
        grafo = {vertice : [] for vertice in range(0, qtd_vertices)}

        for _ in range(0, qtd_arestas):
            letra_no_origem, letra_no_destino = map(str, input().split())
            no_origem = alfabeto_para_indice[letra_no_origem]
            no_destino = alfabeto_para_indice[letra_no_destino]

            if((no_origem not in grafo[no_destino]) and (no_destino not in grafo[no_origem])):
                grafo[no_origem].append(no_destino)
                grafo[no_destino].append(no_origem)

        for vertice in grafo:
            grafo[vertice].sort()
        
        visitados = [0] * qtd_vertices
        qtd_componentes_conexas = 0

        print(f'Case #{caso+1}')

        for vertice in grafo:
            resultado = busca_largura(grafo, vertice, visitados)
            if resultado != []:
                qtd_componentes_conexas += 1
                imprime_resultado(resultado)
        print(f'{qtd_componentes_conexas} connected components\n')

busca_componentes_conexas()
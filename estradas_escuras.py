
import heapq

def kruskal():
    continua = True
    while (continua):
        qtd_vertices, qtd_arestas = map(int, input().split())
        if(qtd_vertices == 0 and qtd_arestas == 0):
            break
        HEAP = []
        custo_inicial = 0
        for _ in range(0, qtd_arestas):
            no_origem, no_destino, custo = map(int, input().split())
            custo_inicial += custo
            heapq.heappush(HEAP, (custo, no_origem - 1, no_destino - 1))

        conjuntos_disjuntos = [[vertice] for vertice in range(qtd_vertices)]
        conjunto_relativo = [vertice for vertice in range(qtd_vertices)]

        custo_total = 0
        cont = 0

        while cont < qtd_vertices - 1:
            custo, no_origem, no_destino = heapq.heappop(HEAP)
            

            if(conjunto_relativo[no_origem] != conjunto_relativo[no_destino]):
                custo_total += custo

                menor = conjunto_relativo[no_origem] 
                maior = conjunto_relativo[no_destino]

                if menor > maior:
                    menor, maior = maior, menor

                for vertice in conjuntos_disjuntos[maior]:
                    conjunto_relativo[vertice] = menor

                conjuntos_disjuntos[menor].extend(conjuntos_disjuntos[maior])
                conjuntos_disjuntos[maior] = []
                cont = cont + 1

        print(custo_inicial - custo_total)

kruskal()

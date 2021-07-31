#A Estrutura de código a seguir checa os vertices que não tenham conexão com vizinhos diretos entre si, apresentando o maior conjunto destes vertices.
#aplicação direta de conjuntos independentes, buscando o máximo conjunto

#O código trata o numero de cidades como vertices e a vizinhança entre cidades como arestas, trazendo assim o maior conjunto independente para a analise de atuação de um determinado mapa.
#implementando SetGrafo para chamadas recursivas usando o grafo definido
def SetGrafo(grafo):

    # Caso base onde o grafo não tenha vertices
    if(len(grafo) == 0):
        return []
    # Segundo caso base caso tenha somente 1 vertice:
    if(len(grafo) == 1):
        return [list(grafo.keys())[0]]
      
    # Selecionando vertice do grafo
    VerticaAtual = list(grafo.keys())[0]
    #criando grafo2 temporario
    grafo2 = dict(grafo)
    # Excluindo vertice atual 
    del grafo2[VerticaAtual]
      
    #Chamada recursiva do grafo2 Temporario que assume vertice atual ainda não verificado
    Temp1 = SetGrafo(grafo2)
    # Percorrendo vertices vizinhos:
    for v in grafo[VerticaAtual]:
        # deleta vizinho do grafo2 temporario
        if(v in grafo2):
            del grafo2[v]
      
    # Temp2 é o resultado recursivo contendo os vertices atuais + a chamada de vertices vizinhos
    Temp2 = [VerticaAtual] + SetGrafo(grafo2)
      
    # devolve o maior dentre Temp1 e Temp2 
    if(len(Temp1) > len(Temp2)):
        return Temp1
    return Temp2
  
# numero de vertices do grafo, iniciando com 1:
# esta estrutura é a representação do número de cidades abordadas no espaço amostral para a analise
V = 15
# arestas do grafo:
# Arestas representando as conexoes de vizinhança entre as cidades.
E = [ (1,2),
      (2,3),
      (2,4),
      (2,5),
      (3,4),
      (3,6),
      (3,7),
      (4,5),
      (4,7),
      (5,7),
      (5,8),
      (5,9),
      (6,7),
      (6,8),
      (6,11),
      (6,12),
      (7,8),
      (8,9),
      (8,10),
      (8,11),
      (9,10),
      (10,14),
      (10,11),
      (11,12),
      (11,14),
      (11,15),
      (12,13),
      (12,15),
      (13,15),
      (14,15),
    ]
# constroi o grafo como um dicionario onde cada posição do mesmo representa o vertice respectivamente com sua lista de vizinhos.
grafo = dict([])
#Cria o dicionario com o tamanho do numero de Vertices:
for j in range(1,V + 1):
    grafo[j] = []
#preechendo a lista com os vertices vizinhos:
for i in range(len(E)):
    # e1 e e2 recebem respectivamente o primeiro e segundo valor da tupla.
    e1, e2 = E[i]
    grafo[e1].append(e2)
    grafo[e2].append(e1)
#chamada recursiva do ConjIndepenMax com o parametro dos dados do grafo:
ConjIndepenMax = SetGrafo(grafo)
# escrevendo o conjunto de vertices independentes:
for i in ConjIndepenMax:
    print(i, end =" ")
#Função que checa se o grafo é pseudografo ou não
def check_pseudographs(graphs):
    # Lista para armazenar os identificadores dos pseudografos
    pseudographs = []

    # Itera sobre cada grafo na lista de grafos
    for graph in graphs:
        # Obtém os vértices e as arestas do grafo
        vertices = graph['vertices']
        edges = graph['edges']

        # Itera sobre cada aresta no grafo
        for edge in edges:
            # Verifica se a aresta é uma aresta autolooping
            if edge[0] == edge[1] and edge[0] in vertices:
                # Se for uma aresta autolooping, adiciona o identificador do grafo à lista de pseudografos
                pseudographs.append(graph['id'])
                # Interrompe o loop interno, pois um pseudografo foi encontrado para esse grafo
                break

    # Verifica se foram encontrados pseudografos
    if pseudographs:
        # Se houver pseudografos, imprime os identificadores encontrados
        print("Id's dos pseudografos:", pseudographs)
    else:
        # Caso contrário, imprime uma mensagem informando que não foram encontrados pseudografos
        print("Nenhum pseudografo encontrado")

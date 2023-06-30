def check_multigraphs(graphs):
    # Lista para armazenar os identificadores dos multigrafos
    multigraphs = []

    # Itera sobre cada grafo na lista de grafos
    for graph in graphs:
        # Converte as arestas em tuplas e armazena na lista "edges"
        edges = [tuple(edge) for edge in graph['edges']]

        # Verifica se o número de arestas originais é diferente do número de arestas únicas
        if len(graph['edges']) != len(set(edges)):
            # Se houver duplicatas de arestas, adiciona o identificador do grafo à lista de multigrafos
            multigraphs.append(graph['id'])

    # Verifica se foram encontrados multigrafos
    if multigraphs:
        # Se houver multigrafos, imprime os identificadores encontrados
        print("Id's dos multigrafos:", multigraphs)
    else:
        # Caso contrário, imprime uma mensagem informando que não foram encontrados multigrafos
        print("Nenhum Multigrafo encontrado")
def check_complete_graphs(graphs):
    complete_graphs = [graph['id'] for graph in graphs if is_complete(graph['vertices'], graph['edges'])]
    if complete_graphs:
        print("Grafos completos encontrados::", complete_graphs)
    else:
        print("Nenhum grafo completo encontrado.")

def is_complete(vertices, edges):
    if not vertices:
        return False
    max_edges = len(vertices) * (len(vertices) - 1) // 2
    return len(edges) == max_edges

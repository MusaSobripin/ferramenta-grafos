from funccoes.codes.desconexos.is_connected import is_connected

def check_disconnected_graphs(graphs):
    
        disconnected_graphs = []
        for graph in graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if not is_connected(vertices, edges):
                disconnected_graphs.append(graph['id'])
        if disconnected_graphs:
            print("Grafos desconexos encontrados:", disconnected_graphs)
        else:
            print("Nenhum grafo desconexo encontrado")
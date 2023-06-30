def get_vertex_degree(graphs, graph_id, vertex):
        
        # Procurar o grafo pelo ID na lista de grafos
        for graph in graphs:
            if graph['id'] == graph_id:
                edges = graph['edges']
                degree = 0

                # Calcular o grau do vértice especificado
                for edge in edges:
                    if edge[0] == vertex:
                        degree += 1
                    if edge[1] == vertex:
                        degree += 1
                
                # Exibir o grau do vértice
                print("O grau do vértice", vertex, "no grafo", graph_id, "é", degree)
                return
        # Verificar se o grafo foi encontrado
        print("Grafo '",graph_id,"' não encontrado!")
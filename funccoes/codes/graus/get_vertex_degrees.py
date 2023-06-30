#Função que verifica os graus de cada grafo a partir do ID informado
def get_vertex_degrees(graphs, graph_id):
        
        # Procurar o grafo pelo ID na lista de grafos
        for graph in graphs:
            if graph['id'] == graph_id:
                vertices = graph['vertices']
                edges = graph['edges']
                degrees = {vertex: 0 for vertex in vertices}

                # Calcular o grau de cada vértice
                for edge in edges:
                    degrees[edge[0]] += 1
                    degrees[edge[1]] += 1

                # Exibir os graus dos vértices
                print("Graus dos vértices para o grafo", graph_id)
                for vertex, degree in degrees.items():
                    print("Vértice:", vertex, "Grau:", degree)
                return
        # Verificar se o gráfico foi encontrado
        print("Grafo '",graph_id,"' não encontrado!")
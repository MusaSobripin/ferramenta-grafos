#Função que informa quais vértices do grafo são inalcançáveis a partir do vértice = A
def find_unreachable_vertices(graphs, graph_id, starting_vertex):
    found_graph = False
    
    # Procurar o gráfico pelo ID na lista de gráficos
    for graph in graphs:
        if graph['id'] == graph_id:
            found_graph = True
            vertices = graph['vertices']
            edges = graph['edges']
            starting_vertex = starting_vertex.strip('"')
            
            # Lista para armazenar os vértices alcançáveis
            reachable_vertices = [starting_vertex]
            
            # Fila para realizar a busca em largura
            queue = [starting_vertex]
            
            # Realizar a busca em largura
            while queue:
                current_vertex = queue.pop(0)
                for edge in edges:
                    if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                        reachable_vertices.append(edge[1])
                        queue.append(edge[1])
                    elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                        reachable_vertices.append(edge[0])
                        queue.append(edge[0])
            
            # Lista para armazenar os vértices inalcançáveis
            unreachable_vertices = [vertex for vertex in vertices if vertex not in reachable_vertices]
            
            # Exibir os vértices inalcançáveis
            print("Vértices inalcançáveis a partir de", starting_vertex, "no grafo", graph_id, "são:", unreachable_vertices)
            break
    
    # Verificar se o gráfico foi encontrado
    if not found_graph:
        print("Grafo '",graph_id,"' não encontrado!")
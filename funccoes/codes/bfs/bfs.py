def bfs(graphs, graph_id, start_vertex, end_vertex):
        found_graph = False
        for graph in graphs:
            if graph['id'] == graph_id:
                found_graph = True
                vertices = graph['vertices']
                edges = graph['edges']
                start_vertex = start_vertex.strip('"')
                end_vertex = end_vertex.strip('"')
                visited = {vertex: False for vertex in vertices}
                queue = [(start_vertex, [start_vertex])]
                while queue:
                    current_vertex, path = queue.pop(0)
                    visited[current_vertex] = True
                    if current_vertex == end_vertex:
                        print("Caminho encontrado no grafo", graph_id, ":", " -> ".join(path))
                        break
                    for edge in edges:
                        if edge[0] == current_vertex and not visited[edge[1]]:
                            queue.append((edge[1], path + [edge[1]]))
                        elif edge[1] == current_vertex and not visited[edge[0]]:
                            queue.append((edge[0], path + [edge[0]]))
                else:
                    print("Nenhum caminho encontrado no grafo", graph_id, "entre", start_vertex, "e", end_vertex)
                break
        if not found_graph:
            print("Grafo '",graph_id,"' não encontrado!")
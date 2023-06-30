def is_connected(vertices, edges):
    if not vertices:
        return False
    reachable_vertices = set()
    queue = [vertices[0]]
    while queue:
        current_vertex = queue.pop(0)
        reachable_vertices.add(current_vertex)
        for edge in edges:
            if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                reachable_vertices.add(edge[1])
                queue.append(edge[1])
            elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                reachable_vertices.add(edge[0])
                queue.append(edge[0])
    return len(reachable_vertices) == len(vertices)
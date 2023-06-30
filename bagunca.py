from asyncio import as_completed
import json
import sys

class GraphTool:
    def __init__(self):
        self.graphs = []

    def load_graphs_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.graphs = data['graphs']
                print("Gráficos carregados com sucesso de", filename)
        except FileNotFoundError:
            print("Arquivo não encontrado:", filename)

    def check_multigraphs(self):
        multigraphs = []
        for graph in self.graphs:
            edges = [tuple(edge) for edge in graph['edges']]
            if len(graph['edges']) != len(set(edges)):
                multigraphs.append(graph['id'])
        if multigraphs:
            print("Gráficos multigrafos encontrados - IDs:", multigraphs)
        else:
            print("Nenhum gráfico multigrafo encontrado")

    def check_pseudographs(self):
        pseudographs = []
        for graph in self.graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            for edge in edges:
                if edge[0] == edge[1] and edge[0] in vertices:
                    pseudographs.append(graph['id'])
                    break
        if pseudographs:
            print("Gráficos pseudografos encontrados - IDs:", pseudographs)
        else:
            print("Nenhum gráfico pseudografo encontrado")
   
    def check_disconnected_graphs(self):
        disconnected_graphs = []
        for graph in self.graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if not self.is_connected(vertices, edges):
                disconnected_graphs.append(graph['id'])
        if disconnected_graphs:
            print("Gráficos desconexos encontrados - IDs:", disconnected_graphs)
        else:
            print("Nenhum gráfico desconexo encontrado")

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
    
    def check_complete_graphs(graphs):
        complete_graphs = []
        for graph in graphs:
            vertices = graph['vertices']
            edges = graph['edges']
            if as_completed(vertices, edges):
                complete_graphs.append(graph['id'])
        if complete_graphs:
            print("Complete graphs found:", complete_graphs)
        else:
            print("No complete graphs found")
    def is_complete(vertices, edges):
        if not vertices:
            return False
        max_edges = len(vertices) * (len(vertices) - 1) // 2
        return len(edges) == max_edges

    def get_vertex_degrees(self, graph_id):
        found_graph = False
        for graph in self.graphs:
            if graph['id'] == graph_id:
                found_graph = True
                vertices = graph['vertices']
                edges = graph['edges']
                degrees = {vertex: 0 for vertex in vertices}
                for edge in edges:
                    degrees[edge[0]] += 1
                    degrees[edge[1]] += 1
                print("Graus dos vértices no gráfico", graph_id)
                for vertex, degree in degrees.items():
                    print("Vértice:", vertex, "Grau:", degree)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def get_vertex_degree(self, graph_id, vertex):
        found_graph = False
        for graph in self.graphs:
            if graph['id'] == graph_id:
                found_graph = True
                edges = graph['edges']
                degree = 0
                for edge in edges:
                    if edge[0] == vertex:
                        degree += 1
                    if edge[1] == vertex:
                        degree += 1
                print("Grau do vértice", vertex, "no gráfico", graph_id, "é", degree)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def find_reachable_vertices(self, graph_id, starting_vertex):
        found_graph = False
        for graph in self.graphs:
            if graph['id'] == graph_id:
                found_graph = True
                vertices = graph['vertices']
                edges = graph['edges']
                starting_vertex = starting_vertex.strip('"')
                reachable_vertices = [starting_vertex]
                queue = [starting_vertex]
                while queue:
                    current_vertex = queue.pop(0)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                            reachable_vertices.append(edge[1])
                            queue.append(edge[1])
                        elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                            reachable_vertices.append(edge[0])
                            queue.append(edge[0])
                print("Vértices alcançáveis a partir de", starting_vertex, "no gráfico", graph_id, "são:", reachable_vertices)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def find_unreachable_vertices(self, graph_id, starting_vertex):
        found_graph = False
        for graph in self.graphs:
            if graph['id'] == graph_id:
                found_graph = True
                vertices = graph['vertices']
                edges = graph['edges']
                starting_vertex = starting_vertex.strip('"')
                reachable_vertices = [starting_vertex]
                queue = [starting_vertex]
                while queue:
                    current_vertex = queue.pop(0)
                    for edge in edges:
                        if edge[0] == current_vertex and edge[1] not in reachable_vertices:
                            reachable_vertices.append(edge[1])
                            queue.append(edge[1])
                        elif edge[1] == current_vertex and edge[0] not in reachable_vertices:
                            reachable_vertices.append(edge[0])
                            queue.append(edge[0])
                unreachable_vertices = [vertex for vertex in vertices if vertex not in reachable_vertices]
                print("Vértices inalcançáveis a partir de", starting_vertex, "no gráfico", graph_id, "são:", unreachable_vertices)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def bfs(self, graph_id, start_vertex, end_vertex):
        found_graph = False
        for graph in self.graphs:
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
                        print("Caminho encontrado no gráfico", graph_id, ":", " -> ".join(path))
                        break
                    for edge in edges:
                        if edge[0] == current_vertex and not visited[edge[1]]:
                            queue.append((edge[1], path + [edge[1]]))
                        elif edge[1] == current_vertex and not visited[edge[0]]:
                            queue.append((edge[0], path + [edge[0]]))
                else:
                    print("Nenhum caminho encontrado no gráfico", graph_id, "entre", start_vertex, "e", end_vertex)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def dfs(self, graph_id, start_vertex, end_vertex):
        found_graph = False
        for graph in self.graphs:
            if graph['id'] == graph_id:
                found_graph = True
                vertices = graph['vertices']
                edges = graph['edges']
                start_vertex = start_vertex.strip('"')
                end_vertex = end_vertex.strip('"')
                visited = {vertex: False for vertex in vertices}
                stack = [(start_vertex, [start_vertex])]
                while stack:
                    current_vertex, path = stack.pop()
                    visited[current_vertex] = True
                    if current_vertex == end_vertex:
                        print("Caminho encontrado no gráfico", graph_id, ":", " -> ".join(path))
                        break
                    for edge in edges:
                        if edge[0] == current_vertex and not visited[edge[1]]:
                            stack.append((edge[1], path + [edge[1]]))
                        elif edge[1] == current_vertex and not visited[edge[0]]:
                            stack.append((edge[0], path + [edge[0]]))
                else:
                    print("Nenhum caminho encontrado no gráfico", graph_id, "entre", start_vertex, "e", end_vertex)
                break
        if not found_graph:
            print("Gráfico não encontrado:", graph_id)

    def run_command(self, command): # Dicionário que mapeia comandos para métodos correspondentes
        
        switch = {
            'ler': self.handle_load_command,
            'multigrafos': self.handle_check_multigraphs_command,
            'pseudografos': self.handle_check_pseudographs_command,
            'desconexos': self.handle_check_disconnected_graphs_command,
            'completos': self.handle_check_complete_graphs_command,
            'graus': self.handle_get_vertex_degrees_command,
            'grau': self.handle_get_vertex_degree_command,
            'alcancaveis': self.handle_find_reachable_vertices_command,
            'inalcancaveis': self.handle_find_unreachable_vertices_command,
            'bfs': self.handle_bfs_command,
            'dfs': self.handle_dfs_command,
            'sair': sys.exit,
        }

        
        action = switch.get(command[0], None) # Obtém o método correspondente ao comando
        if action:
            action(command) # Executa o método correspondente passando o comando como argumento
        else:
            print("Comando inválido")

    # Métodos para lidar com cada comando específico
    def handle_load_command(self, command):
        if len(command) == 3 and command[1] == 'arquivo':
            self.load_graphs_from_file(command[2])

    def handle_check_multigraphs_command(self, command):
        self.check_multigraphs()

    def handle_check_pseudographs_command(self, command):
        self.check_pseudographs()

    def handle_check_disconnected_graphs_command(self, command):
        self.check_disconnected_graphs()

    def handle_check_complete_graphs_command(self, command):
        self.check_complete_graphs()

    def handle_get_vertex_degrees_command(self, command):
        if len(command) == 3:
            graph_id = int(command[2].split('=')[1])
            self.get_vertex_degrees(graph_id)

    def handle_get_vertex_degree_command(self, command):
        if len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            vertex = command[3].split('=')[1].strip('"')
            self.get_vertex_degree(graph_id, vertex)

    def handle_find_reachable_vertices_command(self, command):
        if len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            self.find_reachable_vertices(graph_id, starting_vertex)

    def handle_find_unreachable_vertices_command(self, command):
        if len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'")
            self.find_unreachable_vertices(graph_id, starting_vertex)

    def handle_bfs_command(self, command):
        if len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            self.bfs(graph_id, start_vertex, end_vertex)

    def handle_dfs_command(self, command):
        if len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            self.dfs(graph_id, start_vertex, end_vertex)

def main():
    graph_tool = GraphTool()
    while True:
        user_input = input("Digite um comando: ")
        command = user_input.split()
        graph_tool.run_command(command)

if __name__ == '__main__':
    main()

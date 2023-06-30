import sys
from funccoes.codes.alcancaveis.find_reachable_vertices import find_reachable_vertices
from funccoes.codes.bfs.bfs import bfs
from funccoes.codes.comando.load_graphs import load_graphs_from_file
from funccoes.codes.completos.check_complete_graphs import check_complete_graphs
from funccoes.codes.desconexos.check_disconnected_graphs import check_disconnected_graphs
from funccoes.codes.dfs.dsf import dfs
from funccoes.codes.grau.get_vertex_degree import get_vertex_degree
from funccoes.codes.graus.get_vertex_degrees import get_vertex_degrees
from funccoes.codes.inalcancaveis.find_unreachable_vertices import find_unreachable_vertices
from funccoes.codes.multigrafos.check_multigraphs import check_multigraphs
from funccoes.codes.pseudografos.check_pseudogaphs import check_pseudographs

#Comandos para execução dos grafos
def command_handler(command, graphs):
    if command[0] == 'grafos':
        if len(command) == 3 and command[1] == 'carregar':
            graphs = load_graphs_from_file(command[2])
        elif command[1] == 'multigrafos':
            check_multigraphs(graphs)
        elif command[1] == 'pseudografos':
            check_pseudographs(graphs)
        elif command[1] == 'desconexos':
            check_disconnected_graphs(graphs)
        elif command[1] == 'completos':
            check_complete_graphs(graphs)
        elif command[1] == 'graus' and len(command) == 3:
            graph_id = int(command[2].split('=')[1])
            get_vertex_degrees(graphs, graph_id)
        elif command[1] == 'grau' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            vertex = command[3].split('=')[1].strip('"')
            get_vertex_degree(graphs, graph_id, vertex)
        elif command[1] == 'alcancaveis' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            find_reachable_vertices(graphs, graph_id, starting_vertex)
        elif command[1] == 'inalcancaveis' and len(command) == 4:
            graph_id = int(command[2].split('=')[1])
            starting_vertex = command[3].split('=')[1].strip("'").strip('"')
            find_unreachable_vertices(graphs, graph_id, starting_vertex)
        elif command[1] == 'bfs' and len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            bfs(graphs, graph_id, start_vertex, end_vertex)
        elif command[1] == 'dfs' and len(command) == 5:
            graph_id = int(command[2].split('=')[1])
            start_vertex = command[3].split('=')[1].strip('"')
            end_vertex = command[4].split('=')[1].strip('"')
            dfs(graphs, graph_id, start_vertex, end_vertex)
        elif command[1] == 'sair':
            sys.exit()
        else:
            print("Comando inválido!")
    else:
        print("Comando inválido!")
    return graphs
import json
import sys

from funccoes.codes.comando.command import command_handler

#Classe GraphTool (Principal)
class GraphTool:
    def __init__(self):
        self.graphs = []
    
    #Chamada da função de comandos
    def run_command(self, command):
        self.graphs = command_handler(command, self.graphs)

#Função Main do código
def main():
    graph_tool = GraphTool()
    while True:
        try:
            user_input = input()
            command = user_input.split()
            graph_tool.run_command(command)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("Teclado bloqueado")
            break

if __name__ == '__main__':
    main()

"""
--------- Comandos para execução ---------
| grafos carregar graphs.json             | 
| grafos multigrafos                      |
| grafos pseudografos                     |
| grafos desconexos                       |
| grafos completos                        |
| grafos graus id=1                       |
| grafos grau id=1 vertice="A"            |
| grafos alcancaveis id=1 partida="A"     |
| grafos inalcancaveis id=1 partida="A"   |
| grafos bfs id=1 partida="A" chegada="A" |
| grafos dfs id=1 partida="A" chegada="A" |
-------------------------------------------
"""
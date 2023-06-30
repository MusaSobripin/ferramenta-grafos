import json

#Função para ler arquivo JSON
def load_graphs_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            graphs = data['graphs']
            print("Arquivo '", filename, "' carregado com sucesso!")
            return graphs
    except FileNotFoundError:
        print("Arquivo '", filename, "' não encontrado!")
        return None
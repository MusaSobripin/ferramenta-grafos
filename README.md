# Você deve implementar uma ferramenta chamada "grafos" com intereface em linha de comando. Abaixo estão exemplo de chamadas da ferramenta:
<\br><\br>
<\br>{c:green}[fa=check-circle /]{/c} **grafos carrregar arquivo.json** //deve carregar os grafos contidos no arquivo .json
<\br>{c:green}[fa=check-circle /]{/c} **grafos multigrafos** //deve informar quais grafos do arquivo carregado são multigrafos
<\br>**grafos pseudografos** //deve informar quais grafos do arquivo carregado são pseudografos
<\br>**grafos desconexos** //deve informar quais grafos do arquivo carregado são desconexos
<\br>**grafos completos** //deve informar quais grafos do arquivo carregado são completos
<\br>**grafos graus id=1** //deve informar quais os graus dos vértices do grafo de id=1
<\br>**grafos grau id=1 vertice="A"**  //deve informar o grau do vértice=A do grafo id=1 
<\br>**grafos alcancaveis partida="A"**  //deve informar quais vértices do grafo são alcançáveis a partir do vértice = A
<\br>**grafos inalcancaveis partida="A"** //deve informar quais vértices do grafo são inalcançáveis a partir do vértice = A
<\br>**grafos bfs partida="A" chegada="B"** //deve informar o caminho partindo do vértice = A até chegar no vértice=B usando o algoritmo BFS.
<\br>**grafos dfs partida="A" chegada="B"** //deve informar o caminho partindo do vértice = A até chegar no vértice=B usando o algoritmo DFS.
<\br>**grafos sair** // finaliza a execução da ferramenta

import numpy as np
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Função para gerar o labirinto aleatório
def gerar_labirinto(linhas, colunas, prob_obstaculo=0.3):
    labirinto = np.random.choice([0, 1], size=(linhas, colunas), p=[1 - prob_obstaculo, prob_obstaculo])
    labirinto[0, 0] = 0  # Ponto de início
    labirinto[linhas-1, colunas-1] = 0  # Ponto de fim
    return labirinto

# Função heurística (distância de Manhattan)
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Função do algoritmo a* para encontrar o caminho mais curto
def a_star(labirinto, inicio, fim):
    linhas, colunas = labirinto.shape
    open_list = []
    came_from = {}
    g_score = {inicio: 0}
    f_score = {inicio: heuristica(inicio, fim)}
    
    heappush(open_list, (f_score[inicio], inicio))
    
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    
    while open_list:
        _, atual = heappop(open_list)
        
        if atual == fim:
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            return caminho[::-1]
        
        for movimento in movimentos:
            vizinho = (atual[0] + movimento[0], atual[1] + movimento[1])
            
            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas and labirinto[vizinho] == 0:
                g_tentativo = g_score[atual] + 1
                
                if vizinho not in g_score or g_tentativo < g_score[vizinho]:
                    came_from[vizinho] = atual
                    g_score[vizinho] = g_tentativo
                    f_score[vizinho] = g_tentativo + heuristica(vizinho, fim)
                    heappush(open_list, (f_score[vizinho], vizinho))
    
    return []  

# Função para visualizar o labirinto e o caminho encontrado
def visualizar_labirinto(labirinto, caminho=[]):
    plt.imshow(labirinto, cmap='gray', origin='upper')
    
    # insere o caminho com pontos vermelhos
    for (x, y) in caminho:
        plt.plot(y, x, 'ro')  
    
    plt.show()

# Função principal para executar o projeto
def main():
    linhas, colunas = 20, 20  # Tamanho do labirinto
    labirinto = gerar_labirinto(linhas, colunas)
    
    inicio = (0, 0)
    fim = (linhas - 1, colunas - 1)
    
    caminho = a_star(labirinto, inicio, fim)

    visualizar_labirinto(labirinto, caminho)

if __name__ == "__main__":
    main()

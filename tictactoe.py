# Criando o tabuleiro vazio
tabuleiro = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

def imprimir_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

def verificar_vitoria(jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
           tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def jogar_jogo_da_velha():
    jogador = "X"
    jogadas = 0
    
    while True:
        imprimir_tabuleiro()
        
        try:
            linha = int(input(f"Jogador {jogador}, escolha a linha (1, 2, 3): ")) - 1
            coluna = int(input(f"Jogador {jogador}, escolha a coluna (1, 2, 3): ")) - 1
            
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Escolha inválida. Tente novamente.")
                continue

            if tabuleiro[linha][coluna] == "_":
                tabuleiro[linha][coluna] = jogador
                jogadas += 1
                
                if verificar_vitoria(jogador):
                    imprimir_tabuleiro()
                    print(f"Parabéns! Jogador {jogador} venceu!")
                    break
                elif jogadas == 9:
                    imprimir_tabuleiro()
                    print("Empate!")
                    break
                else:
                    jogador = "O" if jogador == "X" else "X"
            else:
                print("Essa posição já está ocupada. Escolha outra.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
        except IndexError:
            print("Escolha fora do intervalo. Tente novamente.")

if __name__ == "__main__":
    jogar_jogo_da_velha()

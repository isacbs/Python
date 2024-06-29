def imprimir(tabuleiro):
    for i in range(len(tabuleiro)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(tabuleiro[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tabuleiro[i][j])
            else:
                print(str(tabuleiro[i][j]) + " ", end="")

def encontrar(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == 0:
                return (i, j)  # linha, coluna
    return None

# Validação da linha, coluna e do sudoku completo
def valido(tabuleiro, num, pos):
    for i in range(len(tabuleiro[0])):
        if tabuleiro[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(tabuleiro)):
        if tabuleiro[i][pos[1]] == num and pos[0] != i:
            return False

    tabela_x = pos[1] // 3
    tabela_y = pos[0] // 3

    for i in range(tabela_y * 3, tabela_y * 3 + 3):
        for j in range(tabela_x * 3, tabela_x * 3 + 3):
            if tabuleiro[i][j] == num and (i, j) != pos:
                return False

    return True

def resolver(tabuleiro):
    vazio = encontrar(tabuleiro)
    if not vazio:
        return True
    else:
        linha, coluna = vazio

    for i in range(1, 10):
        if valido(tabuleiro, i, (linha, coluna)):
            tabuleiro[linha][coluna] = i

            if resolver(tabuleiro):
                return True

            tabuleiro[linha][coluna] = 0
    return False

tabuleiro = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

imprimir(tabuleiro)
resolver(tabuleiro)
print("\nSolução:\n")
imprimir(tabuleiro)

def sudoku_valido(tabuleiro):
    for i in range(9):
        linha = []
        coluna = []
        bloco = []

        for j in range(9):
            # Verifica linhas
            if tabuleiro[i][j] != "." and tabuleiro[i][j] in linha:
                return False
            elif tabuleiro[i][j] != ".":
                linha.append(tabuleiro[i][j])

            # Verifica colunas
            if tabuleiro[j][i] != "." and tabuleiro[j][i] in coluna:
                return False
            elif tabuleiro[j][i] != ".":
                coluna.append(tabuleiro[j][i])

            # Verifica bloco 3x3
            lin = 3 * (i // 3) + j // 3
            col = 3 * (i % 3) + j % 3
            valor = tabuleiro[lin][col]
            if valor != "." and valor in bloco:
                return False
            elif valor != ".":
                bloco.append(valor)
    
    return True


# Exemplo de uso
entrada = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
saida = sudoku_valido(entrada)
print("Sudoku válido?", saida)

"""
O objetivo deste exercício é verificar se um tabuleiro de Sudoku 9x9 segue as três regras principais do jogo, que são:

- Cada linha deve conter apenas números de 1 a 9, sem repetições.
- Cada coluna deve conter apenas números de 1 a 9, sem repetições.
- Cada um dos nove blocos 3x3 deve conter apenas números de 1 a 9, sem repetições.

Observação: Os espaços vazios do tabuleiro são representados pelo caractere ".".
"""

"""
A função sudoku_valido recebe como parâmetro uma matriz 9x9 representando o tabuleiro do Sudoku.
O objetivo da função é verificar se esse tabuleiro está válido de acordo com as regras do jogo.
"""
def sudoku_valido(tabuleiro):
    
    """
    A função começa com um loop de i que vai de 0 a 8, ou seja, percorre cada linha, coluna e bloco ao mesmo tempo.
    """
    for i in range(9):
        """ 
        Dentro do for, são inicializadas três listas vazias: 
        - linha: responsável por guardar os números que já apareceram na linha i.
        - coluna: responsável por guardar os números que já apareceram na coluna i.
        - bloco: responsável por guardar os números que já apareceram no bloco 3x3 correspondente a i.
        """
        linha = []
        coluna = []
        bloco = []

        """Este laço interno percorre de 0 a 8, ou seja, as 9 posições da linha, da coluna e do bloco."""
        for j in range(9):

            """ 
            VERIFICAÇÃO DE LINHAS
            Esta estrutura de condição é responsável por verificar o elemento da linha i, coluna j.
            Se for diferente de "." e já estiver na lista 'linha', então há repetição ⇒ retorna False.
            Caso contrário, o número é adicionado à lista 'linha'.
            """
            if tabuleiro[i][j] != "." and tabuleiro[i][j] in linha:
                return False
            elif tabuleiro[i][j] != ".":
                linha.append(tabuleiro[i][j])

            """ 
            VERIFICAÇÃO DE COLUNAS
            Verifica a coluna i, na linha j. Segue a mesma lógica da linha: se for número repetido, retorna False.
            """
            if tabuleiro[j][i] != "." and tabuleiro[j][i] in coluna:
                return False
            elif tabuleiro[j][i] != ".":
                coluna.append(tabuleiro[j][i])

            """
            VERIFICAÇÃO DO BLOCO 3x3
            
            Nesta parte do código, o objetivo é usar 'i' para determinar qual bloco está sendo verificado, 
            e 'j' para percorrer as 9 posições internas desse bloco. 
            
            Sendo assim, a fórmula: 
                lin = 3 * (i // 3) + j // 3 ⇒ determina a linha dentro do bloco
                col = 3 * (i % 3) + j % 3 ⇒ determina a coluna dentro do bloco

            Com isso, tabuleiro[lin][col] acessa corretamente cada célula de um dos 9 blocos 3x3.
            """
            lin = 3 * (i // 3) + j // 3
            col = 3 * (i % 3) + j % 3
            valor = tabuleiro[lin][col]
            
            """Verifica se o valor do bloco já apareceu antes. Se sim ⇒ retorna False."""
            if valor != "." and valor in bloco:
                return False
            elif valor != ".":
                bloco.append(valor)
    
    """Se nenhuma repetição for encontrada, retorna True, indicando que o tabuleiro é válido."""
    return True

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

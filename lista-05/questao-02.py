import random
from collections import Counter

"""
Função utilizada para criar o baralho. 

A função inicializa duas listas, uma com as cartas e outra com os naipes.

Após isso, é inicializada a lista baralho[], a qual está sendo usada dentro da estrutura de dois loops for aninhandos. De modo, a preencher o baralho com os números das cartas e seus naipes.

Após preencher o baralho, é utilizado a função shuffle() do próprio python, utilizada para alterar a ordem dos elementos da lista.

Por fim, a função retorna a lista baralho[]
"""
def criar_baralho():
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Valete", "Dama", "Rei", "Às"]
    naipes = ["ouros", "copas", "espadas", "paus"]
    
    baralho = []
    for c in cartas:
        for n in naipes:
            baralho.append({"carta": c, "naipe": n})

    random.shuffle(baralho) # Função python utilizada para alterar a ordem dos elementos de uma lista
    return baralho

""" 
A função definir_valor_carta(), recebe como parâmetro uma carta e retorna o valor da respectiva carta.

Para isso, foi criado um dicionário que armazena o valor de cada carta. 
"""
def retorna_valor_carta(carta):
    ordem_cartas = {
        2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
        7: 7, 8: 8, 9: 9, 10: 10,
        "Valete": 11, "Dama": 12, "Rei": 13, "Às": 14
    }
    return ordem_cartas[carta["carta"]]


""" 
A Classe Classificacao() possui um construtor que inicializa: 

dicionário mao: Os valores do dicionário estaram ordenadas, pois está sendo chamado a função quick_sort();
lista valores: Armazena os valores das cartas do dicionário mão.
lista naipes: Armazena os naipes das cartas do dicionário mão.
dicionário frequencias: Armazena a contagem de cada valor das cartas do dicionário mão.
lista frequencias_ordenadas: Armazena a frequência de aparecimento dos valores em ordem descrescente.

Em seguida, temos a definição dos respectivos métodos de classificação do Poker.
"""

class Classificacao:
    def __init__(self, mao):
        self.mao = mao
        self.valores = [retorna_valor_carta(c) for c in self.mao]  
        self.valores_ordenados = sorted(self.valores)
        self.naipes = [c['naipe'] for c in self.mao]              
        self.frequencias = self.contar_frequencias()               
        self.frequencias_ordenadas = self.get_frequencias_ordenadas() 

    def contar_frequencias(self):
        """Conta quantas vezes cada valor aparece na mão e retorna um dicionário"""
        frequencias = {}
        for v in set(self.valores):
            frequencias[v] = self.valores.count(v)
        return frequencias

    def get_frequencias_ordenadas(self):
        """Retorna uma lista com as frequências dos valores em ordem decrescente."""
        return sorted(self.frequencias.values(), reverse=True)

    def eh_flush(self):
        """Verifica se todas as cartas têm o mesmo naipe (Flush)."""
        for naipe in self.naipes:
            if naipe != self.naipes[0]:
                return False
        return True

    def eh_sequencia(self):
        """Verifica se os valores estão em sequência numérica (normal ou com Ás baixo)."""
        for i in range(1, len(self.valores_ordenados)):
            if self.valores_ordenados[i] != self.valores_ordenados[i - 1] + 1:
                return self.eh_sequencia_ace_baixo()
        return True


    def eh_sequencia_ace_baixo(self):
        """Verifica se a mão é a sequência especial A, 2, 3, 4, 5 (Ás como 1)."""
        valores_convertidos = [1 if v == 14 else v for v in self.valores]
        return set(valores_convertidos) == {1, 2, 3, 4, 5}


    def eh_royal_flush(self):
        """Verifica se a mão é Royal Flush: sequência 10-A do mesmo naipe."""
        return self.eh_flush() and set(self.valores_ordenados) == {10, 11, 12, 13, 14}

    def eh_straight_flush(self):
        """Verifica se a mão é Straight Flush: sequência do mesmo naipe."""
        return self.eh_flush() and self.eh_sequencia()

    def eh_quadra(self):
        """Verifica se a mão tem quatro cartas iguais (Quadra)."""
        return self.frequencias_ordenadas == [4, 1]

    def eh_full_house(self):
        """Verifica se a mão tem três cartas iguais e um par (Full House)."""
        return self.frequencias_ordenadas == [3, 2]

    def eh_trinca(self):
        """Verifica se a mão tem três cartas iguais (Trinca)."""
        return self.frequencias_ordenadas == [3, 1, 1]

    def eh_dois_pares(self):
        """Verifica se a mão tem dois pares (Dois Pares)."""
        return self.frequencias_ordenadas == [2, 2, 1]

    def eh_um_par(self):
        """Verifica se a mão tem um par (Um Par)."""
        return self.frequencias_ordenadas == [2, 1, 1, 1]

    """ 
    O método classificar executa uma lista de condicionais. No caso de um dos condicionais resultar em True, o método retorna o nome da classificação da mão, e uma pontuação para a mesma.
    """
    def classificar(self):
        """Classifica a mão de acordo com as regras do poker e retorna o nome e a pontuação."""
        if self.eh_royal_flush():
            return "Royal Flush", 10
        if self.eh_straight_flush():
            return "Straight Flush", 9
        if self.eh_quadra():
            return "Quadra", 8
        if self.eh_full_house():
            return "Full House", 7
        if self.eh_flush():
            return "Flush", 6
        if self.eh_sequencia():
            return "Sequência", 5
        if self.eh_trinca():
            return "Trinca", 4
        if self.eh_dois_pares():
            return "Dois Pares", 3
        if self.eh_um_par():
            return "Um Par", 2
        return "Carta Alta", 1
    
""" 
A função comparar_maos() recebe como parâmetro as duas mãos dos jogadores. 

Após isso, são criadas duas instâncias da classe Classificacao(), onde passamos por parâmetros aos mãos de cartas dos jogadores. 

Em seguida, criamos as varáveis tipo e pontos para armazenar o resultado da classificação. A variável tipo vai armazenar o nome da classificação das cartas de cada jogador, enquanto que a variável pontos armazena a respectiva pontuação atribuída para aquele tipo de classificação. 

Desse modo, o programa primeiro ordena em ordem descrecente as cartas, onde a key=retorna_valor_carta informa à função sorted() que a ordenação deve ser feita com base no valor retornado pela função retorna_valor_carta(). Isso é feito para os dois jogadores. 

Após isso, é realiza um loop for no dicionário de cartas da mão 01 e da mão 02 para exibir as cartas dos jogadores. 

No fim, é verificado qual dois jogadores possui maior pontuação, para então decidir o vencedor.

Em casos de empate, 

"""
def comparar_maos(mao1, mao2):
    classificacao_mao_1 = Classificacao(mao1)
    classificacao_mao_2 = Classificacao(mao2)
    
    tipo1, pontos1 = classificacao_mao_1.classificar()
    tipo2, pontos2 = classificacao_mao_2.classificar()    
    
    mao_ordenada_1 = sorted(classificacao_mao_1.mao, key=retorna_valor_carta, reverse=True)
    mao_ordenada_2 = sorted(classificacao_mao_2.mao, key=retorna_valor_carta, reverse=True)
    
    print("\nMão do Jogador 1:")
    for carta in mao_ordenada_1:
        print(f"  {carta['carta']} de {carta['naipe']}")

    print("Classificação", tipo1)
    
    print("\nMão do Jogador 2:")
    for carta in mao_ordenada_2:
        print(f"  {carta['carta']} de {carta['naipe']}")

    print("Classificação", tipo2)

    print("\nResultado:")
    if pontos1 > pontos2:
        print("Jogador 1 venceu!")
    elif pontos2 > pontos1:
        print("Jogador 2 venceu!")
    else:
        resultado = desempatar_maos(tipo1, mao1, mao2)
        if resultado == 1:
            print("Jogador 1 venceu no desempate!")
        elif resultado == 2:
            print("Jogador 2 venceu no desempate!")
        else:
            print("Empate total!")
            print("Empate total!")

"""
A função desempatar vai receber como parâmetro o tipo da classificação, assim como as mãoes dos jogadores. 
"""
def desempatar_maos(tipo, mao1, mao2):

    """Realiza a extração dos valores das mãos de cada jogador."""
    valores1 = sorted([retorna_valor_carta(c) for c in mao1], reverse=True)
    valores2 = sorted([retorna_valor_carta(c) for c in mao2], reverse=True)

    """Para comparar os valores das listas, utilizei um loop for e usei a função que permite comparar duas listas ao mesmo tempo. """
    def comparar_listas(v1, v2):
        for a, b in zip(v1, v2):
            if a > b:
                return 1
            elif b > a:
                return 2
        return 0  
    
    """
    Caso o tipo de classificação seja: Carta Alta, Flush, Sequência ou Straigth Flush. 
    Utilizamos a função comparar_listas para definir a carta de maior valor e assim definir o ganhador.
    """
    if tipo in ["Carta Alta", "Flush", "Sequência", "Straight Flush"]:
        return comparar_listas(valores1, valores2)

    # =======================================================================================
    
    elif tipo == "Um Par":
        """
        Um Par No caso de um empate: O par maior vence. Se dois jogadores tiverem o mesmo par, a maior carta fora do par define o vencedor, e se necessário a segunda maior carta e a terceira maior carta pode ser utilizadas para o desempate.
        """
        """ 
        Primeiro, identificamos o maior par de ambas as mãos.
        """
        cont1 = Counter(valores1)
        cont2 = Counter(valores2)
        par1 = max([v for v, count in cont1.items() if count == 2])
        par2 = max([v for v, count in cont2.items() if count == 2])
        
        """Comparamos os pares."""
        if par1 > par2:
            return 1
        elif par2 > par1:
            return 2

        "Caso os pares sejam iguais, usamos as outras cartas para definir o ganhador."
        kickers1 = sorted([v for v in valores1 if v != par1], reverse=True)
        kickers2 = sorted([v for v in valores2 if v != par2], reverse=True)
        return comparar_listas(kickers1, kickers2)

    # =======================================================================================

    elif tipo == "Dois Pares":
        """
        Dois Pares No caso de um empate: O par maior vence. Se os jogadores possuírem o mesmo par mais alto, o segundo par decide o vencedor. Se os dois jogadores tiverem pares idênticos, a quinta carta define o vencedor.
        """
        """
        Primeiro, identificamos pares maiores de cada mão, e os colocá-mos em ordem descrescente.
        """
        cont1 = Counter(valores1)
        cont2 = Counter(valores2)
        pares1 = sorted([v for v, c in cont1.items() if c == 2], reverse=True)
        pares2 = sorted([v for v, c in cont2.items() if c == 2], reverse=True)

        """ 
        Comparamos os pares para decidir o ganhador.
        """
        if pares1[0] != pares2[0]:
            return 1 if pares1[0] > pares2[0] else 2
        if pares1[1] != pares2[1]:
            return 1 if pares1[1] > pares2[1] else 2

        """Caso os pares dos jogadores sejam iguais, utilizamos as cartas kicker."""
        kicker1 = max([v for v in valores1 if v not in pares1])
        kicker2 = max([v for v in valores2 if v not in pares2])
        if kicker1 > kicker2:
            return 1
        elif kicker2 > kicker1:
            return 2
        return 0
    
    # =======================================================================================

    elif tipo == "Trinca":
        """Trinca No caso de um empate: A trinca de maior valor vence. Em jogos com cartas comunitárias onde os jogadores podem ter a mesma trinca, ganha o jogador com a maior carta além das três de mesmo valor, e se necessário a segunda maior carta será utilizada para desempate."""
        """ 
        Primeiro, identificamos a trinca de maior valor de cada jogador.
        """
        cont1 = Counter(valores1)
        cont2 = Counter(valores2)
        trinca1 = [v for v, c in cont1.items() if c == 3][0]
        trinca2 = [v for v, c in cont2.items() if c == 3][0]
        
        """Comparamos as trincas."""
        if trinca1 != trinca2:
            return 1 if trinca1 > trinca2 else 2

        """Caso as trincas tenham o mesmo valor, utilizamos as demais cartas."""
        kickers1 = sorted([v for v in valores1 if v != trinca1], reverse=True)
        kickers2 = sorted([v for v in valores2 if v != trinca2], reverse=True)
        return comparar_listas(kickers1, kickers2)

    # =======================================================================================

    elif tipo == "Full House":
        """Full House No caso de um empate: As maiores três cartas do mesmo valor vencem o pote. Em jogos com cartas comunitárias onde os jogadores podem conseguir as mesmas três cartas de valor igual, vence aquele com o par de maior valor."""
        """ 
        Primeiro, identificamos as três cartas de mesmo valor.
        """
        cont1 = Counter(valores1)
        cont2 = Counter(valores2)
        trio1 = [v for v, c in cont1.items() if c == 3][0]
        trio2 = [v for v, c in cont2.items() if c == 3][0]
         
        """Comparamos o valor das cartas."""
        if trio1 != trio2:
            return 1 if trio1 > trio2 else 2

        """Caso o trio seja igual para ambos os jogadores, procuramos pelo par de maior valor."""
        par1 = [v for v, c in cont1.items() if c == 2][0]
        par2 = [v for v, c in cont2.items() if c == 2][0]
        if par1 != par2:
            return 1 if par1 > par2 else 2

        return 0

    # =======================================================================================

    elif tipo == "Quadra":
        """Quadra No caso de um empate: A maior quadra vence. Em jogos com cartas comunitárias onde os jogadores podem conseguir a mesma quadra, a maior quinta carta (Kicker) vence."""
        
        """ 
        Primeiro, identificamos a maior quadra.
        """
        cont1 = Counter(valores1)
        cont2 = Counter(valores2)
        quadra1 = [v for v, c in cont1.items() if c == 4][0]
        quadra2 = [v for v, c in cont2.items() if c == 4][0]

        """Comparamos o valor da quadra."""
        if quadra1 != quadra2:
            return 1 if quadra1 > quadra2 else 2
        
        """No caso de ambos os jogadores possuírem quadras de mesmo valor. Utilizamos a carta restante para definir o ganhador."""
        kicker1 = [v for v in valores1 if v != quadra1][0]
        kicker2 = [v for v in valores2 if v != quadra2][0]
        if kicker1 > kicker2:
            return 1
        elif kicker2 > kicker1:
            return 2
        return 0

    # =======================================================================================

    elif tipo == "Royal Flush":
        """No caso de um Royal Flush, o empate realmente aconteceu."""
        return 0  

    return 0 

def main():
    baralho = criar_baralho()

    mao1 = baralho[:5]
    mao2 = baralho[5:10]

    print("\nResultado da Partida:")
    comparar_maos(mao1, mao2)



main()
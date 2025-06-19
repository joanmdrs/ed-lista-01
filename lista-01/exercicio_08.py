""" 
Para resolver o exercício 08, foi pensando uma estrutura envolvendo classes para organização dos métodos, e estruturas de listas para realizar o armazenamento. 
"""

"""
A classe Votacao define um construtor que inicializa duas listas, uma para armazenar os nomes dos votantes, e outra para armazenar os votos. 
"""
class Votacao:
    def __init__(self):
        self.votantes = []
        self.votos = []
    
    """
    O método registrar_voto executa um trecho de código, onde é solicitado o nome do votante. Uma vez inserido o nome do votante, o método verifica se o nome existe dentro da lista de votantes. Caso o nome informado já esteja dentro da lista de votantes, o método exibe um aviso informando que 'Você já votou!' e encerra a execução. 
    
    Caso o nome ainda não esteja na lista de votantes, o sistema pede a opção de VOTO. Caso a opção selecionada esteja entre as opções disponíveis, a mesma é armazenada na lista de votos. Em seguida, o nome do votante é adicionado a lista de votantes. 
    
    
    Caso o usuário selecione uma opção de voto que não está disponível, o sistema exibe uma mensagem de opção inválida e encerra a execução do método. 
    """
    def registrar_voto(self):
        
        nome = input("Informe seu nome: ")
        
        if nome in self.votantes:
            print("Você já votou!")
            return
        
        voto = input("Selecione sua opção de voto: (A, B ou C): ").strip().upper()
        
        if voto == 'A':
            self.votos.append("A")
        elif voto == 'B':
            self.votos.append("B")
        elif voto == 'C':
            self.votos.append("C")
        else:
            print("A opção selecionada é inválida!\n")
            return
        
        self.votantes.append(nome)
        print("Seu voto foi registrado com sucesso!\n")
    
    """
    O método exibir_resultado inicializa três variáveis, uma para cada opção de voto.

    Em seguida, é realizado um loop for que percorre a lista de votos e verifica 
    qual opção foi votada em cada iteração. Conforme o voto encontrado, o contador 
    correspondente é incrementado (A, B ou C).

    Após o término da contagem, os totais de votos de cada opção são exibidos na tela.

    Em seguida, o método verifica qual das opções recebeu o maior número de votos. 
    Se a opção A tiver mais votos que B e C, A é declarada vencedora. O mesmo vale 
    para B e C. Se nenhuma das opções tiver uma quantidade de votos estritamente 
    maior que as outras (ou seja, se houver empate entre duas ou mais), o resultado 
    é definido como "Empate".

    Por fim, o nome da opção vencedora (ou "Empate") é impresso na tela como o 
    resultado final da votação.
    """
    def exibir_resultado(self):
        total_votos_A = 0
        total_votos_B = 0
        total_votos_C = 0

        for voto in self.votos:
            if voto == "A":
                total_votos_A += 1
            elif voto == "B":
                total_votos_B += 1
            elif voto == "C":
                total_votos_C += 1

        print("\nRESULTADO DA VOTAÇÃO:")
        print(f"Total de votos A: {total_votos_A}")
        print(f"Total de votos B: {total_votos_B}")
        print(f"Total de votos C: {total_votos_C}")

        if total_votos_A > total_votos_B and total_votos_A > total_votos_C:
            vencedor = "A"
        elif total_votos_B > total_votos_A and total_votos_B > total_votos_C:
            vencedor = "B"
        elif total_votos_C > total_votos_A and total_votos_C > total_votos_B:
            vencedor = "C"
        else:
            vencedor = "Empate"

        print(f"VENCEDOR DA VOTAÇÃO: {vencedor}")

"""
A função main() por sua vez é responsável pela lógica de execução do programa, onde 
inicialmente ela instancia a classe Votacao. Em seguida, executa um loop while, que 
fica em execução contínua até que o usuário decida encerrar o processo de votação.

Dentro do laço, o programa solicita ao usuário que informe se deseja votar, digitando 
's' para sim ou 'n' para não. Se a resposta for 's', o método registrar_voto() da 
instância da classe Votacao é chamado, permitindo que o usuário registre seu voto.

Se a resposta for 'n', o loop é interrompido com a instrução break, encerrando a fase 
de votação. Caso o usuário digite qualquer outro valor, uma mensagem de "Opção inválida!" 
é exibida, e o programa volta a perguntar.

Após o encerramento da votação (quando o usuário digitar 'n'), o método exibir_resultado() 
é chamado para mostrar os totais de votos e o vencedor da votação.
"""
        
def main():
    
    votacao = Votacao()
    while True:
        opcao = input("Deseja votar? (s/n): ").strip().lower()
        if opcao == 's':
            votacao.registrar_voto()
        elif opcao == 'n':
            break
        else:
            print("Opção inválida!")

    votacao.exibir_resultado()
    
main()
                
    
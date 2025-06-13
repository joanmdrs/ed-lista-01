"""
Para implementar este exercício, foi pensada uma estrutura envolvendo classes, assim como estruturas envolvendo listas. Essa lógica foi elaborada buscando garantir maior organização, reutilização de código e facilidade na manipulação dos dados. 
"""

""" 
A classe Participante é responsável por representar cada participante do evento. Ela possui dois atributos: nome e idade. 
"""
class Participante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

""" 
A classe Evento gerencia o controle dos participantes inscritos e aplica critérios de seleção. No método construtor da classe é definido uma lista para armazenar os participantes aprovados, e outras duas variáveis, uma para armazenar a quantidade de participantes rejeitados por idade, e outra para armazenar a quantidade de rejeitados pelo nome. 
"""
class Evento:
    def __init__(self):
        self.aprovados = []
        self.rejeitados_por_idade = 0
        self.rejeitados_por_nome = 0

    """ 
    O método adicionar_participante recebe como parâmetro um participante e tem como finalidade verificar se aquele participante será aprovado ou não. Para isso, este método avalia se o participante atende aos dois critérios de aceitação: Idade entre 18 e 30 anos, Nome com mais de 5 caracteres. 
    r
    No caso de ambos os critérios forem atendidos, o participante é adicionado à lista de aprovados. Caso contrário, os contadores de rejeição são atualizados conforme o motivo da reprovação.
    """
    def adicionar_participante(self, participante):
        
        verifica_idade = participante.idade >= 18 and participante.idade <= 30
        verifica_nome = len(participante.nome) > 5

        if verifica_idade and verifica_nome:
            self.aprovados.append(participante)
        else:
            if not verifica_idade:
                self.rejeitados_por_idade += 1
            if not verifica_nome:
                self.rejeitados_por_nome += 1

    """ 
    O método exibir_relatorio tem como finalidade exibir a relação dos participantes que foram aprovados, assim como: a quantidade de participantes rejeitados por idade e a quantidade de participantes rejeitados por nome.
    Para exibir a relação de participantes aprovados, é executado um loop for para percorrer a lista de aprovados.
    """
    def exibir_relatorio(self):
        print("\nParticipantes Aprovados:")
        for a in self.aprovados:
            print(f"- {a.nome}")
        print("\nParticipantes Rejeitados:")
        print(f"Por idade: {self.rejeitados_por_idade}")
        print(f"Por nome: {self.rejeitados_por_nome}")

"""
A função main() é responsável por executar as seguintes ações:
1. Cria uma instância da classe Evento.
2. Pergunta ao usuário quantos participantes deseja cadastrar.
3 Executa um laço de repetição para: 
    - Solicitar o nome e a idade de cada participante;
    - Criar um objeto Participante;
    - Enviar esse objeto ao evento por meio do método adicionar_participante().

Por fim, é chamado o método exibir_relatorio() para mostrar os resultados da avaliação.
"""
def main():
    evento = Evento()
    quant = int(input("Quantos participantes deseja cadastrar? "))

    for i in range(quant):
        nome = input(f"\nNome do participante {i+1}: ")
        idade = int(input(f"Idade do participante {i+1}: "))
        participante = Participante(nome, idade)
        evento.adicionar_participante(participante)

    evento.exibir_relatorio()

main()

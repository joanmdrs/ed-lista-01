class Participante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Evento:
    def __init__(self):
        self.aprovados = []
        self.rejeitados_por_idade = 0
        self.rejeitados_por_nome = 0

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

    def exibir_relatorio(self):
        print("\nParticipantes Aprovados:")
        for a in self.aprovados:
            print(f"- {a.nome}")
        print("\nParticipantes Rejeitados:")
        print(f"Por idade: {self.rejeitados_por_idade}")
        print(f"Por nome: {self.rejeitados_por_nome}")

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

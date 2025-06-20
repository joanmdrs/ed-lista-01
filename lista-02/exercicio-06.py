class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.pilha.pop()
        print("Erro: pilha vazia")

    def top(self):
        if not self.isEmpty():
            return self.pilha[-1]

    def isEmpty(self):
        return len(self.pilha) == 0

    def size(self):
        return len(self.pilha)

    def __str__(self):
        return str(self.pilha)

    def __iter__(self):
        return iter(self.pilha)


class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.fila.pop(0)
        print("Erro: fila vazia")

    def isEmpty(self):
        return len(self.fila) == 0

    def size(self):
        return len(self.fila)

    def __str__(self):
        return str(self.fila)

    def __iter__(self):
        return iter(self.fila)


class Aluno:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

    def __str__(self):
        return f"{self.numero} - {self.nome}"


class Nota:
    def __init__(self, numero_aluno, pontuacao):
        self.numero_aluno = numero_aluno
        self.pontuacao = pontuacao


class SistemaAcademico:
    def __init__(self):
        self.alunos = Pilha()
        self.notas = Fila()
        self.proximo_numero_aluno = 1

    def menu(self):
        while True:
            print("\n====== MENU DE OPÇÕES ======")
            print("1 - Cadastrar aluno")
            print("2 - Cadastrar nota")
            print("3 - Calcular a média de um aluno")
            print("4 - Listar os nomes dos alunos sem notas")
            print("5 - Excluir aluno")
            print("7 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.cadastrar_aluno()
            elif opcao == '2':
                self.cadastrar_nota()
            elif opcao == '3':
                self.calcular_media()
            elif opcao == '4':
                self.listar_alunos_sem_nota()
            elif opcao == '5':
                self.excluir_aluno()
            elif opcao == '7':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        if not nome.strip():
            print("Nome inválido.")
            return
        aluno = Aluno(self.proximo_numero_aluno, nome)
        self.alunos.push(aluno)
        print(f"O aluno {nome} foi cadastrado com sucesso! \nNúmero do aluno: {self.proximo_numero_aluno}")
        self.proximo_numero_aluno += 1

    def cadastrar_nota(self):
        try:
            numero = int(input("Informe o número de cadastro do aluno: "))
            achou = False
            for aluno in self.alunos:
                if aluno.numero == numero:
                    achou = True
                    break

            if not achou:
                print("Aluno não encontrado.")
                return

            nota = float(input("Digite a nota (0 a 10): "))
            if 0 <= nota <= 10:
                self.notas.enqueue(Nota(numero, nota))
                print("Nota cadastrada com sucesso!")
            else:
                print("Nota inválida. A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números.")

    def calcular_media(self):
        try:
            numero = int(input("Digite o número do aluno: "))
            aluno_encontrado = None
            for aluno in self.alunos:
                if aluno.numero == numero:
                    aluno_encontrado = aluno
                    break

            if not aluno_encontrado:
                print("Aluno não encontrado!")
                return

            soma_notas = 0
            cont_notas = 0
            for nota in self.notas:
                if nota.numero_aluno == numero:
                    soma_notas += nota.pontuacao
                    cont_notas += 1

            if cont_notas == 0:
                print("Este aluno não possui notas cadastradas.")
                return

            media = soma_notas / cont_notas
            print(f"Aluno: {aluno_encontrado.nome}")
            print(f"Média: {media:.2f}")
        except ValueError:
            print("Entrada inválida.")

    def listar_alunos_sem_nota(self):
        alunos_com_nota = []

        for nota in self.notas:
            alunos_com_nota.append(nota.numero_aluno)

        sem_nota = []
        for aluno in self.alunos:
            if aluno.numero not in alunos_com_nota:
                sem_nota.append(aluno.nome)

        if len(sem_nota) == 0:
            print("Todos os alunos possuem notas.")
        else:
            print("Alunos sem notas:")
            for nome in sem_nota:
                print(f"- {nome}")


    def excluir_aluno(self):
        if self.alunos.isEmpty():
            print("Não há alunos para excluir.")
            return

        aluno = self.alunos.top()
        tem_nota = any(n.numero_aluno == aluno.numero for n in self.notas)

        if tem_nota:
            print(f"Não é possível excluir {aluno.nome} (número {aluno.numero}), pois ele possui notas.")
        else:
            removido = self.alunos.pop()
            print(f"Aluno {removido.nome} excluído com sucesso.")


def main():
    sistema = SistemaAcademico()
    sistema.menu()

main()
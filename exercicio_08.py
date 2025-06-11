       
class Votacao:
    def __init__(self):
        self.votantes = []
        self.votos = []
        
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
                
    
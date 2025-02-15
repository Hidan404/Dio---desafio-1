'''
Sistema Bancário - 1.0
Com três métodos de operação:
1. Depositar
2. Sacar
3. Extrato
'''

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []
        self.saques_realizados = 0 

    def depositar(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                self.extrato.append(f'Depósito: R$ {valor:.2f}')
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            else:
                print("O valor do depósito precisa ser positivo.")
        except ValueError:
            print('Erro: Valor inválido para depósito.')

    def sacar(self, valor):
        try:
            LIMITE_SAQUES = 3
            SAQUE_MAXIMO = 500

            valor = float(valor)

            if self.saques_realizados >= LIMITE_SAQUES:
                print("Erro: Limite diário de saques atingido.")
                return
            
            if valor > self.saldo:
                print(f"Erro: Saldo insuficiente Saldo atual de: R$ {self.saldo:.2f}")
                return

            if valor > SAQUE_MAXIMO:
                print(f"Erro: O valor máximo para saque é de R$ {SAQUE_MAXIMO:.2f} por operação.")
                return

            if valor > 0:
                self.saldo -= valor
                self.extrato.append(f'Saque: R$ {valor:.2f}')
                self.saques_realizados += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print("Erro: O valor do saque deve ser maior que zero.")

        except ValueError:
            print('Erro: Valor inválido para saque.')

    def mostrar_extrato(self):
        print(f"\nExtrato da conta de {self.titular}")  
        print(f"Saldo atual: R$ {self.saldo:.2f}")   
        if self.extrato:
            for operacao in self.extrato:
                print(operacao)
        else:
            print("Nenhuma operação realizada ainda.")

# Interface do usuário
def buscar_conta(titular, contas):
    """ Busca uma conta pelo nome do titular. """
    for conta in contas:
        if conta.titular == titular:
            return conta
    return None

def ui():
    contas = []

    while True:
        try:
            print("\n=== MENU ===")
            print("1. Criar conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Extrato")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titular = input("Digite o nome do titular: ").strip()
                saldo = float(input("Digite o saldo inicial: "))
                nova_conta = Conta(titular, saldo)
                contas.append(nova_conta)
                print(f"Conta criada para {titular}!")

            elif opcao == "2":
                titular = input("Digite o nome do titular: ").strip()
                conta = buscar_conta(titular, contas)
                if conta:
                    valor = input("Digite o valor do depósito: ")
                    conta.depositar(valor)
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "3":
                titular = input("Digite o nome do titular: ").strip()
                conta = buscar_conta(titular, contas)
                if conta:
                    valor = input("Digite o valor do saque: ")
                    conta.sacar(valor)
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "4":
                titular = input("Digite o nome do titular: ").strip()
                conta = buscar_conta(titular, contas)
                if conta:
                    conta.mostrar_extrato()
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "5":
                print("Saindo do sistema...")      
                break  

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    ui()

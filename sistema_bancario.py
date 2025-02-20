from datetime import datetime, time, timedelta, date
import re


'''
Sistema Bancário - 1.0
Com três métodos de operação:
1. Depositar
2. Sacar
3. Extrato

'''

#todo: estabelecer limite de transacoes diários 10
#todo: se o usuario tentar fazer mais de 10 transações diarias, exibir mensagem que limite diario foi atingido
#todo: mostrar no extrato data e hora de todas transaçoes
#todo: armazenar usuarios com nome, data de nascimento, cpf, endereco no formato logradouro, numero, bairro, cidade, estado, cep
#todo: não podemos ter mais de uma conta com o mesmo cpf

class Usuario():
    def __init__(self,titular, data_nascimento, cpf, endereco):
        self.titular = titular
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco



class Conta:
    def __init__(self, usuario, saldo=0):
        self.usuario = usuario
        self.saldo = saldo
        self.extrato = []
        self.saques_realizados = 0 
        self.transacoes = 0
        self.transacoes_limite = 10
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def atualizar_transacoes(self):
        if (self.transacoes) >= self.transacoes_limite:
            print(f"Erro: Limite diário de transações atingido para sua conta {self.usuario.nome}.")
            return False

    def atualizar_data(self):
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def depositar(self, valor):
        if not self.atualizar_transacoes():
            return False

        try:
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                self.atualizar_data()
              
                self.transacoes+= 1
                self.extrato.append(f'Depósito: R$ {valor:.2f}, Data: {self.data}')
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            else:
                print("O valor do depósito precisa ser positivo.")
        except ValueError:
            print('Erro: Valor inválido para depósito.')

    def sacar(self, valor):

        if not self.atualizar_transacoes():
            return False
        
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
            
            if valor < 0:
                print("Erro: O valor do saque deve ser positivo.")
                return

            if valor > SAQUE_MAXIMO:
                print(f"Erro: O valor máximo para saque é de R$ {SAQUE_MAXIMO:.2f} por operação.")
                return

            if valor > 0:
                self.saldo -= valor
                self.atualizar_data()
                self.transacoes+= 1
                self.extrato.append(f'Saque: R$ {valor:.2f}, Data: {self.data}')
                self.saques_realizados += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print("Erro: O valor do saque deve ser maior que zero.")

        except ValueError:
            print('Erro: Valor inválido para saque.')

    def mostrar_extrato(self):
        print(f"\nExtrato da conta de {self.usuario.titular}:")  
        print(f"Saldo atual: R$ {self.saldo:.2f}")   
        if self.transacoes:
            for transacao in self.transacoes:
                print(transacao)
        else:
            print("Nenhuma operação realizada ainda.")

    def listar_contas(contas):
        """ Lista todas as contas cadastradas. """
        for conta in contas:
            print(f"Titular: {conta.usuario.titular}, Saldo: R$ {conta.saldo:.2f} CPF: {conta.usuario.cpf}")



    def buscar_conta(cpf, contas):
        """ Busca uma conta pelo nome do cpf. """
        for conta in contas:
            if conta.usuario.cpf == cpf:
                return conta
        return None

    def validar_data_nascimento(data_nascimento):
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return True
        except Exception as e:
            return False

    def validar_cpf(cpf):
        try:
            regex_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
            if regex_cpf.match(cpf):
                return True  
        except:
            return False       

transacoes_diarias = 0
ultima_transacao = datetime.today().date()

def ui():
    contas = []
    global transacoes_diarias, ultima_transacao
    
    while True:
        try:
            
            if datetime.today().date() != ultima_transacao:
                ultima_transacao = datetime.today().date()
                transacoes_diarias = 0
                print("Limite diário de transações resetado.")

            if transacoes_diarias >= 10:
                print("Erro: Limite diário de transações atingido.")    
                print("Deseja sair do sistema ou continuar?")
                opcao = input("Digite 1 para sair ou 2 para continuar: ")
                if opcao == "1":
                    print("Saindo do sistema...")
                    break
                continue

            print("\n=== MENU ===")
            print("1. Criar conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Extrato")
            print("5. Listar contas Cadastradas")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                if transacoes_diarias >= 10:
                    print("Erro: Limite diário de transações atingido.")
                else:    
                    titular = input("Digite o nome do titular: ").strip()
                    saldo = float(input("Digite o saldo inicial: "))
                    data_nascimento = input("Digite a data de nascimento formato 00/00/0000: ")
                    cpf = input("Digite o CPF no formato 000.000.000-00: ").strip()

                    if any(conta.usuario.cpf == cpf for conta in contas):
                        print("Erro: Já existe uma conta com esse CPF.")
                        continue

                    if not Conta.validar_data_nascimento(data_nascimento) or not Conta.validar_cpf(cpf):
                        print("Erro: Data de nascimento ou CPF inválidos.")
                        continue
                        
                    endereco = input("Digite o endereço nesse formato: 'logradouro, numero, bairro, cidade, estado, cep': ") .split(',')   


                    usuarios = Usuario(titular, data_nascimento, cpf, endereco)
                    conta = Conta(usuarios, saldo)
                    contas.append(conta)
                    
                    print(f"Conta criada para {titular}!")
                    transacoes_diarias += 1

            elif opcao == "2":
                if transacoes_diarias >= 10:
                    print("Erro: Limite diário de transações atingido.")

                cpf = input("Digite seu cpf do titular: ").strip()
                conta = Conta.buscar_conta(cpf, contas)
                
                if conta:
                    valor = input("Digite o valor do depósito: ")
                    conta.depositar(valor)
                    transacoes_diarias += 1
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "3":
                cpf = input("Digite seu cpf do titular: ").strip()
                conta = Conta.buscar_conta(cpf, contas)
                if conta:
                    valor = input("Digite o valor do saque: ")
                    conta.sacar(valor)
                    transacoes_diarias += 1
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "4":
                cpf = input("Digite o numero do cpf da conta: ").strip()
                conta = Conta.buscar_conta(cpf, contas)
                if conta:
                    conta.mostrar_extrato()
                    transacoes_diarias += 1
                else:
                    print("Erro: Conta não encontrada.")

            elif opcao == "5":
                print("Listando contas")
                conta.listar_contas(contas)
            elif opcao == "6":
                print("Saindo do sistema...")      
                break  

            print(f"Transações diárias: {transacoes_diarias}")      

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    ui()

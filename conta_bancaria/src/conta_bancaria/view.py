from datetime import datetime
from model.conta import Conta
from model.usuario import Usuario
from model.arquivo import salvar_usuario_em_arquivo

def ui():
    contas = []
    transacoes_diarias = 0
    ultima_transacao = datetime.today().date()

    while True:
        if datetime.today().date() != ultima_transacao:
            ultima_transacao = datetime.today().date()
            transacoes_diarias = 0
            print("Transações resetadas.")

        print("\n=== MENU ===")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Extrato")
        print("5. Listar contas")
        print("6. Salvar usuário")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            saldo = float(input("Saldo inicial: "))
            data = input("Data nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (xxx.xxx.xxx-xx): ")
            if any(c.usuario.cpf == cpf for c in contas):
                print("CPF já cadastrado.")
                continue
            if not Conta.validar_cpf(cpf) or not Conta.validar_data_nascimento(data):
                print("CPF/Data inválidos.")
                continue
            endereco = input("Endereço (logradouro, numero, bairro, cidade, estado, cep): ").split(',')
            usuario = Usuario(nome, data, cpf, endereco)
            conta = Conta(usuario, saldo)
            contas.append(conta)
            transacoes_diarias += 1
            print("Conta criada com sucesso!")

        elif opcao == "2":
            cpf = input("CPF: ")
            conta = Conta.buscar_conta(cpf, contas)
            if conta:
                valor = input("Valor depósito: ")
                conta.depositar(valor)
                transacoes_diarias += 1
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            cpf = input("CPF: ")
            conta = Conta.buscar_conta(cpf, contas)
            if conta:
                valor = input("Valor saque: ")
                conta.sacar(valor)
                transacoes_diarias += 1
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            cpf = input("CPF: ")
            conta = Conta.buscar_conta(cpf, contas)
            if conta:
                conta.mostrar_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            Conta.listar_contas(contas)

        elif opcao == "6":
            cpf = input("CPF: ")
            conta = Conta.buscar_conta(cpf, contas)
            if conta:
                salvar_usuario_em_arquivo(conta.usuario)
            else:
                print("Conta não encontrada.")

        elif opcao == "7":
            print("Saindo...")
            break

from datetime import datetime

class Conta:
    def __init__(self, usuario, saldo=0, agencia="0001"):
        self.usuario = usuario
        self.saldo = saldo
        self.agencia = agencia
        self.extrato = []
        self.saques_realizados = 0
        self.transacoes = 0
        self.transacoes_limite = 10
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def atualizar_transacoes(self):
        return self.transacoes < self.transacoes_limite

    def atualizar_data(self):
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def depositar(self, valor):
        if not self.atualizar_transacoes():
            print("Erro: Limite de transações atingido.")
            return
        valor = float(valor)
        if valor > 0:
            self.saldo += valor
            self.transacoes += 1
            self.atualizar_data()
            self.extrato.append(f'Depósito: R$ {valor:.2f} em {self.data}')
            print(f'Depósito de R$ {valor:.2f} realizado.')
        else:
            print("Erro: Valor inválido.")

    def sacar(self, valor):
        if not self.atualizar_transacoes():
            print("Erro: Limite de transações atingido.")
            return
        valor = float(valor)
        if valor <= 0 or valor > 500 or valor > self.saldo:
            print("Erro: Valor inválido ou saldo insuficiente.")
            return
        if self.saques_realizados >= 3:
            print("Erro: Limite diário de saques atingido.")
            return
        self.saldo -= valor
        self.saques_realizados += 1
        self.transacoes += 1
        self.atualizar_data()
        self.extrato.append(f'Saque: R$ {valor:.2f} em {self.data}')
        print(f'Saque de R$ {valor:.2f} realizado.')

    def mostrar_extrato(self):
        if not self.extrato:
            print("Extrato vazio.")
            return
        print(f"\nExtrato de {self.usuario.titular} - Saldo: R$ {self.saldo:.2f}")
        for linha in self.extrato:
            print(linha)

    @staticmethod
    def listar_contas(contas):
        if not contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in contas:
            print(f"Titular: {conta.usuario.titular}, Saldo: R$ {conta.saldo:.2f}, CPF: {conta.usuario.cpf} Data visualização: {conta.data}")

    @staticmethod
    def buscar_conta(cpf, contas):
        for conta in contas:
            if conta.usuario.cpf == cpf:
                return conta
        return None

    @staticmethod
    def validar_cpf(cpf):
        import re
        return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf) is not None

    @staticmethod
    def validar_data_nascimento(data):
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except:
            return False

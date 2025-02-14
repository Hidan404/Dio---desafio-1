'''
Sistema Bancario - 1.0
com somente 3 metodos de operação:
1. Depositar
2. Sacar
3. Extrato
'''

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        try:
            valor = float(valor)

            if valor > 0:
                self.saldo += valor
                self.extrato.append(f'Depósito: R$ {valor:.2f}')
        except ValueError:
            print('Valor inválido')    
         
    def sacar(self, valor):
        try:
            limite_saques = 3
            saque_diarios = 500
            valor = float(valor)
            total_vezes_de_saque = 0

            if valor > 0 and valor <= self.saldo:
                if total_vezes_de_saque < limite_saques:
                    if valor <= saque_diarios:
                        self.saldo -= valor
                        self.extrato.append(f'Saque: R$ {valor:.2f}')
                        total_vezes_de_saque += 1
                    else:
                        print(f'saldo insuficiente , saldo atual: R$ {self.saldo:.2f}')
                        
        except ValueError:
            print('Valor inválido')    

    def extrato(self):
        print(f"extrato da conta de {self.titular}")  
        print(f"Saldo de R$ {self.saldo:.2f}")   

        for operacao in self.extrato:
            print(operacao)      
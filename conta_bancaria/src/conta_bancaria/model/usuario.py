class Usuario:
    def __init__(self, titular, data_nascimento, cpf, endereco):
        self.titular = titular
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
    def __str__(self):
        return f"Usuário: {self.titular}, Data Nascimento: {self.data_nascimento}, CPF: {self.cpf}, Endereço: {self.endereco}"
# Sistema Bancário 1.0

Esse é um projeto simples de um Sistema Bancário desenvolvido em Python como primeiro desafio do bootcamp Suzano Python Developer. Adicionei mais funcionalidades do que o proposto no exercício, quis me testar até onde posso melhorar, mas por enquanto, o objetivo principal foi praticar conceitos de POO (Programação Orientada a Objetos) e manipulação de entrada de dados.

## 🛠 Funcionalidades

- **Criar conta bancária:** Permite ao usuário criar uma nova conta, fornecendo informações como nome do titular, saldo inicial, CPF, e endereço.
- **Realizar depósitos:** Permite ao titular depositar um valor em sua conta.
- **Realizar saques com limite diário:** Permite ao titular realizar saques, respeitando um limite de transações diárias.
- **Consultar extrato bancário:** O titular pode consultar o extrato, com todos os depósitos e saques realizados, incluindo data e hora.
- **Limite de 10 transações diárias por titular:** Cada titular pode realizar até 10 transações por dia. Após atingir esse limite, não é possível realizar mais transações até o próximo dia.
- **Bloqueio de transações quando o limite diário for atingido:** O sistema bloqueia novas transações quando o limite diário de transações for atingido.
- **Data e hora registradas no extrato de todas as transações:** Cada transação é registrada com a data e a hora em que foi realizada.
- **Método `atualizar_transacoes`:** Atualiza a quantidade de transações realizadas no dia.
- **Método `atualizar_data`:** Atualiza a data para o dia atual, resetando as transações diárias se o dia for diferente.
- **Método `listar_contas`:** Exibe todas as contas cadastradas no sistema.
- **Método `buscar_conta`:** Busca uma conta pelo CPF do titular e retorna a conta correspondente.
- **Método `validar_data_nascimento`:** Valida a data de nascimento do titular de acordo com um formato padrão.
- **Método `validar_cpf`:** Valida o CPF do titular para garantir que o formato e os dados sejam válidos.

## 🚀 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Hidan404/Dio---desafio-1.git
Acesse a pasta do projeto:
bash
Copiar
Editar
cd Dio---desafio-1
Execute o script principal:
bash
Copiar
Editar
python sistema_bancario.py
📝 Como funciona?
O sistema é baseado na classe Conta, que representa uma conta bancária com os seguintes métodos:

depositar(valor): Adiciona saldo à conta.
sacar(valor): Realiza saques respeitando o limite diário de transações.
mostrar_extrato(): Exibe o saldo e o histórico de operações da conta, com data e hora de cada transação.
atualizar_transacoes(): Atualiza a quantidade de transações feitas no dia.
atualizar_data(): Reseta o contador de transações diárias no início de cada dia.
listar_contas(): Lista todas as contas cadastradas no sistema.
buscar_conta(cpf): Busca uma conta específica pelo CPF do titular.
validar_data_nascimento(data): Valida se a data de nascimento fornecida está no formato correto.
validar_cpf(cpf): Valida se o CPF fornecido é válido de acordo com as regras de formatação.
A interface do usuário (função ui()) apresenta um menu interativo no terminal, permitindo ao usuário interagir com o sistema.

⚙ Requisitos
Python 3.x instalado.
🔗 Melhorias futuras
Implementar persistência de dados (salvar contas em um arquivo JSON ou banco de dados).
Criar uma interface gráfica.
Adicionar autenticação de usuário.
Se quiser contribuir, fique à vontade! 😃

📌 Autor: Ronald (Hidan404)

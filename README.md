# Sistema Bancário 1.0

Esse é um projeto simples de um Sistema Bancário desenvolvido em Python como primeiro desafio do bootcamp Suzano Python Developer. Adicionei mais funcionalidades do que o proposto no exercício, quis me testar até onde posso melhorar, mas por enquanto, o objetivo principal foi praticar conceitos de POO (Programação Orientada a Objetos) e manipulação de entrada de dados.

🛠 **Funcionalidades**

- Criar conta bancária
- Realizar depósitos
- Realizar saques com limite diário
- Consultar extrato bancário
- **Limite de 10 transações diárias por titular**
- **Bloqueio de transações quando o limite diário for atingido**
- **Data e hora registradas no extrato de todas as transações**

🚀 **Como executar o projeto**

Clone o repositório:

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

O sistema é baseado na classe Conta, que representa uma conta bancária com os métodos:

depositar(valor): Adiciona saldo à conta.
sacar(valor): Realiza saques respeitando um limite diário.
mostrar_extrato(): Exibe o saldo e o histórico de operações da conta, com data e hora de cada transação.
A interface do usuário (ui()) apresenta um menu interativo no terminal, permitindo ao usuário interagir com o sistema.

⚙ Requisitos

Python 3.x instalado
🔗 Melhorias futuras

Implementar persistência de dados (salvar contas em um arquivo JSON ou banco de dados)
Criar uma interface gráfica
Adicionar autenticação de usuário
Se quiser contribuir, fique à vontade! 😃

📌 Autor: Ronald (Hidan404)

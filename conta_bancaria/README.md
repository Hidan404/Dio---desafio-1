# 💳 Sistema de Conta Bancária em Python

Este é um projeto simples de simulação de contas bancárias desenvolvido em **Python**, utilizando o **Poetry** para gerenciamento de dependências e estruturação profissional com módulos separados. O objetivo foi praticar conceitos de **POO (Programação Orientada a Objetos)**, modularização, manipulação de arquivos e interação com o usuário via terminal.

---

## 🚀 Funcionalidades

- Criar conta bancária com validação de CPF e data de nascimento
- Realizar **depósitos** e **saques** com limites diários
- Gerar e visualizar **extrato de transações**
- Listar todas as contas cadastradas
- Salvar dados do usuário em um arquivo `.txt`
- Interface interativa no terminal com menu principal

---

## 🧱 Estrutura do Projeto

Organizei o projeto em módulos, separando as responsabilidades em arquivos distintos:

```
conta_bancaria/
├── main.py                     # Ponto de entrada da aplicação
├── view.py                     # Interface com o usuário (menus, inputs)
└── model/
    ├── conta.py                # Classe Conta: saques, depósitos, extrato etc.
    ├── usuario.py              # Classe Usuario: titular, cpf, endereço
    └── arquivo.py              # Função de salvar usuários em arquivo
```

> Toda a estrutura está dentro da pasta `src/`, conforme boas práticas com o Poetry.

---

## ⚙️ Como executar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SeuUsuario/seu-repo.git
   cd seu-repo
   ```

2. **Instale o Poetry** (caso ainda não tenha)
   ```bash
   pip install poetry
   ```

3. **Instale as dependências**
   ```bash
   poetry install
   ```

4. **Execute a aplicação**
   ```bash
   poetry run python -m conta_bancaria.main
   ```

---

## 📁 Arquivo de usuários

As contas salvas pelo sistema são registradas em um arquivo `.txt` localizado em:

- Linux: `/home/hidan/Documentos/GitHub/Dio---desafio-1/usuarios.txt`
- Windows: `C:\Users\hidan\Documents\GitHub\Dio---desafio-1\usuarios.txt`

> Esse caminho pode ser personalizado conforme o sistema operacional.

---

## 🧠 Tecnologias e conceitos aplicados

- Python 3
- Programação Orientada a Objetos
- Modularização de código
- Manipulação de arquivos (`.txt`)
- Validação de dados (CPF, datas)
- Menu interativo no terminal
- Gerenciamento de projeto com [Poetry](https://python-poetry.org)

---

## ✍️ Autor

Desenvolvido por **Ronald Sousa** – estudante e entusiasta de tecnologia em transição de carreira para a área de desenvolvimento.

---

## 📌 Observações

Este projeto faz parte dos meus estudos e práticas pessoais, com foco em reforçar a base de desenvolvimento em Python e boas práticas de organização de código.

---

## 🛠️ Melhorias futuras

- Adicionar persistência com banco de dados (SQLite ou MySQL)
- Criar uma interface gráfica (Tkinter ou Web)
- Implementar autenticação por senha
- Criar testes automatizados com `pytest`

---

📫 Ficou com dúvidas ou quer dar sugestões? Fique à vontade para abrir uma _issue_ ou me chamar no LinkedIn!
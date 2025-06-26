import os

def salvar_usuario_em_arquivo(usuario):
    if os.name == 'posix':
        caminho = "/home/hidan/Documentos/GitHub/Dio---desafio-1/usuarios.txt"
    elif os.name == 'nt':
        caminho = "C:\\Users\\hidan\\Documents\\GitHub\\Dio---desafio-1\\usuarios.txt"
    else:
        print("Sistema não suportado.")
        return

    with open(caminho, "a", encoding="utf-8") as f:
        f.write(f"{usuario.titular}, {usuario.data_nascimento}, {usuario.cpf}, {usuario.endereco}\n")
        print(f"Usuário {usuario.titular} salvo com sucesso.")

# Verificação de Força de Senha

Este é um programa simples em Python para verificar a força de uma senha com base em critérios predefinidos de segurança. Ele analisa a senha fornecida pelo usuário e fornece feedback sobre sua força com base nos seguintes requisitos:

- A senha deve ter no mínimo 8 caracteres.
- A senha deve conter pelo menos uma letra maiúscula (A-Z).
- A senha deve conter pelo menos uma letra minúscula (a-z).
- A senha deve conter pelo menos um número (0-9).
- A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

## Funcionalidades

- Verifica se a senha atende aos critérios de segurança.
- Fornece feedback sobre a força da senha.

## Como Usar

1. Clone o repositório para o seu ambiente local:
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
2. Navegue até o diretório do projeto:
   cd nome_do_repositorio
3. Execute o script Python e siga as instruções para inserir a senha:
   python verificar_forca_senha.py

Exemplo de Uso

from verificar_forca_senha import verificar_forca_senha

# Obtendo a senha do usuário
senha = input("Digite sua senha: ").strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
   
Contribuição
Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para abrir uma issue para discutir suas ideias ou enviar um pull request com suas alterações.

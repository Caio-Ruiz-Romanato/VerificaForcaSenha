import re

def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha é muito curta. Recomenda-se no mínimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letras maiúsculas e minúsculas, números e caracteres especiais
    for caractere in senha:
        if caractere.isupper():
            tem_letra_maiuscula = True
        elif caractere.islower():
            tem_letra_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif re.match(r'[!@#$%^&*(),.?":{}|<>]', caractere):
            tem_caractere_especial = True

    if not tem_letra_maiuscula or not tem_letra_minuscula or not tem_numero or not tem_caractere_especial:
        return "Sua senha não atende a todos os critérios de segurança."

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contém uma sequência comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha é muito comum. Tente uma senha mais complexa."

    # Se a senha atender a todos os critérios, retorna uma mensagem de sucesso
    return "Sua senha atende aos requisitos de segurança. Parabéns!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)

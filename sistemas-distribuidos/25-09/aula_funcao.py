def dados_pessoais(nome, sobrenome, idade, sexo):
    print(f"Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nSexo: {sexo}")

def mensagem(nome="Simao Caolho"):
    print(f"Ola, {nome}.")

def funcao_aula(a, b, c):
    """
    Funcao Aula
    """
    print(a, b, c)

### ===== ÁREA DE TESTES ===== ###

# Invocacao de forma posicional
dados_pessoais("Vitor", "Antoni", 19, "masculino")

# Invocacao de forma nomeada / chave-valor
dados_pessoais(sobrenome="Antoni", nome="Vitor", sexo="masculino", idade=19)

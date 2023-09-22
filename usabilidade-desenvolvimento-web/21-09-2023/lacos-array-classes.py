def codigo_seis():
    """
    ========= Classes =========
    - Modelos / moldes
    - Objetos serão instâncias
    ===========================
    """
    
    nome = "Carlos"
    print(nome.upper())
    print(isinstance(nome, str))

def codigo_cinco():
    listaNumeros = []
    while True:
        numeros = int(input("Digite um numero [0 para sair]: "))
        if numeros == 0:
            break
        
        listaNumeros.append(numeros)
    
    cont = 0
    while cont < len(listaNumeros):       # len() para determinar a quantidade de index na lista 'L'
        print(f"Contador: {cont} - Numero: {listaNumeros[cont]}")
        cont += 1

def codigo_quarto():
    notas = [6, 7, 5, 8, 9]
    soma = 0
    x = 0

    while x < 5:
        soma += notas[x]
        x += 1
    
    print(f"Média: {soma / 5:5.2f}")
    
def codigo_tres():
    x = 1
    soma = 0
    
    while x <= 5:
        n = int(input("Digite um numero: "))
        soma += n
        x += 1
    
    print(f"Soma: {soma / 5:5.2f}")

def codigo_dois():
    pontos = 0
    questao = 1
    while questao <= 3:
        resposta = str(input(f"Resposta da questao {questao}: "))

        if questao == 1 and resposta == "b":
            pontos += 1

        elif questao == 2 and resposta == "a":
            pontos += 1

        elif questao == 3 and resposta == "d":
            pontos += 1
    
        questao += 1

    print(f"O aluno fez {pontos} pontos")

def codigo_um():
    inicio = 0
    fim = int(input("Digite um numero: "))

    while inicio <= fim:
        print(inicio)
        inicio += 1


# AREA DE TESTES
codigo_um()
codigo_dois()
codigo_tres()
codigo_quarto()
codigo_cinco()
codigo_seis()

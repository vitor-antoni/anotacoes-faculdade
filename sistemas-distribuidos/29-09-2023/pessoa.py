# Classe pessoa
class pessoa():
    def __init__(self, nome, sobrenome, idade, eh_casada):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.eh_casada = eh_casada
    
    def casou(self):
        if self.eh_casada == False:
            self.eh_casada = True
        else:
            print("Pessoa já é casada!")

class Veiculo():
    def __init__(self, nome, ano, marca, combustivel, esta_ligado):
        self.nome = nome
        self.ano = ano
        self.marca = marca
        self.combustivel = combustivel
        self.esta_ligado = esta_ligado
    
    def __del__(self):
        print("Objeto veiculo deletado!")

    def ligar(self):
        if not self.esta_ligado:
            self.esta_ligado = True
            print("Ligando carro...")

        else:
            print("Veículo já está ligado!")
    
    def desligar(self):
        if self.esta_ligado:
            self.esta_ligado = False
            print("Desligando carro...")

        else:
            print("Veículo já está desligado!")
        
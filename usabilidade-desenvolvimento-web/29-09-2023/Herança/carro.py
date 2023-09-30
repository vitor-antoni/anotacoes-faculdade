from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, ano, marca, combustivel, esta_ligado,qtd_portas):
        super().__init__(nome, ano, marca,combustivel,esta_ligado)
        self.qtd_portas = qtd_portas

from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome, ano, marca, combustivel, esta_ligado, passageiros):
        super().__init__(nome, ano, marca, combustivel, esta_ligado)
        self.passageiros = passageiros
from carro import Carro

carro = Carro("Gol",2002,"Volkswagen","Gasolina",False,4)

print(f"Estado atual do carro: {carro.esta_ligado}")

carro.ligar()
print(f"Estado atual do carro: {carro.esta_ligado}")

carro.desligar()
print(f"Estado atual do carro: {carro.esta_ligado}")

### Para exibir todos os atributos da variável carro
print(carro.__dict__)
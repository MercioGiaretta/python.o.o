class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')

carros = []

while True:
    marca = input("Insira a marca do carro ou 0 para sair: ")

    if marca == "0":
        break
    
    modelo = input("Digite o Modelo: ")
    cor = input("Digite a Cor: ")
    ano = input("Digite qual o Ano: ")

    carro = Carro(marca, modelo, cor, ano)
    carro.append(carro)

print("\n Informações dos Carros: ")
for i, carro in enumerate(carros, start=1):
    print(f"\n Carro {i}")
    carro.exibir_informacoes()

input()

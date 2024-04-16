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

carro1 = Carro('Fiat', 'Uno', 'Prata', 2010)
carro2 = Carro('Ford', 'Ka', 'Preto', 2015)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()
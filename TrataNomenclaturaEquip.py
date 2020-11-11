from unicodedata import normalize

class TrataLista:
    def __init__(self):
        pass

    def removeAcentos(self, equipamento):
        return normalize('NFKD', equipamento).encode('ASCII', 'ignore').decode('ASCII')

    def caixaBaixa(self, equipamento):
        return self.removeAcentos(equipamento).lower()

    def separaPalavras(self, equipamento):
        return self.caixaBaixa(equipamento).split(' ')

    def compara(self, equipamento, filtro):
        resultado = []
        for i in self.separaPalavras(equipamento):
            for j in self.caixaBaixa(filtro):
                if i == j:
                    resultado.append(j)
        return resultado


"""
#Método para ser aplicado no arquivo principal
for i in listaEquipamentos: #A partir da lista contendo todos os equipamentos do site escolhido
    for j in equipamento[i]: #Executa métodos em cada equipamento
        TrataLista().compara(equipamento[i], GrauDeRisco().defineGrau())
"""

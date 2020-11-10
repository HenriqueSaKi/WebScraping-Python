from unicodedata import normalize

class TrataLista:
    def __init__(self):
        pass

    def removeAcentos(self, equipamento):
        equipamento = normalize('NFKD', equipamento).encode('ASCII', 'ignore').decode('ASCII')
        return equipamento

    def caixaBaixa(self, equipamento):
        self.removeAcentos(equipamento)
        return equipamento.lower()

#Função de split da nomenclatura do equipamento
#Função de extração de informação importante (Isolamento, CAG, TI, Centro Cirúrgico/CC, Arsenal, etc...)
#Função run retornando a lista com os valores filtrados

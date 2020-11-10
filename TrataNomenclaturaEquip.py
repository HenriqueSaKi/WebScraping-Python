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

    def compara(self, equipamento):
        for i in self.separaPalavras(equipamento):
            if i == self.caixaBaixa('climatizacao'):
                return "Deu certo!"
            else:
                return "Não deu certo."

retorna = TrataLista().compara('Climatização - Módulo 1')
print(retorna)
#Função de extração de informação importante (Isolamento, CAG, TI, Centro Cirúrgico/CC, Arsenal, etc...)
#Função run retornando a lista com os valores filtrados

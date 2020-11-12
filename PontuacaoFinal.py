from TrataNomenclaturaEquip import TrataLista

class Pontuacao:
    def __init__(self):
        self.filtros = {'comum': 25, 'arsenal': 34, 'cag': 39, 'geladeira': 33, 'cdi': 38, 'sdai': 38,
                        'cirurgica': 43, 'cirurgico': 43, 'cc': 43, 'cme': 37, 'cpd': 30, 'ti': 30, 'cti': 41,
                        'uti': 41, 'eletrica': 45, 'substacao': 45, 'gases': 36, 'gerador': 47, 'hidraulica': 32,
                        'incendio': 49, 'internacao': 27, 'isolamento': 40, 'no break': 48, 'cabine primaria': 46,
                        'farmacia': 31, 'tmo': 42, 'medicina nuclear': 35, 'sala de exames': 28, 'laboratorio': 26,
                        'aquecedores': 29, 'aquecedor': 29}
        self.filtro = ''

    def incremento(self, equipamento):
        equipamento = equipamento.split('-')
        for i in equipamento:
            for j in self.filtros:
                if j in i:
                    self.filtro = j
        return self.filtros[self.filtro]

print(Pontuacao().incremento(TrataLista().caixaBaixa('AC - BL A 8P - Isolamento Quarto A803 - 37')))
print(Pontuacao().incremento(TrataLista().caixaBaixa('AC - BL C - 2SS - Sala Cirúrgica 03 - UTA-CC-03 e EX-CC-03 - 34')))
print(Pontuacao().incremento(TrataLista().caixaBaixa('AC - BL Peixotinho - Sala Técnica Elétrica - FC-CM-01 - 220')))
print(Pontuacao().incremento(TrataLista().caixaBaixa('GS - Gases - Somatório Gases - 000')))

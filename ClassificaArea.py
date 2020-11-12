from TrataNomenclaturaEquip import TrataLista as TL
from PontuacaoInicial import Pontuacao as PI
from PontuacaoFinal import Pontuacao as PF


class GrauDeRisco:
    def __init__(self):
        # Define as strings que podem conter na nomenclatura do equipamento
        self.C = ['CAG', '', '', '', '']  # Critico
        self.S = ['', '', '', '', '']  # Substancial
        self.M = ['', '', '', '', '']  # Moderado
        self.A = ['', '', '', '', '']  # Aceitável

    def defineGrau(self, equipamento):
        # Risco à vida
        if TL().compara(equipamento, self.C) != '':
            return 4

        # Financeiro/Saúde
        elif TL().compara(equipamento, self.S) != '':
            return 3

        # Operacional
        elif TL().compara(equipamento, self.M) != '':
            return 2

        # Desconforto
        elif TL().compara(equipamento, self.A) != '':
            return 1


class Afetacao:
    def __init__(self):
        # Define as strings que podem conter na nomenclatura do equipamento
        self.G = ['CAG', '', '', '', '', '', '', '']  # Global
        self.L = ['Isolamento', 'Cirúrgico', 'Obstétrico', 'Sala', 'CC', 'CO', 'UTI', '', '']  # Local

    def defineZona(self, equipamento):  # Local ou Global
        # Geral
        if TL().compara(equipamento, self.G) != '':
            return 2

        # Local
        elif TL().compara(equipamento, self.L) != '':
            return 1


class TipoComponente:
    def __init__(self):
        self.P = ['Ventilador', 'Exaustor', 'Fancoil', 'Multimedidor', 'Hidrômetro']
        self.U = ['Torre', 'BAGP', 'BAGS', 'BAC', 'Rack']

    def defineTipo(self, equipamento):
        # Parte de um sistema
        if TL().compara(equipamento, self.P) != '':
            return 2

        # Componente único
        elif TL().compara(equipamento, self.U) != '':
            return 1


# Classificação sem definição do código da área
class ClassificacaoInicial:
    def __init__(self, equipamento):
        self.GDR = GrauDeRisco().defineGrau(equipamento)
        self.AFT = Afetacao().defineZona(equipamento)
        self.TC = TipoComponente().defineTipo(equipamento)

    def pontuacaoInicial(self, grau, afetacao, tipo):
        resultado = [grau, afetacao, tipo]
        return resultado

    def run(self):
        return PI().inicial(self.pontuacaoInicial(self.GDR, self.AFT, self.TC))


# Classificação após definicao do código da área
class Classificacao:
    def __init__(self):
        pass

    def run(self, equipamento):
        return ClassificacaoInicial(equipamento).run() + PF().incremento(equipamento)

class Areas:
    def __init__(self):
        pass

    def centroCirurgico(self):
        pass

    def salaIsolamento(self):
        pass


class Operacao(Areas):
    def __init__(self):
        pass

    def somaTudo(self):
        self.centroCirurgico()+self.salaIsolamento()

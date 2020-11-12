class Pontuacao:
    def __init__(self):
        pass

    def inicial(self, criterios):
        if criterios == [1, 1, 1]:
            return 0
        elif criterios == [1, 1, 2]:
            return 150
        elif criterios == [1, 2, 1]:
            return 200
        elif criterios == [1, 2, 2]:
            return 350
        elif criterios == [2, 1, 1]:
            return 400
        elif criterios == [2, 1, 2]:
            return 450
        elif criterios == [2, 2, 1]:
            return 500
        elif criterios == [2, 2, 2]:
            return 550
        elif criterios == [3, 1, 1]:
            return 600
        elif criterios == [3, 1, 2]:
            return 650
        elif criterios == [3, 2, 1]:
            return 700
        elif criterios == [3, 2, 2]:
            return 750
        elif criterios == [4, 1, 1]:
            return 800
        elif criterios == [4, 1, 2]:
            return 850
        elif criterios == [4, 2, 1]:
            return 900
        elif criterios == [4, 2, 2]:
            return 950

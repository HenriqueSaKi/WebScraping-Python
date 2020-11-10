equipamento = input("Digite algo: ")
print(remover_acentos(equipamento).lower())

if remover_acentos(equipamento).lower() == 'Cirurgico'.lower():
    print("Reconheceu")
else:
    print("Não deu certo")

class GrauRisco:
    def __init__(self):
        pass

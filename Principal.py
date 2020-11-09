from ValidaRequisicao import ListaEquipamentosG5
from WebScrapingG5site import ListaSitesG5
import getpass


def preencherLogin():
    print("Favor preencha os campos solicitados.")
    email = input("Informe seu email: ")
    senha = getpass.getpass("Informe sua senha: ")
    ListaSitesG5().login(email, senha)

def preencherSite():
    site = input("Qual é o nome do site?\nObs: O mesmo deve ser descrito exatamente igual como está no G5.\nSite: ")
    ListaSitesG5().verificaSiteG5(site)

answer = 's'
while answer == 's':
    preencherLogin()
    while(ListaSitesG5().testaLogin() == False):
        preencherLogin()

    site = input("Qual é o nome do site?\nObs: O mesmo deve ser descrito exatamente igual como está no G5.\nSite: ")

    ListaEquipamentosG5().run(site)
    answer = input("Deseja pesquisar outro equipamento?? ")

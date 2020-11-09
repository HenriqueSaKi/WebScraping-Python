from ValidaRequisicao import ListaEquipamentosG5
from WebScrapingG5site import ListaSitesG5

print("Favor preencha os campos solicitados.")
email = input("Informe seu email: ")
senha = input( "Informe sua senha: " )
ListaSitesG5().login(email, senha)

while(ListaSitesG5().testaLogin() == False):
    print("Usuário ou senha inválido!")
    print("Favor preencha os campos solicitados.")
    email = input("Informe seu email: ")
    senha = input("Informe sua senha: ")
    ListaSitesG5().login(email, senha)

site = input("Qual é o nome do site?\nObs: O mesmo deve ser descrito exatamente igual como está no G5.\nSite: ")

ListaEquipamentosG5().run(site)

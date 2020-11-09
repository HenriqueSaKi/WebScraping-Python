from WebScrapingG5site import ListaSitesG5

class ListaEquipamentosG5:
    def __init__(self):
        self.count = 0

    """ #To work with WebScrapingG5
    def verificaSeExiste(self, site):
        #Variable that stores list of G5's sites
        SitesG5 = ListaSitesG5().listarSitesG5()
        for i in SitesG5:
            if i == site:
                self.count = self.count + 1
        return self.count
    
    def run(self, site):
        if self.verificaSeExiste(site) > 0:
            print("Site encontrado!")
            print("Segue Informações:\n")
            print("Site: " + site)
            print("Equipamentos:")
            ListaSitesG5().listarEquipamentoG5(site)
        else:
            print("Site não encontrado, favor verificar.")
    """

    #To work with WebScrapingG5site
    def run(self, site):
        ListaSitesG5().listarEquipamentoG5(site)

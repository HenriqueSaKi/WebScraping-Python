from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options)
listaSites = []
listaEquipamentos = []

class ListaSitesG5:
    def __init__(self):
        pass

    def login(self, email, senha):
        driver.get("https://g5config.oxyn.com.br/app/sites_list")
        #Datas must be from someone that has g5config access
        driver.find_element_by_id('user_email').send_keys('{}'.format(email))
        driver.find_element_by_id('user_senha').send_keys('{}'.format(senha))
        driver.find_element_by_xpath("//input[@value='Entrar']").click()

    def testaLogin(self):
        if driver.find_elements_by_xpath("//p[contains(text(), 'Usuário ou senha inválido')]"):
            return False
        elif driver.find_elements_by_xpath("//thead//th[@align='center']"):
            return True

    def selectSite(self, site):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '{}')]".format(site))))
        elemento = driver.find_element_by_xpath("//a[contains(text(), '{}')]".format(site))
        driver.get(elemento.get_attribute('href'))

    def listarSitesG5(self):
        print("Validando sites do G5.")
        time.sleep(1)
        print("Aguarde, isso pode levar alguns minutos...")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@id='newspaper-b']//tbody")))
        sites = driver.find_elements_by_xpath("//tbody//tr//td")
        for i in sites:
            listaSites.append(i.text)
        print("Pronto!")
        time.sleep(2)
        #List comprehension to remove blank spaces
        x = [i for i in listaSites if i!= '']
        return x

    def listarEquipamentoG5(self, site):
        self.selectSite(site)
        #Warrant that I'm into equipment page
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//th[@id='equipamentos']")))
        #Wait until detect equipments text
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//table[@id='newspaper-b_sub']//tbody//tr[1]//td[2]//a")))
        equipamentos = driver.find_elements_by_xpath("//table[@id='newspaper-b_sub']//tbody//tr//td[2]//a")
        for i in equipamentos:
            #Include equipment name into list listaEquipamentos
            listaEquipamentos.append(i.text)
            print(i.text)

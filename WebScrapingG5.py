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

    def login(self):
        driver.get("https://g5config.oxyn.com.br/app/sites_list")
        #Os dados devem ser de uma pessoa que contém acesso ao G5 config.
        driver.find_element_by_id('user_email').send_keys('')
        driver.find_element_by_id('user_senha').send_keys('')
        driver.find_element_by_xpath("//input[@value='Entrar']").click()

    def selectSite(self, site):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '{}')]".format(site))))
        elemento = driver.find_element_by_xpath("//a[contains(text(), '{}')]".format(site))
        driver.get(elemento.get_attribute('href'))

    def listarSitesG5(self):
        print("Validando sites do G5.")
        time.sleep(1)
        print("Aguarde, isso pode levar alguns minutos...")
        self.login()
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
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//th[@id='equipamentos']")))
        equipamentos = driver.find_elements_by_xpath("//table[@id='newspaper-b_sub']//tbody//tr//td[2]//a")
        for i in equipamentos:
            listaEquipamentos.append(i.text)
            print(i.text)
        time.sleep(2)
        print("Fim da busca.")

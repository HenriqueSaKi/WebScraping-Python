#This code allow any person that have G5 website access
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
        driver.get("https://g5.oxyn.com.br/")
        driver.find_element_by_id('user_email').send_keys('{}'.format(email))
        driver.find_element_by_id('user_senha').send_keys('{}'.format(senha))
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def testaLogin(self):
        if driver.find_elements_by_xpath("//div[contains(text(), 'Usuário ou senha inválido')]"):
            return False
        elif driver.find_elements_by_xpath("//div[@id='nav']"):
            return True

    def verificaSiteG5(self):
        if driver.find_element_by_xpath("//li[contains(text(), 'Nenhum ')]") #####VALIDAR

    def acessaSite(self, site):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//tbody//tr[@class='odd']")))
        while verificaSiteG5() == False: ######VALIDAR
            driver.find_element_by_xpath("//span[@class='select2-selection__rendered']").click()
            driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(site)
        driver.find_element_by_xpath("//span[@class='select2-results']//ul//li[1]").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//tbody//tr//a[contains(text(), '{}')]".format(site))))

    def listarEquipamentoG5(self, site):
        self.acessaSite(site)
        print("Aguarde, estamos validando as informações")
        time.sleep(4)
        driver.find_element_by_xpath("//span[contains(text(), 'Selecione um equipamento')]").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id='select2-eqpts-results']")))
        equipamentos = driver.find_elements_by_xpath("//ul[@id='select2-eqpts-results']//li")
        for i in equipamentos:
            #Include equipment name into list listaEquipamentos
            listaEquipamentos.append(i.text)
            print(i.text)
        print("Temos um total de {} equipamentos instanciados neste site".format(len(equipamentos)))

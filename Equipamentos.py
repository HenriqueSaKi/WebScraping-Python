from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
listaSites = []

class GetTableData:
    def __init__(self):
        pass

    def login(self):
        driver.get("https://g5config.oxyn.com.br/app/sites_list")
        driver.find_element_by_id('user_email').send_keys('')
        driver.find_element_by_id('user_senha').send_keys('')
        driver.find_element_by_xpath("//input[@value='Entrar']").click()

    def accessSite(self):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@id='newspaper-b']//tbody//tr")))
        #driver.find_element_by_xpath()

    def run(self):
        self.login()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@id='newspaper-b']//tbody")))
        sites = driver.find_elements_by_xpath("//tbody//tr//td")
        for i in sites:
            listaSites.append(i.text)

        print(listaSites)


GetTableData().run()
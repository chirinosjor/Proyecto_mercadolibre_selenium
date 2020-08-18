import unittest
from selenium import webdriver
from time import sleep


class ProyectoML(unittest.TestCase):

    # Sirve para seleccionar la secuencia de prueba
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        # 1- Ingresar a Mercadolibre.com
        driver.get("https://mercadolibre.com/")
        driver.implicitly_wait(5)      
        
    def test_search_ps(self):
        driver = self.driver
        # 2- Seleccionar Colombia
        country_select = driver.find_element_by_id('CO')
        country_select.click()

        sleep(3)


        # 3- Buscar "PlayStation 4"
        search_field = driver.find_element_by_class_name('nav-search-input')
        search_field.clear() 
        search_field.send_keys('PlayStation 4')
        search_field.submit()

        sleep(3)

        # 4 - Seleccionar Bogotá
        city_selector = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-filter-groups > dl:nth-child(8) > dd:nth-child(2) > a > span.ui-search-filter-name')
        city_selector.click()
        driver.refresh()

        sleep(3)

        # 5- Seleccionar articulos nuevos
        condition_selector = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-filter-groups > dl:nth-child(6) > dd:nth-child(2) > a > span.ui-search-filter-name')
        condition_selector.click()

        sleep(3)

        # 6- Ordenar por mayor precio
        sort_select = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div')
        sort_select.click()

        price_select = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/div/div/a')
        price_select.click()

        sleep(3)

        # 7 - Obtener primeros 5 nombres y precios

        names = []
        prices = []

        for i in range(5):
            article = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            names.append(article)

        for i in range(5):
            price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            prices.append(price)

        results = dict(zip(names, prices))
        print(results)








    # Sirve para cerrar las ventanas luego de que se corra la prueba para que no consuma mas memoria
    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
import os 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class CMSScrapper(object):
    def __init__(self, domain):
        self.BASE_URL       = "https://whatcms.org/"
        self.domain         = domain
        self.driver_path    = f"{os.getcwd()}/drivers/geckodriver"


    def get_infos(self):
        infos = {}

        self.driver = webdriver.Firefox(executable_path=self.driver_path)
        self.driver.get(self.BASE_URL)

        input_field = self.driver.find_element_by_xpath('//*[@id="what-cms-size"]')
        input_field.send_keys(self.domain)
        input_field.send_keys(Keys.RETURN)

        time.sleep(3)

        response = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]")
        scrapper = BeautifulSoup(response.get_attribute("innerHTML"), "html.parser")
        td_array = [item.find_all("td") for item in scrapper.find_all("tr")]

        for tds in td_array[1:]:
            key = tds[0].contents[0]
            infos[ key ] = []

            for td in tds[1:]:
                if td.find("a") is not None:
                    infos[ key ].append(td.find("a").contents[0])
                else:
                    infos[ key ].append(td.contents)

        self.driver.close()
        return (infos)
        
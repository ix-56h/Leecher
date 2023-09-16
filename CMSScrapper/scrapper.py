import os 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


class CMSScrapper(object):
	def __init__(self, domain):
		self.BASE_URL = "https://whatcms.org/"
		self.domain = domain
		self.driver_path = f"{os.getcwd()}/drivers/geckodriver"
		# Chrome options
		self.chrome_options = Options()
		self.chrome_options.add_argument("--headless")

		self.driver = webdriver.Chrome(executable_path=self.driver_path, options=self.chrome_options)


	def get_infos(self):
		infos = {}

		self.driver.get(self.BASE_URL)

		input_field = self.driver.find_element_by_xpath('//*[@id="what-cms-size"]')
		input_field.send_keys(self.domain)
		input_field.send_keys(Keys.RETURN)

		time.sleep(3)

		response = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]")
		scrapper = BeautifulSoup(response.get_attribute("innerHTML"), "html.parser")
		td_array = [item.find_all("td") for item in scrapper.find_all("tr")]
		infos = []

		for tds in td_array[1:]:
			sublist = []

			for index, td in enumerate(tds):
				if td.find("a") is not None:
					sublist.append(td.find("a").contents[0])
				else:
					if len(td.contents) != 0:
						sublist.append(td.contents[0])
					else:
						sublist.append(None)

				if (index + 1) % 3 == 0:
					infos.append(sublist)
					sublist = []

		self.driver.close()
		return (infos)
		
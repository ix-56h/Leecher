#!/usr/bin/env python
import cfscrape
from bs4 import BeautifulSoup


class CMScrapper(object):
    def __init__(self, domain):
        self.URL = "https://whatcms.org"
        self.domain = domain
        self.head = {
            "Host": "whatcms.org",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }
        scraper     =   cfscrape.create_scraper()  # returns a CloudflareScraper instance
        response    =   scraper.get(self.URL, headers=self.head)
        soup        =   BeautifulSoup(response.content, "html.parser")
        self.nb     =   soup.find("input", {"name" : "nb"}).get("value")
        #print(self.nb)

    def get_infos(self):
        scraper     =   cfscrape.create_scraper()  # returns a CloudflareScraper instance
        response    =   scraper.get(self.URL+"?s="+self.domain+"&na=&nb="+self.nb)
        with open('x.html', 'wb') as file:
            file.write(response.content)
        #soup = BeautifulSoup(resp.content, "html.parser")
        #print(soup.find("table", {"class" : "table"}))
        #infos = soup.find("div", {"id" : "result_destination"}).find("div", {"class" : "card-body"}).find("div") 

head = {
        "Host": "whatcms.org",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "TE": "Trailers"
        }
scraper =   cfscrape.create_scraper()  # returns a CloudflareScraper instance
x       =   scraper.get("https://whatcms.org", headers=head)
soup    =  BeautifulSoup(x.content, "html.parser")
nb = soup.find("input", {"name" : "nb"}).get("value")

x = scraper.get("https://whatcms.org/?s=test.fr&na=&nb="+nb, headers=head)

with open('x.html', 'wb') as file:
    file.write(x.content)
#x = CMScrapper("test.fr").get_infos()

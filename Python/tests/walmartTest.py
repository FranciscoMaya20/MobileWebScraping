from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import time

class Walmart_Test(object):

    def __init__(self,item):
        self.walmartURL = "https://www.walmart.com/"
        self.items = item

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        options=self.options)

        
        self.driver.get(self.walmartURL)

        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.html = self.soup.prettify('utf-8')

    def findItem(self):
        self.driver.get(self.baseURL)

        searchBarInput = self.driver.find_element_by_id("global-search-input")
        searchBarInput.send_keys(self.item)

        time.sleep(4)

        searchButton = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/section/div[2]/div/div[3]/div[2]/div/form/button[3]/span/img')
        searchButton.click()

        time.sleep(4)

        itemResult = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/section/div/div/div/div[4]/div[2]/div[2]/ul/li[1]/div/div[2]/div[5]/div/a/span')
        itemResult.click()
        
        try:
            price = str(self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[1]/section/div[1]/div[1]/div[1]/span/div/span[1]/span/span[2]/span[3]').text)
        except:
            raise Exception("No Price Found")

        return price

    def getPrice(self,url):
        self.driver.get(url)
        
        try:
            price = self.driver.find_element_by_id("price-mark").text
        except:
            raise Exception("No Our Price Found")

        try:
            price = self.driver.find_element_by_id("price-mark").text
        except:
            raise Exception("No DealPrice Found")

        nonDecimal = re.compile(r'[^\d.]+')
        price = nonDecimal.sub('', price)

        return price
        

    def closeSession(self):
        self.webDriver.close()
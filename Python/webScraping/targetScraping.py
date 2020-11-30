from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
import time

class Target_Test(object):

    def __init__(self,item):
        self.targetURL = "https://www.target.com/"
        self.item = item

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        options=self.options)

        
        self.driver.get(self.targetURL)

        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.html = self.soup.prettify('utf-8')

    def findItem(self):
        self.driver.get(self.targetURL)

        searchBarInput = self.driver.find_element_by_id("search")
        searchBarInput.send_keys(self.item)

        time.sleep(4)

        searchButton = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/nav/div[1]/form/button[2]')
        searchButton.click()

        time.sleep(4)

        itemResult = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[4]/div[2]/div/div[2]/div[3]/div[2]/ul/li[1]/div/div[1]/h3/a/div/div/div/picture/img')
        itemResult.click()
        
        try:
            price = str(self.driver.find_element_by_xpath('$12.99').text)
        except:
            raise Exception("No Price Found")

        return price

    def getPrice(self,url):
        self.driver.get(url)
        
        try:
            price = self.driver.find_element_by_id("product-price").text
        except:
            raise Exception("No Our Price Found")

        try:
            price = self.driver.find_element_by_id("product-price").text
        except:
            raise Exception("No DealPrice Found")

        nonDecimal = re.compile(r'[^\d.]+')
        price = nonDecimal.sub('', price)

        return price
        

    def closeSession(self):
        self.webDriver.close()


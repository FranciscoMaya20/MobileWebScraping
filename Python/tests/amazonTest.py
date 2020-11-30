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


class Amazon_Test(object):

    def __init__(self,item):
        self.amazonUrl = "https://www.amazon.com"
        self.item = item
        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
        options=self.options)

        self.driver.get(self.amazonUrl)

        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html,'html.parser')
        self.html = self.soup.prettify('utf-8')

        

    def findItem(self):
        self.driver.get(self.amazonUrl)

        searchBarInput = self.driver.find_element_by_id("twotabsearchtextbox")
        searchBarInput.send_keys(self.item)

        time.sleep(4)

        searchButton = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
        searchButton.click()

        time.sleep(3)

        itemResult = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/h2/a/span')
        itemResult.click()

        try:
            price = str(self.driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text)
        except:
            raise Exception("No Price Found")


        nonDecimal = re.compile(r'[^\d.]+')
        price = nonDecimal.sub('', price)

        return price


    def getPrice(self,url):
        self.driver.get(url)

        try:
            price = self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            raise Exception("No Price Found")

        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
            raise Exception("No DealPrice Found")

        nonDecimal = re.compile(r'[^\d.]+')
        price = nonDecimal.sub('', price)

        return price

    def closeSession(self):
        self.driver.close()





from amazonTest import Amazon_Test
from targetTest import Target_Test
from walmartTest import Walmart_Test
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
import time

def main():
    item = "toilet paper"

    amazon = Amazon_Test(item)
    target = Target_Test(item)
    walmart = Walmart_Test(item)

    amazonPrice = amazon.findItem()
    targetPrice =target.findItem()
    walmartPrice = walmart.findItem()

    print(f"Amazon: {amazonPrice}")
    print(f"Target Price: {targetPrice}")
    print(f"Walmart Price: {walmartPrice}")


if __name__=="__main__":
    main()
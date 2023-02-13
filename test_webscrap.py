from selenium import webdriver
from selenium.webdriver.common.by import By
#from openpyxl import Workbook
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import re
import json
import pytest

def test_webscrap():

  
  driver=webdriver.Chrome(ChromeDriverManager().install())
  driver.maximize_window()
  driver.get("https://www.amazon.in/")
  driver.implicitly_wait(10)


  driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("iphones")
  driver.find_element(By.XPATH,"//input[@value='Go']").click()
  driver.find_element_by_xpath('//span[contains(text(),"Apple iPhone 14 128GB Starlight")]').click()

  driver.switch_to.window(driver.window_handles[1])
  title=driver.title
  items=title.split(':')
  print(items)

  itemsdict={itm for itm in items}
  d1=dict(enumerate(itemsdict))
  print(d1)

  driver.switch_to.window(driver.window_handles[0])
  driver.close()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.audible.in/search')
driver.implicitly_wait(10)
driver.maximize_window()
products = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
book_title = []
book_author = []
book_length = []
for product in products:
   #book_title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
   book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
   book_length.count(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)
#ValueError: All arrays must be of the same lengt if i execute below code
#df_books1 = pd.DataFrame({'title': book_title, 'author': book_author, 'length1': book_length})
df_books = pd.DataFrame({'author': book_author})
df_books.to_csv('booksjuly10.csv', index=False)
print(df_books)






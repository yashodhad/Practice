from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Ser


#driver=webdriver.Chrome(service=Ser(ChromeDriverManager().install()))
driver = webdriver.Firefox()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Sumsung phones")
driver.find_element(By.XPATH,"//input[@value='Go']").click()
driver.find_element(By.XPATH,'//span[text()="Samsung"]').click()
phonenames=driver.find_elements(By.XPATH, '//span[contains(@class,"a-color-base a-text-normal")]')
prices=driver.find_elements(By.XPATH, '//span[contains(@class,"a-price-whole")]')
myphone=[]
myprice=[]

for phone in phonenames:
   # print(phone.text)
    myphone.append(phone.text)
for prize in prices:
   # print(prize.text)
    myprice.append(prize.text)
df_books = pd.DataFrame({'phone': myphone,'price': myprice})
df_books.to_csv('amazon.csv', index=False)
print(df_books)



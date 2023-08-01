from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


url = 'https://www.investing.com/rates-bonds/south-korea-10-year-bond-yield-historical-data'
dr = webdriver.Chrome()
dr.get(url)

act = ActionChains(dr)


element1 = dr.find_element(By.XPATH, '//*[@id="datePickerIconWrap"]')

act.click(element1).perform()  # element1  클릭 동작을 수

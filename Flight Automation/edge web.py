from selenium import webdriver
from selenium.webdriver.edge.service import Service
ser_obj = Service("D:\Python Pycharm\Flight Automation\Driver\msedgedriver.exe")
driver = webdriver.edge(service =ser_obj)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
driver.close()
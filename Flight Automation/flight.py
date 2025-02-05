
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Initialize the WebDriver

# Open a URL
driver.get("https://www.goibibo.com/")
try:
    # Launch website
    driver.get("https://www.goibibo.com/")
    driver.maximize_window()

    # Wait for the flight search form to load
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[5]/div/div/div[2]/div[1]/div/div[2]/div/input'))
    )

    # Input "From" location
    from_location = 'Mumbai (BOM)'  # Change this to your desired "From" location
    from_field = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div/div/div[2]/div[1]/div/div[2]/div/input")
    from_field.send_keys(from_location)
    # Wait for auto-suggestions and select the first option
    time.sleep(20)  # Adjust if necessary
    from_field.send_keys(Keys.ENTER)

    to_location = 'Hyderabad (HYD)'  # Change this to your desired "To" location
    to_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[5]/div/div/div[2]/div[2]/div/div[2]/div/input')
    to_field.send_keys(to_location)
    time.sleep(20)
    to_field.send_keys(Keys.ENTER)


    # Optionally wait to see the result before quitting
    time.sleep(15)

finally:
    # Ensure the browser is closed
    driver.quit()
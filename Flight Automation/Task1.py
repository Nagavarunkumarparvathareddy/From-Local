from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)
driver.implicitly_wait(10)

# Navigate to Goibibo's website
driver.get("https://www.goibibo.com/")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

def close_popup():
    """Attempts to close a popup if it appears."""
    try:
        popup_close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/span/span"))
        )
        popup_close_button.click()
        print("Popup closed successfully.")
    except Exception as e:
        print("No popup found or unable to close: ", e)

try:
    # Attempt to close popup
    close_popup()

    # Wait for the "From" location input field to be clickable
    from_location = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//p[@class='sc-12foipm-6 erPfRs' and text()='Enter city or airport']")))
    from_location.click()
    print("From location clicked successfully!")

    # Enter "Hyderabad" in the From input
    from_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='text' and @value='']")))  # Targeting input with type='text'
    from_input.clear()
    from_input.send_keys("Hyderabad")
    time.sleep(3)  # Wait for suggestions to load

    # Select the suggestion that matches "Hyderabad"
    suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Rajiv Gandhi International Airport')]"
    first_suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
    first_suggestion.click()
    print("Hyderabad selected from the suggestions!")

    # Enter "Delhi" in the To input
    to_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='text' and @value='']")))
    to_input.clear()
    to_input.send_keys("Delhi")
    time.sleep(3)  # Wait for suggestions to load

    # Select the suggestion that matches "Delhi"
    to_suggestion_xpath = "//div[@class='sc-12foipm-32 jVTqNw']//p[contains(text(), 'Indira Gandhi International Airport')]"
    to_first_suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, to_suggestion_xpath)))
    to_first_suggestion.click()
    print("Delhi selected from the suggestions!")

    # Open the calendar
    calendar_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='sc-12foipm-8 eXKWBG fswDownArrow']")))
    calendar_input.click()
    print("Calendar opened.")

    # Wait for the calendar and select the date
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='DayPicker']")))
    time.sleep(2)  # Ensure the calendar is loaded completely
    date_to_select = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label='Mon Jan 06 2025']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", date_to_select)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", date_to_select)
    print("Date Mon Jan 06 2025 selected successfully!")

    time.sleep(2)
    # Click the "Search Flights" button
    search_flights_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='sc-12foipm-71 cJDpIZ']//span[text()='SEARCH FLIGHTS']"))
    )
    # Scroll the button into view
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", search_flights_button)

    # Wait until the button is clickable
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-12foipm-71 cJDpIZ']//span[text()='SEARCH FLIGHTS']"))
    )
    search_flights_button.click()
    print('Search Flight button clicked successfully')

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    time.sleep(100)
    driver.quit()

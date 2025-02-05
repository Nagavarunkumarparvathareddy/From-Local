from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Set up the WebDriver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the Cleartrip website
driver.get("https://www.cleartrip.com/")
driver.maximize_window()

try:
    # Wait for the pop-up to appear and close it
    try:
        close_button_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, close_button_xpath))
        ).click()
        print("Pop-up closed successfully.")
    except Exception as e:
        print(f"Error closing the pop-up: {e}")

    # Locate and click on the "Where from?" input field
    from_location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where from?']"))
    )
    from_location.click()
    print("From location clicked successfully!")

    # Enter "Bangalore" in the input field
    from_location.send_keys("Bangalore")
    time.sleep(3)  # Allow suggestions to load

    # Locate and select the specific suggestion for "Bangalore, IN - Kempegowda International Airport (BLR)"
    suggestion_xpath_bangalore = "//div[@class='mr-4']//p[contains(text(), 'Bangalore, IN - Kempegowda International Airport (BLR)')]"
    specific_suggestion_bangalore = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, suggestion_xpath_bangalore))
    )
    specific_suggestion_bangalore.click()
    print("Bangalore, IN - Kempegowda International Airport (BLR) selected from the suggestions!")

    # Locate and click on the "Where to?" input field
    to_location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where to?']"))
    )
    to_location.click()
    print("To location clicked successfully!")

    # Enter "Hyderabad" in the input field
    to_location.send_keys("Hyderabad")
    time.sleep(3)  # Allow suggestions to load

    # Locate and select the specific suggestion for "Hyderabad, IN - Rajiv Gandhi International (HYD)"
    suggestion_xpath_hyderabad = "//ul[@class='airportList']//p[contains(text(), 'Hyderabad, IN - Rajiv Gandhi International (HYD)')]"
    hyderabad_suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, suggestion_xpath_hyderabad))
    )
    hyderabad_suggestion.click()
    print("Hyderabad, IN - Rajiv Gandhi International (HYD) selected from the suggestions!")

    # Locate and click on the calendar icon (the current date "Tue, Jan 7")
    calendar_icon_xpath = "//div[contains(@class, 'c-inherit') and contains(text(), 'Thu, Jan 8')]"
    calendar_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, calendar_icon_xpath))
    )
    calendar_icon.click()
    print("Calendar icon (Tue, Jan 7) clicked successfully!")

    # Wait for the calendar to load and select the specific date (Jan 9, 2025)
    date_element_xpath = "//div[@class='Day-grid flex flex-middle flex-column flex-top']" \
                         "//div[@class='p-1 day-gridContent fs-14 fw-500 flex flex-middle flex-column flex-center flex-top' and contains(text(), '9')]"
    date_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, date_element_xpath))
    )
    date_element.click()
    print("Jan 9, 2025 selected successfully!")

    # Now click the "Search flights" button
    search_flights_button_xpath = "//button[@class='sc-dAlyuH cIApyz']//div[@class='sc-aXZVg ibgoAF']//h4[contains(text(), 'Search flights')]"
    search_flights_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, search_flights_button_xpath))
    )
    time.sleep(2)
    search_flights_button.click()
    print("Search flights button clicked successfully!")

    # Wait for the "Non-stop" checkbox and click it
    non_stop_checkbox_xpath = '//label[@class="checkbox w-100p checkbox flex-1 bs-border w-100p br-4 h-7 px-1 intl_checkbox py-1 hover:bg-neutral-0"]'
    non_stop_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, non_stop_checkbox_xpath))
    )
    non_stop_checkbox.click()
    print("Non-stop checkbox selected successfully!")

    # Wait for the price slider to appear
    slider_xpath = "//div[@aria-valuemax='22300']"
    slider = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, slider_xpath))
    )

    # Get slider dimensions and calculate offset
    slider_width = slider.size['width']
    max_value = 22300
    min_value = 19090
    target_value = 10101

    # Calculate the proportion of the movement
    proportion = (target_value - min_value) / (max_value - min_value)
    move_by = proportion * slider_width

    # Perform the action using ActionChains
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(move_by - slider_width / 2, 0).release().perform()
    print(f"Slider moved to value {target_value} successfully!")

    # Wait for flight cards to appear
    flight_cards_xpath = "//div[contains(@class, 'ow-tuple-container__details-a')]"
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, flight_cards_xpath))
    )

    # Extract flight details
    flights = driver.find_elements(By.XPATH, flight_cards_xpath)
    flight_data = []

    for flight in flights:
        try:
            # Extract airline name and code
            airline = flight.find_element(By.XPATH, ".//p[@class='fw-500 fs-2 c-neutral-900']").text
            flight_code = flight.find_element(By.XPATH, ".//p[@class='fs-1 c-neutral-400 pt-1']").text

            # Extract departure time, duration, arrival time, and stops
            departure_time = flight.find_element(By.XPATH, ".//p[contains(@class, 'fw-400 c-neutral-900')][1]").text
            duration = flight.find_element(By.XPATH, ".//p[contains(@class, 'fw-400 c-neutral-400 ta-center')]").text
            arrival_time = flight.find_element(By.XPATH, ".//p[contains(@class, 'fw-400 c-neutral-900 ta-center')][1]").text
            stops = flight.find_element(By.XPATH, ".//p[contains(@class, 'c-neutral-400 lh-copy')]").text

            # Extract price
            price = flight.find_element(By.XPATH, ".//p[contains(@class, 'fs-5 fw-700 c-neutral-900 ta-right')]").text

            # Append the data to the list
            flight_data.append({
                "Airline": airline,
                "Flight Code": flight_code,
                "Departure Time": departure_time,
                "Duration": duration,
                "Arrival Time": arrival_time,
                "Stops": stops,
                "Price": price
            })
        except Exception as e:
            print(f"Error extracting flight details: {e}")

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(flight_data)

    # Save the DataFrame to a CSV or Excel file
    df.to_csv("flight_details.csv", index=False)

    print("Flight details saved successfully to flight_details.csv")

    # Keep the browser open until the user manually closes it
    print("Execution completed. Please manually close the browser window when done.")
    input("Press Enter to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

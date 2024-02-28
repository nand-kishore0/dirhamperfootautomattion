from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
import csv
from datetime import datetime

today_date = datetime.now().strftime("%m/%d/%Y")
current_date_time = datetime.now().strftime("%m/%d/%Y, %I:%M %p")

BASE_URL = "https://main.d9sib1cvnq16j.amplifyapp.com"


def open_browser(urls, first_name, last_name, email, password, re_password, businedirss):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(urls)
    time.sleep(3)

    driver.find_element(By.NAME, "first_name").send_keys(first_name)
    time.sleep(1)

    driver.find_element(By.NAME, "last_name").send_keys(last_name)
    time.sleep(1)

    driver.find_element(By.NAME, "email").send_keys(email)
    time.sleep(1)

    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)

    driver.find_element(By.NAME, "password_confirmation").send_keys(re_password)
    time.sleep(1)

    business_radio = driver.find_element(By.NAME, 'is_business')
    business_radio.is_selected()
    business_radio.click()
    time.sleep(1)

    business_profile = driver.find_element(By.NAME, 'business_profile')
    business_profile.is_selected()
    business_profile.click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/form/button').click()
    time.sleep(3)

    already_registration = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div[2]').text
    time.sleep(1)

    if "user with this email address already exists." in already_registration:
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.NAME, 'email').send_keys(email)
        driver.find_element(By.NAME, 'password').send_keys(password)
        login = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[4]/button')
        login.click()
        time.sleep(2)

        driver.get(f"{BASE_URL}/profile")
        time.sleep(2)

        edit_profile = driver.find_element(By.CLASS_NAME, 'btn.bg-blue.text-white.hover-saffron')
        edit_profile.click()
        time.sleep(2)

        update_description = driver.find_element(By.ID, "description")
        update_description.send_keys("We are developer to upload multiple properties")
        time.sleep(2)

        address_input = driver.find_element(By.CLASS_NAME, "mt-fourteen")
        address_value = "dubai"
        address_input.send_keys(address_value)
        time.sleep(2)

        address_input.send_keys(Keys.ARROW_DOWN)
        address_input.send_keys(Keys.RETURN)
        time.sleep(10)

        select_company = driver.find_element(By.ID, "react-select-3-input")
        select_company.click()
        time.sleep(5)

        company_register = "test"
        select_company.send_keys(company_register)
        time.sleep(2)

        select_company.send_keys(Keys.ARROW_DOWN)
        select_company.send_keys(Keys.RETURN)
        time.sleep(2)

        # update_profile = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/main/div/form/div[2]/button")
        update_profile = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.bg-blue.text-white.hover-saffron.ml-4.mb-3")
        driver.execute_script("arguments[0].scrollIntoView(true);", update_profile)
        update_profile.click()

        time.sleep(600)

        #
        # try:
        #     # Find the input field by its ID
        #     check_company = driver.find_element(By.ID, "company")
        #
        #     # Get the value attribute of the input field
        #     company_value = check_company.get_attribute('value')
        #
        #     # Print the value if not blank
        #     if company_value.strip():
        #         print(f"The value is: {company_value}")
        #     else:
        #         print("The value is blank")
        #
        # except Exception as e:
        #     # Handle exceptions if the element is not found
        #     print(f"An error occurred: {e}")
        #
        # time.sleep(600)

        driver.get(f"{BASE_URL}/property/kind/")
        time.sleep(1)

        driver.get(f"{BASE_URL}/property/add?key=True")
        time.sleep(5)

        search_input = driver.find_element(By.CLASS_NAME, "mt-fourteen")
        location_value = "dubai"
        search_input.send_keys(location_value)
        time.sleep(2)
        search_input.send_keys(Keys.ARROW_DOWN)
        search_input.send_keys(Keys.RETURN)

        input_description = driver.find_element(By.ID, "description")
        input_description.send_keys("Hello World")
        time.sleep(1)

        input_property_name = driver.find_element(By.ID, "property_name")
        input_property_name.send_keys("Hello Worlds")
        time.sleep(1)

        building_type_dropdown = driver.find_element(By.ID, 'building_type')
        select = Select(building_type_dropdown)
        select.select_by_visible_text('Commercial')
        time.sleep(3)

        property_type_dropdown = driver.find_element(By.ID, 'property_type')
        select = Select(property_type_dropdown)
        select.select_by_visible_text('Office')
        time.sleep(1)

        property_label_dropdown = driver.find_element(By.ID, 'property_label')
        select = Select(property_label_dropdown)
        select.select_by_visible_text('Sale')
        time.sleep(2)

        property_price = driver.find_element(By.ID, 'property_price')
        property_price.send_keys("500000")
        time.sleep(1)

        construction_status_dropdown = driver.find_element(By.ID, 'construction_status')
        select = Select(construction_status_dropdown)
        select.select_by_visible_text('Completed')
        time.sleep(1)

        ownership_dropdown = driver.find_element(By.ID, 'ownership')
        select = Select(ownership_dropdown)
        select.select_by_visible_text('Self')
        time.sleep(1)

        property_size = driver.find_element(By.ID, 'property_size')
        property_size.send_keys("300")
        time.sleep(2)

        project_website = driver.find_element(By.ID, "project_website")
        project_website.send_keys("https://thinkdatalabs.com")
        time.sleep(2)

        property_status_dropdown = driver.find_element(By.ID, 'property_status')
        select = Select(property_status_dropdown)
        select.select_by_visible_text('Furnished')
        time.sleep(2)

        label_element = driver.find_element(By.ID, "amenities")
        label_element.click()
        time.sleep(10)

        save_button = driver.find_element(By.CLASS_NAME, 'btn.bg-blue')
        save_button.click()
        time.sleep(2)

        time.sleep(600)
        driver.quit()

    if "Welcome to Dirham Per Foot, Please check your email to verify" in already_registration:
        time.sleep(30)
        driver.get(f"{BASE_URL}/login")

        driver.find_element(By.NAME, 'email').send_keys(email)
        driver.find_element(By.NAME, 'password').send_keys(password)
        login = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[4]/button')
        login.click()
        time.sleep(2)

        driver.get(f"{BASE_URL}/profile")
        time.sleep(2)

        edit_profile = driver.find_element(By.CLASS_NAME, 'btn.bg-blue.text-white.hover-saffron')
        edit_profile.click()
        time.sleep(2)

        update_description = driver.find_element(By.ID, "description")
        update_description.send_keys("We are developer to upload multiple properties")
        time.sleep(2)

        address_input = driver.find_element(By.CLASS_NAME, "mt-fourteen")
        address_value = "dubai"
        address_input.send_keys(address_value)
        time.sleep(2)

        address_input.send_keys(Keys.ARROW_DOWN)
        address_input.send_keys(Keys.RETURN)
        time.sleep(10)

        select_company = driver.find_element(By.ID, "react-select-3-input")
        select_company.click()
        time.sleep(5)

        company_register = "test"
        select_company.send_keys(company_register)
        time.sleep(2)
        select_company.send_keys(Keys.ARROW_DOWN)
        select_company.send_keys(Keys.RETURN)
        time.sleep(2)

        update_profile = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.bg-blue.text-white.hover-saffron.ml-4.mb-3")
        driver.execute_script("arguments[0].scrollIntoView(true);", update_profile)
        update_profile.click()

        time.sleep(600)

        driver.get(f"{BASE_URL}/property/kind/")
        time.sleep(1)

        driver.get(f"{BASE_URL}/property/add?key=True")
        time.sleep(5)

        search_input = driver.find_element(By.CLASS_NAME, "mt-fourteen")
        location_value = "dubai"
        search_input.send_keys(location_value)
        time.sleep(2)

        search_input.send_keys(Keys.ARROW_DOWN)
        search_input.send_keys(Keys.RETURN)

        input_description = driver.find_element(By.ID, "description")
        input_description.send_keys("Hello World")
        time.sleep(1)

        input_property_name = driver.find_element(By.ID, "property_name")
        input_property_name.send_keys("Hello Worlds")
        time.sleep(1)

        building_type_dropdown = driver.find_element(By.ID, 'building_type')
        select = Select(building_type_dropdown)
        select.select_by_visible_text('Commercial')
        time.sleep(3)

        property_type_dropdown = driver.find_element(By.ID, 'property_type')
        select = Select(property_type_dropdown)
        select.select_by_visible_text('Office')
        time.sleep(1)

        property_label_dropdown = driver.find_element(By.ID, 'property_label')
        select = Select(property_label_dropdown)
        select.select_by_visible_text('Sale')
        time.sleep(2)

        property_price = driver.find_element(By.ID, 'property_price')
        property_price.send_keys("500000")
        time.sleep(1)

        construction_status_dropdown = driver.find_element(By.ID, 'construction_status')
        select = Select(construction_status_dropdown)
        select.select_by_visible_text('Completed')
        time.sleep(1)

        ownership_dropdown = driver.find_element(By.ID, 'ownership')
        select = Select(ownership_dropdown)
        select.select_by_visible_text('Self')
        time.sleep(1)

        property_size = driver.find_element(By.ID, 'property_size')
        property_size.send_keys("300")
        time.sleep(2)

        project_website = driver.find_element(By.ID, "project_website")
        project_website.send_keys("https://thinkdatalabs.com")
        time.sleep(2)

        property_status_dropdown = driver.find_element(By.ID, 'property_status')
        select = Select(property_status_dropdown)
        select.select_by_visible_text('Furnished')
        time.sleep(2)

        label_element = driver.find_element(By.ID, "amenities")
        label_element.click()
        time.sleep(10)

        save_button = driver.find_element(By.CLASS_NAME, 'btn.bg-blue')
        save_button.click()
        time.sleep(2)

        time.sleep(600)
        driver.quit()

    time.sleep(600)
    driver.quit()


if __name__ == "__main__":
    csv_file = "data.csv"
    data = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)

    urls = []
    first_name = []
    last_name = []
    email = []
    password = []
    re_password = []
    business = []

    for item in data:
        urls.append(item[0])
        first_name.append(item[1])
        last_name.append(item[2])
        email.append(item[3])
        password.append(item[4])
        re_password.append(item[5])
        business.append(item[6])

    urls = urls
    first_name = first_name
    last_name = last_name
    email = email
    password = password
    re_password = re_password
    business = business

    processes = []
    for i in range(len(urls)):
        process = Process(target=open_browser, args=(
            urls[i], first_name[i], last_name[i], email[i], password[i], re_password[i], business[i]))
        processes.append(process)
        process.start()
    time.sleep(10)

    for process in processes:
        process.join()

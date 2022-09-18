from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re


chrome_driver_path = "C:\\Users\\acer\\Desktop\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=103644278&keywords=scrum%20master&location=United%20States")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys("grangerr26@gmail.com")

password_field = driver.find_element_by_id("password")
password_field.send_keys("Harry1234")
password_field.send_keys(Keys.ENTER)

#Remember_Me = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-primary"]/button')
#Remember_Me.click()
#time.sleep(2)

Message_down = driver.find_element_by_xpath('//*[@id="ember319"]')
Message_down.click()
time.sleep(2)

total_results = driver.find_element_by_class_name("display-flex.t-12.t-black--light.t-normal")
total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
print(total_results_int)
time.sleep(5)

Job_list = driver.find_elements_by_css_selector('.job-card-container--clickable')
for list in Job_list:
    print("called")
    list.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_button.click()
        time.sleep(2)
        phone_number = driver.find_element_by_class_name("fb-single-line-text__input")
        phone_number.send_keys("9095056060")
        next_button = driver.find_element_by_css_selector("footer button")
        if next_button.get_attribute("data-control-name") == "continue_unify":
            next_button.click()
        else:
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_xpath("//button[contains(@class, 'artdeco-button')]//*[contains(., 'Discard')]/..")
            discard_button.click()
            print("complex application, skipped....")
            continue

        time.sleep(2)
        review_button = driver.find_element_by_class_name("artdeco-button--primary")
        if review_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_xpath("//button[contains(@class, 'artdeco-button')]//*[contains(., 'Discard')]/..")
            discard_button.click()
            print("complex application, skipped....")
            continue
        else:
            review_button.click()
            time.sleep(2)
            submit_button = driver.find_element_by_class_name("artdeco-button--primary")
            if submit_button.get_attribute("data-control-name") == "submit_unify":
                submit_button.click()
                time.sleep(2)
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
            else:
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("complex application, skipped....")
                continue
    except NoSuchElementException:
        print("No application button, skipped.")
        continue        

























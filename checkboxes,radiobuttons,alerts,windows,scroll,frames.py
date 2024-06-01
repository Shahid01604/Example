import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Url
url = "https://rahulshettyacademy.com/AutomationPractice/"

# Locators
radio_button_xpath = '//input[@class="radioButton" and @value="radio1"]'
common_value_of_checkboxes_xpath = '//input[@type="checkbox"]'
alert_search_box_xpath = '//input[@id="name"]'
alert_button_xpath = '//input[@id="alertbtn"]'
another_alert_button_xpath = '//input[@id="confirmbtn"]'
open_window_button_xpath = '//button[@id="openwindow"]'
open_tab_xpath = '//a[@id="opentab"]'
frame_ID = "courses-iframe"
scroll_element_xpath = '//button[@id="mousehover"]'

# Automation Code
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH, radio_button_xpath).click()
check_boxes = driver.find_elements(By.XPATH, common_value_of_checkboxes_xpath)

for check in check_boxes:
    if not check.is_selected():
        check_boxes[0].click()
        check_boxes[1].click()
        break

driver.find_element(By.XPATH, alert_search_box_xpath).send_keys("example")
driver.find_element(By.XPATH, alert_button_xpath).click()
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()
driver.find_element(By.XPATH, another_alert_button_xpath).click()
another_alert = driver.switch_to.alert
time.sleep(2)
another_alert.dismiss()
driver.find_element(By.XPATH, open_window_button_xpath).click()
windows = driver.window_handles
window1 = windows[0]
window2 = windows[1]
driver.switch_to.window(window1)
driver.find_element(By.XPATH, open_tab_xpath).click()
windows_tab = driver.window_handles
tab1 = windows_tab[0]
tab2 = windows_tab[1]
driver.switch_to.window(tab1)
scroll_element = driver.find_element(By.XPATH, scroll_element_xpath)
driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
driver.switch_to.frame(frame_ID)
time.sleep(3)
driver.switch_to.default_content()
time.sleep(2)
driver.quit()
print("Test Passed")


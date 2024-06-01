import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://tutorialsninja.com/demo/index.php?route=common/home"
lap_hover_xpath = '//a[@class="dropdown-toggle" and text() = "Laptops & Notebooks"]'
mac_click_Xpath = '//a[text() ="Macs (0)"]'
search_bar_xpath = '//input[@class="form-control input-lg"]'
search_bar_click_xpath = '//button[@class="btn btn-default btn-lg"]'
drop_down_xpath = '//select[@class="form-control"]'
drop_search_xpath = '//input[@id="button-search"]'

driver.get(url)
driver.maximize_window()
act = ActionChains(driver)
lap = driver.find_element(By.XPATH, lap_hover_xpath)
act.move_to_element(lap).perform()
driver.find_element(By.XPATH, mac_click_Xpath).click()
driver.find_element(By.XPATH, search_bar_xpath).send_keys("Example")
click = driver.find_element(By.XPATH, search_bar_click_xpath)
click.send_keys(Keys.ENTER)
drop = Select(driver.find_element(By.XPATH, drop_down_xpath))
drop.select_by_value("26")
driver.find_element(By.XPATH, drop_search_xpath).click()
time.sleep(4)
driver.close()
print("Test Passed")

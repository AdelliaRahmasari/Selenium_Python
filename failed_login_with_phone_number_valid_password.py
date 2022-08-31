from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(5) #delay 5 detik

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('088823772363')
time.sleep(1)
driver.find_element_by_id("password").send_keys('sman60jakarta')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
time.sleep(2)

respon_error_email = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").get_attribute("validationMessage")

assert "Please include an '@' in the email address. '088823772363' is missing an '@'."== respon_error_email

driver.close()
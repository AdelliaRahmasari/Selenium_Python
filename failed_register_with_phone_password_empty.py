from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(5) #delay 5 detik

driver.find_element_by_id("signUp").click() #tombol sign up disebelah kanan
time.sleep(2)
driver.find_element_by_id("email_register").send_keys('0138127391263') #row email
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]').click() #tombol signup untuk daftar
time.sleep(2)

error_email = driver.find_element_by_id("email_register").get_attribute("validationMessage")

assert "Please include an '@' in the email address. '0138127391263' is missing an '@'."== error_email

driver.close()
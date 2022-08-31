from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(5) #delay 5 detik

driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('coba.coba@yahoo.com')
time.sleep(1)
driver.find_element_by_id("password").send_keys('sman60jakarta')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
time.sleep(2)

respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

assert respon_welcome== "User's not found"
assert respon_berhasil== 'Email atau Password Anda Salah'

driver.close()
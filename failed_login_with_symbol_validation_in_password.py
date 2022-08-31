from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install()) #deklarasi library chrome
driver.get('https://barru.pythonanywhere.com/daftar') #url web yang dituju
time.sleep(5) #delay 5 detik

driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@gmail.com')
time.sleep(1)
driver.find_element_by_id("password").send_keys("SELECT%count%(*)%FROM%Users%WHERE%Username='jebol'%or%1=1%--%'%AND%Password=%'email")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
time.sleep(2)

respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
respon_gagal = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

assert respon_welcome== "Password tidak valid"
assert respon_gagal== 'Tidak boleh mengandung symbol'

driver.close()
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(chrome_options = options, executable_path = 'chromedriver')
driver.get('http://codepad.org')

# click radio button

python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
# python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button.click()

# type text

text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print('Hello World')")
# text_area.send_keys("print('Hello World')")

# click submit button

submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
submit_button.click() 
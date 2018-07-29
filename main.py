from selenium import webdriver

login_url = "https://academia.srmuniv.ac.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&serviceurl=https://academia.srmuniv.ac.in/&service_language=en"
after_login = "https://academia.srmuniv.ac.in/#View:My_Attendance"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')

driver = webdriver.Chrome(chrome_options = options, executable_path = 'chromedriver')
driver.get(login_url)

# Typing the details

username = input("Enter your username: ")
usertext = driver.find_element_by_xpath("//input[@name = 'username']")
usertext.send_keys(username)
password = input("Enter your password: ")
passtext = driver.find_element_by_xpath("//input[@name = 'password']")
passtext.send_keys(password)

# Submitting the form

submit_button = driver.find_element_by_xpath("//input[@value = 'Sign In']")
submit_button.submit()

# Go to attendance

driver.get(after_login)
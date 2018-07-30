from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import yaml

login_url = "https://academia.srmuniv.ac.in/"
after_login = "https://academia.srmuniv.ac.in/#View:My_Attendance"
subject_list = []
attendance_list = []
hours_conducted = []
hours_absent = []

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
# options.add_argument('headless')

driver = webdriver.Chrome(chrome_options = options, executable_path = 'chromedriver')
driver.get(login_url)
driver.switch_to_frame("zohoiam")

with open("login.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print("################### Academia Scrapper ###################")

# Typing the details

usertext = driver.find_element_by_xpath("//input[@name = 'username']")
usertext.send_keys(cfg['login']['username'])
passtext = driver.find_element_by_xpath("//input[@name = 'password']")
passtext.send_keys(cfg['login']['password'])

# Submitting the form

submit_button = driver.find_element_by_xpath("//input[@value = 'Sign In']")
submit_button.submit()

# Go to attendance

time.sleep(6)
print("Logged in!")
driver.get(after_login)
time.sleep(3)

# Getting data

for i in range(2,12):
	sub = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[2]")
	att = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[9]")
	hc = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[7]")
	ha = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[8]")
	subject_list.append(sub.text)
	attendance_list.append(att.text)
	hours_conducted.append(hc.text)
	hours_absent.append(ha.text)

for i in range(10):
	print(str(i+1) + ". " + str(subject_list[i]) + " - " + str(attendance_list[i]) + "%")
ch = input("Select a subject: ")
perc = (1 - (int(hours_absent[ch-1])/int(hours_conducted[ch-1])))*100
if perc<75:
	print("Your attendance is below 75%")
	noc = 0
	while perc<75:
		noc+=1
		perc = (1 - ((int(hours_absent[ch-1])+noc) / (int(hours_conducted[ch-1])+noc)))*100
	print("No. of classes to attend to get 75%: "+noc)

# print("Your attendance is below 75%")
# noc = 0
# perc = (12/20)*100
# print("The percentage is: " + str(perc))
# while perc<75:
# 	noc+=1
# 	print(noc)
# 	perc = ((12+noc)/(20+noc))*100
# 	print(str(perc)+"%")
# 	print("No. of classes to attend: "+str(noc))

# print("\nNo. of classes you can safely bunk:\n")

# for i in range(10):
# 	perc = (1 - (int(hours_absent[i])/int(hours_conducted[i])))*100
# 	# print(perc)
# 	while perc>=75:



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import yaml
import sys

login_url = "https://academia.srmuniv.ac.in/"
after_login = "https://academia.srmuniv.ac.in/#View:My_Attendance"
subject_list = []
attendance_list = []
hours_conducted = []
hours_absent = []
types = []

print("################### Academia Scraper ###################")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
# options.add_argument('headless')

driver = webdriver.Chrome(chrome_options = options, executable_path = "D:\\Documents\\GitHub\\academia_scraper\\chromedriver.exe")
driver.get(login_url)
driver.switch_to_frame("zohoiam")

with open("login.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

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
driver.get(after_login)
time.sleep(8)

# Getting data

for i in range(2,11):
	sub = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[2]")
	att = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[9]")
	hc = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[7]")
	ha = driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[8]")
	subject_list.append(sub.text)
	attendance_list.append(att.text)
	hours_conducted.append(hc.text)
	hours_absent.append(ha.text)
	types.append(driver.find_element_by_xpath("//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div[1]/table[2]/tbody/tr["+str(i)+"]/td[3]").text)

# Show subjects

flag = 0
while flag!=1:
	for i in range(9):
		print(str(i+1) + ". " + str(subject_list[i]) + " - " + types[i] + " - " + str(attendance_list[i]) + "%")
	print("10. Exit")	
	ch = int(input("Select an option: "))
	
	if ch==11:
		flag=1
		driver.close()
		sys.exit("Goodbye!")
	
	else:
		perc = (1 - (int(hours_absent[ch-1])/int(hours_conducted[ch-1])))*100
		if perc<75:
			p = perc
			print("Your attendance is below 75%")
			nocn = 0
			while p<75:
				nocn+=1
				p = (1 - ((int(hours_absent[ch-1])+nocn) / (int(hours_conducted[ch-1])+nocn)))*100
			print("No. of classes to attend to get 75%: "+str(nocn))
		else:
			nocb = 0
			p = perc
			while p>75:
				if ((1 - ((int(hours_absent[ch-1]) + nocb)/ (int(hours_conducted[ch-1])+nocb)))*100) > 75:
					nocb+=1
				p = (1 - ((int(hours_absent[ch-1]) + nocb)/ (int(hours_conducted[ch-1])+nocb)))*100
			print("No. of classes you can safely bunk: "+str(nocb))

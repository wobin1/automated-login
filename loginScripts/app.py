from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://web.facebook.com")

username = driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys('nathanielmusa3@gmail.com')

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('peacedauda')

button = driver.find_element_by_xpath('//*[@id="u_0_d_g5"]')
button.click()



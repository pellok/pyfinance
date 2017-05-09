#Selenium: You’re First Program on Web Automation
#***********************************************
#Load required Selenium library files.
from selenium import webdriver

#invoke the firefox browser
# driver=webdriver.Firefox()
driver=webdriver.Chrome()

#navigate to the given weburl
driver.get("http://www.google.com")

#print the web url of the current page.
print(driver.current_url)

#print title of the web page
print(driver.title)

print("navigating to yahoo.com")
driver.get("http://www.yahoo.com")

print(driver.current_url)
print(driver.title)

print("going back to google.com")

#Navigating to previous web page.
driver.back()

print(driver.current_url)
print(driver.title)

print("going forward to yahoo.com")

#after using driver.back(), driver.forward() helps to navigate to latest web page.
driver.forward()

print(driver.current_url)
print(driver.title)

driver.refresh()
driver.maximize_window()

driver.close()
# driver.quit()
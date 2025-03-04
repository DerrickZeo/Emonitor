from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")
assert "Energy Dashboard" in driver.title
driver.quit()

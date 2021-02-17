from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# opts = Options()
# opts.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=opts, executable_path=path)
driver = webdriver.Chrome(executable_path="chromedriver.exe")
url="http://www.python.org"
driver.get(url)
page_title = driver.title
page_title
driver.get('http://www.google.com')
driver.page_source\
textbox = driver.find_element_by_id("id-search-field")
textbox.send_keys("Python")
textbox.clear()
textbox = driver.find_element_by_class_name("search-field")
textbox.send_keys("Python")
textbox = driver.find_element_by_xpath('//*[@id="id-search-field"]')
textbox.clear()
textbox.send_keys("Python")\
btn = driver.find_element_by_id('submit')
btn.click()
driver.page_source
driver.execute_script("window.history.go(-1)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("http://www.google.com")
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Public Login')]")))
driver.close()

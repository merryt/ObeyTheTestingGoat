from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'.\geckodriver.exe')
browser.get('http://localhost:8000')
browser.close()

assert 'Django' in browser.title

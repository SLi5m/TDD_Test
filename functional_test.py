from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/mnt/c/Users/NUMIDA/SLi5m/TDD/geckodriver', options=options)

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')
   
assert 'The install' in browser.title

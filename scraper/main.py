import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='./111/chromedriver.exe', options=chrome_options)
driver.get('https://www.amazon.com/Hoover-WindTunnel-Whole-House-Rewind/dp/B094YRDNTC/ref=sr_1_2_sspa?crid=18Y1EYLFX0VHS&keywords=hoover&qid=1679600473&sprefix=hoove%2Caps%2C207&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzT1FESkpYWUZTV1hNJmVuY3J5cHRlZElkPUEwNDQ0NjUxM1RJTkxZRUI5MVFMMCZlbmNyeXB0ZWRBZElkPUEwODM5NDg2MThVNVgwOUQwMERRWSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1')

content = driver.page_source
soup = BeautifulSoup(content)

results = []

#print(soup.contents)
driver.quit()

for element in soup.findAll(attrs={'id':'productTitle'}):
    print(element.text)
    results.append(element.text)


text_file = open("sample.html", "w")
text_file.write('\n'.join(results))
text_file.close()
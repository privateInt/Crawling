from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('created '+directory)
    except OSError:
        print('Error : already Created' + directory)

search = input('검색할 단어를 입력하세요: ')
createFolder('data/'+search)

driver = webdriver.Chrome("C:\Imageclassification\chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

for i in range(500):
    driver.execute_script("window.scrollBy(0,50000)")
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")
img = soup.select('img')

n = -3
imgurl = []

for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

for i in imgurl:
    urlretrieve(i, "data/"+ search +'/' + search + str(n) + ".jpg")
    n += 1
    print('downloading.........{}'.format(n))

driver.close()

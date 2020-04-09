import os
import requests
import shutil
import time
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup

baseURL = "https://www.google.com/search?tbm=isch&biw=1536&bih=722&ei=7JaAXsX1MYvUUebfvPgH&q="
query = "coding memes jpg"
url = baseURL + query

driver = webdriver.Chrome()
driver.get(url)

html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll('img')))
images = []
for image in sel_soup.findAll('img'):
    #print(image)
    try:
        src = image["src"]
    except:
        src = image["data-src"]
    images.append(src)

print(len(images))
currentPath = os.getcwd()
j = 0
for image in images:
    #print(image)
    fileName = os.path.basename(str(j)+".jpg")
    #print(fileName)
    filePath = os.path.join(currentPath, "images", fileName)
    #print(filePath)
    #print(image)
    try:
        imageRequest = requests.get(image, stream=True)
        with open(filePath, "wb") as outputFile:
            shutil.copyfileobj(imageRequest.raw, outputFile)
            print("Done")
        del imageRequest
        j += 1
    except:
        '''
        driver2 = webdriver.Chrome()
        driver2.get(image)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.typewrite(str(j) + '.html')
        pyautogui.hotkey('enter')
        driver2.close()
        j += 1
        '''
        pass
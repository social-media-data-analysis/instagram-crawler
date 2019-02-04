from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def createDriver(chromeDriverPath, targetUrl):
    options = Options()
    #head less mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    #for head less mode detection
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # agent change 
    options.add_argument("lang=ko_KR") 

    # driver setting
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromeDriverPath)
    driver.get(targetUrl)

    # for head less mode detection
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #num of plugin spoofing
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    return driver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")

    time.sleep(3)

    a: [WebElement] = driver.find_elements(By.TAG_NAME, "a")
    link : WebElement
    for link in a:
        print(link.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

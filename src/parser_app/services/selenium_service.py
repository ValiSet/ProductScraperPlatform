from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def parse_url(url):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(2)
        headers = driver.find_elements(By.TAG_NAME, 'h1')

        result = '\n'.join([header.text for header in headers])
        return result

    except Exception as e:
        return str(e)

    finally:
        driver.quit()
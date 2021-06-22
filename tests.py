from selenium import webdriver
from selenium.common import exceptions
import time
import requests
from bs4 import BeautifulSoup
import json
from email_generator import email_generator
from response_writer import write_response


def test_mail_ru(n):
    responses = []
    while n > 0:
        try:
            driver = webdriver.Chrome()
            driver.get("https://account.mail.ru/")
            time.sleep(2)
            element = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/form/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/input')
            element.send_keys(email_generator())
            element = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/form/div[2]/div/div[3]/div/div[1]/button/span')
            element.click()
            response = requests.get(driver.current_url).text
            soup = BeautifulSoup(response, 'lxml')
            soup = soup.find("script", id="state").contents
            for i in soup:
                responses.append(json.loads(i.strip()))
            driver.close()
            n -= 1
            print(f'Осталось {n} ящиков')
        except Exception:
            if exceptions:
                continue
            else:
                break
    write_response(responses)

if __name__ == "__main__":
    n_boxes = 100
    test_mail_ru(n_boxes)

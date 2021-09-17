import time
import re
from yandex import login_, password_

from selenium import webdriver


def correct_login(login_=login_):
    return len(re.findall(r"\w[\w\d_]+@.*", login_)) == 1


def selenium_login(login_=login_, password_=password_):
    if correct_login(login_):
        result = dict()
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        time.sleep(1)
        elem = driver.find_element_by_name('login')
        elem.send_keys(login_)
        elem.send_keys(webdriver.common.keys.Keys.ENTER)
        time.sleep(3)
        result['login'] = driver.current_url
        elem = driver.find_element_by_name('passwd')
        elem.send_keys(password_)
        elem.send_keys(webdriver.common.keys.Keys.ENTER)
        time.sleep(1)
        result['password'] = driver.current_url
        driver.close()
        driver.quit()
        return result


if __name__ == '__main__':
    pass

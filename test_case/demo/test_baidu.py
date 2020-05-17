# -*- coding:utf-8 -*-

from time import sleep

import allure


def test_baidu(driver):

    driver.get('http://www.baidu.com')
    sleep(2)
    driver.send_keys("//*[@id='kw']",'手机')
    sleep(2)



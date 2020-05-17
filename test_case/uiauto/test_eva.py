from time import sleep

import allure


def test_eva_guofu(driver):

    #打开官网
    driver.get('http://115.159.54.253:3002/eva')
    sleep(2)
    #点击登录
    driver.click("xpath=>//div[@class='btn btn-login']")
    sleep(2)
    #输入用户名
    driver.send_keys("xpath=>//input[1]",'15035090142')
    sleep(2)
    #输入密码
    driver.send_keys("xpath=>//input[2]",'123456')
    sleep(2)
    #点击登录
    driver.click("xpath=>//div[@class='modal-login-btn-login'] ")
    sleep(10)
    #点击确定
    driver.click("xpath=>//div[@class='modal-login-btn-confirm']")
    sleep(2)
    #点击礼物
    driver.click("xpath=>//div[@class='gift-zone']")
    sleep(2)








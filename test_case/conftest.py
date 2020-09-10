#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from tools.ui.base_ui import BaseUI
import  platform

@pytest.fixture(scope='session')
def driver():
    base = BaseUI()
    if platform.system() == "Windows":
        base.start_browser('chrome')
        print('Window环境运行chrome浏览器驱动')
    else:       # 无头浏览器 在Linux下
        base.start_browser('chrome_headless')
        print('linux环境运行chrome_headless浏览器驱动')

    yield base
    base.driver.quit()






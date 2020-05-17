# -*- coding:utf-8 -*-

import pytest
from tools.ui.base_ui import BaseUI

@pytest.fixture(scope='session')
def driver():
    base = BaseUI()
    base.start_browser("chrome")

    yield base
    base.driver.quit()






from datetime import datetime
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import yaml  # PyYaml

from src.TestCase import TestCase


class TestTimemeter:
    # 获取app的package: adb shell dumpsys window | grep mCurrent
    # 获取app的launcher activity: adb shell monkey -p {appPackage} -vvv 1
    # $ANDROID_HOME 配置了吗？appium运行会调用这个。

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "7XBRX19118002370"
        caps["appPackage"] = "com.liulishuo.engzo"
        caps["appActivity"] = ".app.activity.PrepositionPrivacyActivity"
        # caps["autoGrantPermissions"] = "true"  # 自动赋予 App 权限
        caps["noReset"] = "true"
        # caps["unicodeKeyboard"] = "true"  # 输入中文
        # caps["ignoreUnimportantViews"] = "true"  # 忽略不重要的 View 提升运行速度

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    # 数据驱动
    def test_liulishuo_from_testcase(self):
        TestCase("tc_liulishuo.yaml").run(self.driver)


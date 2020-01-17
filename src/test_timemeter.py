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

    # 参数化读取文件
    search_data = yaml.safe_load(open("search.yaml", "r"))
    print(search_data)

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "7XBRX19118002370"
        caps["appPackage"] = "cc.imzbb.timemeter"
        caps["appActivity"] = "cc.imzbb.timemeter.MainActivity"
        # caps["autoGrantPermissions"] = "true"  # 自动赋予 App 权限
        # caps["noReset"] = "false"
        # caps["unicodeKeyboard"] = "true"  # 输入中文
        # caps["ignoreUnimportantViews"] = "true"  # 忽略不重要的 View 提升运行速度

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    # 参数化设计
    @pytest.mark.parametrize("package", [
        ("hello"),
        ("world"),
        ("你好")  # 使用元祖可以变动的值
    ])
    def test_gallary(self, package):
        # accessibility_id = content_desc
        el1 = self.driver.find_element_by_accessibility_id("打开抽屉式导航栏")
        el1.click()
        el2 = self.driver.find_elements_by_id("cc.imzbb.timemeter:id/design_menu_item_text")[1]
        el2.click()
        el3 = self.driver.find_element_by_id("android:id/search_button")
        el3.click()
        el4 = self.driver.find_element_by_id("android:id/search_src_text")
        el4.send_keys(package)
        sleep(1)

    # 参数化设计（导入文档）
    @pytest.mark.parametrize("package", search_data)
    def test_gallary2(self, package):
        # accessibility_id = content_desc
        el1 = self.driver.find_element_by_accessibility_id("打开抽屉式导航栏")
        el1.click()
        el2 = self.driver.find_elements_by_id("cc.imzbb.timemeter:id/design_menu_item_text")[1]
        el2.click()
        el3 = self.driver.find_element_by_id("android:id/search_button")
        el3.click()
        el4 = self.driver.find_element_by_id("android:id/search_src_text")
        el4.send_keys(package)
        sleep(1)

    # 数据驱动
    def test_gallary_from_testcase(self):
        TestCase("tc_timemeter.yaml").run(self.driver)

    def test_webview(self):
        el1 = self.driver.find_element_by_accessibility_id("打开抽屉式导航栏")
        el1.click()
        # el2 = self.driver.find_elements_by_id("cc.imzbb.timemeter:id/design_menu_item_text")[4]
        el2 = self.driver.find_element_by_xpath("//*[@text='Share']")
        el2.click()
        for i in range(5):
            print(self.driver.contexts)
        el3 = self.driver.find_element_by_xpath("//*[@text='Github']")
        el3.click()
        sleep(5)


    def test_timemeter(self):
        el1 = self.driver.find_element_by_id("cc.imzbb.timemeter:id/fab")
        el1.click()

        # sleep(10)  # 时间消耗太大，不建议使用
        # if len(self.driver.find_elements_by_id("cc.imzbb.timemeter:id/snackbar_action")) >= 1:
        #     self.driver.find_element_by_id("cc.imzbb.timemeter:id/snackbar_action").click()

        # 第一种显示等待
        # WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.find_elements_by_id("cc.imzbb.timemeter:id/snackbar_action")) >= 1)
        # self.driver.find_element_by_id("cc.imzbb.timemeter:id/snackbar_action").click()
        # sleep(10)

        # 第二种显示等待
        # WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located((By.ID, "cc.imzbb.timemeter:id/snackbar_action")))
        # self.driver.find_element_by_id("cc.imzbb.timemeter:id/snackbar_action").click()
        # sleep(10)

        # 第三种显示等待
        def loaded(drive):
            print(datetime.now())
            if len(self.driver.find_elements_by_id("cc.imzbb.timemeter:id/snackbar_action")) >= 1:
                self.driver.find_element_by_id("cc.imzbb.timemeter:id/snackbar_action").click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 15).until(loaded)
        except:
            print("no update")

    def teardown(self):
        # pass
        self.driver.quit()

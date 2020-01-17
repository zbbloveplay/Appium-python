import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCase:
    def __init__(self, path):
        file = open(path, "r")
        self.steps = yaml.safe_load(file)

    def run(self, driver: WebDriver):
        for step in self.steps:
            if isinstance(step, dict):
                # 先看看有没有好找
                if "order" in step.keys():
                    if "id" in step.keys():
                        element = driver.find_elements_by_id(step["id"])[step["order"]]
                elif "wait" in step.keys():
                    WebDriverWait(driver, step["wait"]).until(expected_conditions.visibility_of_element_located(
                        (By.ID, step["id"])))
                    element = driver.find_element_by_id(step["id"])

                # 如果没什么幺蛾子就直接找对象
                elif "id" in step.keys():
                    element = driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step["xpath"])
                elif "content_desc" in step.keys():
                    element = driver.find_element_by_accessibility_id(step["content_desc"])
                elif "text" in step.keys():
                    xpath = '%s%s%s'%("//*[@text='", step["text"], "']")
                    element =driver.find_element_by_xpath(xpath)
                else:
                    print(step.keys())

                # 然后对对象进行操作
                if "input" in step.keys():
                    element.send_keys(step["input"])
                else:
                    element.click()

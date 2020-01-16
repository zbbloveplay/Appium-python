from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestApiDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "8.1.0"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_gsm_call(self):
        self.driver.send_sms('555-123-4567', 'Hello, zbb')
        # self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data("io.appium.android.apis", p, 5))
            except:
                pass

    def teardown(self):
        # pass
        self.driver.quit()

# 打开小小优酷这个app
from appium import webdriver
import time
import pytest
@pytest.fixture(scope="class")
def lian():
    d={
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "emulator-5554",
      "appPackage": "com.youkuchild.android",
      "appActivity": ".ChildNewHomeActivity",
      "noReset": "true"
    }
    dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=d)
    time.sleep(10)
    return dr
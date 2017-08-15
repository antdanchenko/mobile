import pytest
from sauceclient import SauceClient
from tests import *
from os import environ
from appium import webdriver
from abc import ABCMeta, \
    abstractmethod
import hmac
from hashlib import md5


class AbstractTestCase:

    __metaclass__ = ABCMeta


    @property
    def sauce_access_key(self):
        return environ.get('SAUCE_ACCESS_KEY')

    @property
    def sauce_username(self):
        return environ.get('SAUCE_USERNAME')

    @property
    def executor_sauce_lab(self):
        return 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (self.sauce_username, self.sauce_access_key)

    @property
    def capabilities_sauce_lab(self):

        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['appiumVersion'] = '1.6.5'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android GoogleAPI Emulator'
        desired_caps['app'] = pytest.config.getoption('apk')
        desired_caps['browserName'] = ''
        desired_caps['deviceOrientation'] = "portrait"
        desired_caps['name'] = tests_data.name
        desired_caps['build'] = pytest.config.getoption('build')
        desired_caps['idleTimeout'] = 300
        return desired_caps

    @property
    def token(self):
        return hmac.new(bytes(self.sauce_username + ":" + self.sauce_access_key, 'latin-1'),
                        bytes(self.driver.session_id, 'latin-1'), md5).hexdigest()

    def update_sauce_lab_result(self):
        SauceClient(self.sauce_username,
                    self.sauce_access_key).jobs.update_job(self.driver.session_id, passed=tests_data.result,
                                                           public=self.token)

    @property
    def public_url(self):
        return "https://saucelabs.com/jobs/%s?auth=%s" % (self.driver.session_id, self.token)


    @property
    def executor_local(self):
        return 'http://localhost:4723/wd/hub'

    @property
    def capabilities_local(self):
        desired_caps = dict()
        desired_caps['deviceName'] = 'takoe'
        desired_caps['platformName'] = 'Android'
        desired_caps['appiumVersion'] = '1.6.5'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['app'] = pytest.config.getoption('apk')
        return desired_caps

    @abstractmethod
    def setup_method(self, method):
        raise NotImplementedError('Should be overridden from a child class')

    @abstractmethod
    def teardown_method(self, method):
        raise NotImplementedError('Should be overridden from a child class')


def create_session(executor, desired_caps):
    return webdriver.Remote(executor, desired_caps)


class SingleDeviceTestCase(AbstractTestCase):

    def setup_method(self, method):
        self.driver = create_session(self.executor_sauce_lab, self.capabilities_sauce_lab)
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()
        self.update_sauce_lab_result()


class MultiplyDeviceTestCase(AbstractTestCase):

    def setup_method(self, method):

        loop = asyncio.get_event_loop()
        self.driver_1, self.driver_2 = loop.run_until_complete(start_threads(2, create_session, self.executor_sauce_lab,
                                                                             self.capabilities_sauce_lab))
        loop.close()

    def teardown_method(self, method):
        for driver in self.driver_1, self.driver_2:
            self.driver = driver
            self.driver.quit()
            self.update_sauce_lab_result()

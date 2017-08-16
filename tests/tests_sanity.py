import pytest
from tests.basetestcase import SingleDeviceTestCase
from views.home import HomeView


class TestSanity(SingleDeviceTestCase):

    @pytest.mark.parametrize('verification, text', [
        ("short", "Password should be not less then 6 symbols."),
        ("mismatch", "Password confirmation doesn\'t match password."),
        ("valid", "Tap here to enter your phone number & I\'ll find your friends")
                                                      ])
    def test_password(self, verification, text):

        pytest.allure.dynamic_issue(self.get_public_url(self.driver))
        passwords = {"short": "qwe1",
                     'mismatch': 'mismatch1234',
                     'valid': 'qwerty1234'}

        home = HomeView(self.driver)
        home.request_password_icon.click()
        home.type_message_edit_box.send_keys(passwords[verification])
        home.confirm()
        if 'short' not in verification:
            home.type_message_edit_box.send_keys(passwords['valid'])
            home.confirm()
        home.find_text(text)

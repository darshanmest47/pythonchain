import time

import pytest

from hubspot.POM.Username import Username
from hubspot.testdata.Basetest import Basetest
from hubspot.testdata.Testdata import Testdata


class Testlogin(Basetest):

    def test_verifytitle(self):
        user = Username(self.driver)

        title = user.get_title_name()
        print(title)
        assert title == Testdata.title

    def test_needhelpdisp(self):
        user = Username(self.driver)

        user_link = user.need_help_disp()
        print(user_link)
        assert user_link == Testdata.need_help

    def test_buttondisp(self):
        user = Username(self.driver)

        print(user.button_displayed())

        assert user.button_displayed()

    @pytest.mark.negative
    def test_negative(self):
        user = Username(self.driver)
        user.cont_click()
        time.sleep(2)
        warn_text = user.warning_present()
        print(warn_text)
        print(Testdata.warning_msg)
        assert warn_text == Testdata.warning_msg

    def test_submit(self):
        user = Username(self.driver)
        user.eneter_Username(Testdata.username)

        pass_obj=user.cont_click()
        return pass_obj

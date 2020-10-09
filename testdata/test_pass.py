from hubspot.POM.Username import Username
from hubspot.testdata.Basetest import Basetest
from hubspot.testdata.Testdata import Testdata

from hubspot.testdata.test_login import Testlogin


class Testpass(Basetest):

    def test_email_veri(self):
        user=Username(self.driver)
        user.eneter_Username(Testdata.username)
        pass1=user.cont_click()
        p_txt = pass1.email_verify()
        print(p_txt)
        assert p_txt == Testdata.username
        # tl = Testlogin()
        # pass1 = tl.test_submit()




    def test_forgot_pass(self):
        user = Username(self.driver)
        user.eneter_Username(Testdata.username)
        pass1 = user.cont_click()
        f_txt= pass1.forgot_passtext()
        print(f_txt)
        # assert f_txt == Testdata.forgot_pass

    # def test_chkboxchk(self):
    #     user = Username(self.driver)
    #     user.eneter_Username(Testdata.username)
    #     pass1 = user.cont_click()
    #
    #     pass1.checkbox_chk()

    def test_warnverify(self):
        user = Username(self.driver)
        user.eneter_Username(Testdata.username)
        pass1 = user.cont_click()

        warn_txt = pass1.warn_verify()
        print(warn_txt)

        # assert warn_txt == Testdata.pass_warn

    def test_enterpass(self):
        user = Username(self.driver)
        user.eneter_Username(Testdata.username)
        pass1 = user.cont_click()

        pass1.password_enter(Testdata.password)
        pass1.click_sub()



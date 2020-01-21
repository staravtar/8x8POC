from assertionsClass import Assertions
from baseClass import SeleniumWebdriverBase
from testdata import TestData as td


class TestPage(Assertions):

    def login(self):
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(10)
        self.isElementPresentByXPATH(td.start_button_xpath)
        self.teardown()

    def join_call(self):
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(10)
        self.clickElementByXPATH(td.join_button_xpath)
        self.pause(10)
        self.isElementPresentByXPATH(td.large_video_xpath)
        self.teardown()

    def delete_calender_sync(self):
        self.clickElementByXPATH(td.setting_btn_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.calender_and_schedule_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.delete_mail_xpath)
        self.pause(2)

    def open_url(self, url="https://calendar.google.com/calendar"):
        self.openURL(url=url)

    def calender_sync(self):
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name_1, td.Email_box_xpath)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(10)
        self.clickElementByXPATH(td.sync_calender_xpath)
        self.pause(4)
        self.switch_to_window(1)
        self.clickElementByXPATH(td.google_xpath)
        self.pause(4)
        self.clickElementByXPATH(td.terms_checkbox_xpath)
        self.clickElementByXPATH(td.link_google_acc_xpath)
        self.pause(6)
        self.typeTextByXPath(td.user_name_1, td.gmail_email_input_xpath)
        self.clickElementByXPATH(td.gmail_email_next_xpath)
        self.pause(3)
        self.typeTextByXPath(td.password, td.gmail_pwd_xpath)
        self.clickElementByXPATH(td.gmail_pwd_next_xpath)
        self.pause(4)
        self.clickElementByXPATH(td.gmail_allow_xpath)
        self.pause(5)
        self.clickElementByXPATH(td.gmail_accept_xpath)
        self.pause(5)
        self.switch_to_window(0)
        self.pause(2)
        self.isElementPresentByXPATH(td.no_schedule_event_xpath)
        self.open_new_tab()
        self.switch_to_window(1)
        self.open_url()
        self.pause(6)
        self.clickElementByXPATH(td.create_btn_xpath)
        self.pause(4)
        #self.driver.find_element_by_xpath(td.add_title_xpath).send_keys('abc')
        self.typeTextByXPath(td.meeting_title, td.add_title_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.save_button)
        self.pause(2)
        self.switch_to_window(0)
        self.pause(2)
        self.refresh()
        self.pause(5)
        self.isElementPresentByXPATH(td.meeting_title_homepage_xpath)
        self.pause(2)
        self.delete_calender_sync()
        self.teardown()



from assertionsClass import Assertions
from baseClass import SeleniumWebdriverBase
from testdata import TestData as td
import win32com.shell.shell as shell
from time import sleep

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
        """This will join the call from available meeting"""
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(10)
        self.clickElementByXPATH(td.join_button_xpath)
        self.pause(15)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(2)
        is_large_video = self.isElementPresentByXPATH(td.large_video_xpath)
        assert True == is_large_video
        self.teardown()

    def delete_calender_sync(self):
        self.switch_to_window(0)
        self.pause(1)
        self.clickElementByLocator(td.setting_btn_css)
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
        self.typeTextByXPath(td.user_name, td.gmail_email_input_xpath)
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
        is_event_present = self.isElementPresentByXPATH(td.no_schedule_event_xpath)
        self.open_new_tab()
        self.switch_to_window(1)
        self.open_url()
        self.pause(6)
        self.clickElementByXPATH(td.create_btn_xpath)
        self.pause(4)
        self.typeTextByXPath(td.meeting_title, td.add_title_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.save_button)
        self.pause(2)
        self.switch_to_window(0)
        self.pause(2)
        self.refresh()
        self.pause(6)
        is_title_present = self.isElementPresentByXPATH(td.meeting_title_homepage_xpath)
        self.pause(8)
        self.clickElementByXPATH(td.join_button_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.join_button_xpath)
        self.pause(15)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(2)
        is_large_video = self.isElementPresentByXPATH(td.large_video_xpath)
        self.pause(2)
        assert True == is_large_video
        assert True == is_event_present
        # assert True == is_title_present
        self.delete_calender_sync()
        self.teardown()

    def get_connection_info(self):
        """This function will get the connection info and save the values"""
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.pause(2)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(8)
        self.clickElementByXPATH(td.start_button_xpath)
        self.pause(15)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(2)
        self.clickElementByXPATH(td.my_call_box_xpath)
        self.pause(3)
        self.clickElementByXPATH(td.states_icon_xpath)
        self.pause(2)
        connection_level = self.getElementTextByXpath(td.connection_xpath)
        self.pause(1)
        bitrate = self.getElementTextByXpath(td.bitrate_xpath)
        self.pause(1)
        packet_loss = self.getElementTextByXpath(td.packet_loss_xpath)
        self.pause(1)
        resolution = self.getElementTextByXpath(td.resolution_xpath)
        self.pause(1)
        frame_rate = self.getElementTextByXpath(td.frame_rate_xpath)
        self.pause(1)
        return connection_level, bitrate, packet_loss, resolution, frame_rate

    def fetch_webrtc_data(self):
        '''As a pre requisite only use a meeting link in which more than 1 person is already available'''
        meetingurl = self.read_data_fromfile("TestDataSection", "meeting_url")
        print(meetingurl)
        self.open_custom_uri(meetingurl)
        self.pause(10)
        self.typeTextByXPath(self.read_data_fromfile("TestDataSection", "joynee_name"),
                             td.enter_name_meeting_joining_xpath)
        self.clickElementByXPATH(td.button_to_setName)
        self.pause(5)
        self.open_new_tab()
        self.switch_to_window(1)
        self.pause(3)
        self.openURL(td.webrtc_url)
        self.pause(5)
        self.clickElementByXPATH(td.audiosourcehead)
        self.pause(2)
        audLEVEL = self.get_element_text_byindex_xpath(td.tab_audio_level, 0)
        print(audLEVEL)
        self.update_data_in_testdatafile("TestDataSection", "AUDIOLEVEL", audLEVEL)
        self.pause(2)
        self.clickElementByXPATH(td.videosourcehead)
        self.pause(2)
        vdoheight = self.get_element_text_byindex_xpath(td.tab_video_height, 0)
        print(vdoheight)
        self.update_data_in_testdatafile("TestDataSection", "VIDEOHEIGHT", vdoheight)
        vdoweight = self.get_element_text_byindex_xpath(td.tab_video_width, 0)
        print(vdoweight)
        self.update_data_in_testdatafile("TestDataSection", "VIDEOWIDTH", vdoweight)
        self.pause(2)
        self.clickElementByXPATH(td.VideoOutboundhead)
        self.pause(2)
        self.clickElementByXPATH(td.tab_videobytes_persec)
        self.pause(2)
        #self.scroll_down(td.VideoOutboundhead)
        vdobitrate = self.get_element_text_byindex_xpath(td.tab_videobytes_persec_after_off, 0)
        print(vdobitrate)
        self.update_data_in_testdatafile("TestDataSection", "VIDEOBITRATE", vdobitrate)
        self.pause(2)
        self.switch_to_window(0)
        self.teardown()

    def vdo_width_height_webRtc(self):
        """
        Precondition : The user should be on call page and other user should have joined the call
        Function work : This function return AUDIO LEVEL and VIDEO RATE
        """
        self.open_new_tab()
        self.switch_to_window(1)
        self.pause(1)
        self.openURL(td.webrtc_url)
        self.pause(3)
        self.clickElementByXPATH(td.audiosourcehead)
        self.pause(2)
        audLEVEL = self.get_element_text_byindex_xpath(td.tab_audio_level, 0)
        self.pause(2)
        self.clickElementByXPATH(td.VideoOutboundhead)
        #self.scroll_down(td.VideoOutboundhead)
        self.pause(2)

        vdobitrate = self.get_element_text_byindex_xpath(td.tab_videobytes_persec_after_off, 0)
        self.pause(2)
        self.clickElementByXPATH(td.tab_videobytes_persec)
        self.pause(2)
        self.close_window()
        return audLEVEL, vdobitrate

    def get_audio_video_quality(self):
        self.setup()
        self.pause(8)
        connection_level, bitrate, packet_loss, resolution, frame_rate = self.get_connection_info()
        assert str(resolution) != "N/A"
        assert str(frame_rate) != "N/A"
        self.pause(2)
        self.open_new_tab()
        self.switch_to_window(1)
        self.pause(3)
        self.openURL(td.webrtc_url)
        self.pause(5)
        self.clickElementByXPATH(td.vdo_track_sender_xpath)
        vdo_width = self.getElementTextByXpath(td.vdo_farme_width_xpath)
        self.pause(1)
        vdo_height = self.getElementTextByXpath(td.vdo_frame_hight_xpath)
        self.pause(2)
        self.clickElementByXPATH(td.audiosourcehead)
        self.pause(2)
        audLEVEL = self.get_element_text_byindex_xpath(td.tab_audio_level, 0)
        self.pause(2)
        self.clickElementByXPATH(td.VideoOutboundhead)
        self.pause(2)
        self.clickElementByXPATH(td.tab_videobytes_persec)
        self.pause(2)
        vdobitrate = self.get_element_text_byindex_xpath(td.tab_videobytes_persec, 0)
        assert float(audLEVEL) != 0.0
        assert float(vdobitrate) != 0.0
        assert str(resolution).split('x')[0] == vdo_width
        assert str(resolution).split('x')[1] == vdo_height
        self.pause(2)
        self.switch_to_window(0)
        self.pause(2)
        self.teardown()

    def data_from_webRtc(self):
        """
        Precondition : The user should be on call page and other user should have joined the call
        Function work : This function return AUDIO LEVEL and VIDEO RATE
        """
        self.open_new_tab()
        self.switch_to_window(1)
        self.pause(1)
        self.openURL(td.webrtc_url)
        self.pause(3)
        self.clickElementByXPATH(td.audiosourcehead)
        self.pause(2)
        audLEVEL = self.get_element_text_byindex_xpath(td.tab_audio_level, 0)
        self.pause(2)
        self.clickElementByXPATH(td.VideoOutboundhead)
        self.pause(2)
        self.clickElementByXPATH(td.tab_videobytes_persec)
        self.pause(2)
        vdobitrate = self.get_element_text_byindex_xpath(td.tab_videobytes_persec_after_off, 0)
        self.close_window()
        return audLEVEL, vdobitrate

    def audio_video_mute_unmute(self):
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(10)
        self.clickElementByXPATH(td.start_button_xpath)
        self.pause(15)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(2)
        class_audio_unmute = self.isElementPresentByXPATH(td.unmute_audio_btn_xpath)
        class_video_unmute = self.isElementPresentByXPATH(td.non_video_btn_xpath)
        self.pause(2)
        audLEVEL, vdobitrate = self.data_from_webRtc()
        self.switch_to_window(0)
        self.pause(2)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(1)
        self.clickElementByXPATH(td.unmute_audio_btn_xpath)
        self.clickElementByXPATH(td.non_video_btn_xpath)
        self.pause(1)
        class_audio_mute = self.isElementPresentByXPATH(td.mute_audio_btn_xpath)
        class_video_mute = self.isElementPresentByXPATH(td.mute_video_btn_xpath)
        self.pause(2)
        audLEVEL1, vdobitrate1 = self.data_from_webRtc()
        self.switch_to_window(0)
        self.pause(2)
        assert class_audio_unmute is True
        assert class_video_unmute is True
        assert float(audLEVEL) > 0
        assert float(vdobitrate) > 0
        assert class_audio_mute is True
        assert class_video_mute is True
        assert int(audLEVEL1) is 0
        assert int(vdobitrate1) is 0
        self.teardown()


    def packet_loss(self):
        self.setup()
        self.pause(8)
        self.clickElementByXPATH(td.Log_in_button_xpath)
        self.typeTextByXPath(td.user_name, td.Email_box_xpath)
        self.pause(2)
        self.typeTextByXPath(td.password, td.Pwd_box_xpath)
        self.clickElementByXPATH(td.log_in_xpath)
        self.pause(8)
        self.clickElementByXPATH(td.start_button_xpath)
        self.pause(15)
        self.switch_to_iframe_using_css(td.iframe_css)
        self.pause(2)
        self.clickElementByXPATH(td.my_call_box_xpath)
        self.pause(3)
        self.clickElementByXPATH(td.states_icon_xpath)
        self.pause(2)
        resolution = self.getElementTextByXpath(td.resolution_xpath)
        print(self.calculate_screensize(resolution))
        res_v1 = self.calculate_screensize(resolution)
        commands = str(self.read_data_fromfile("TestDataSection","clumzy_cmd_run"))
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
        self.pause(15)
        self.pause(2)
        self.clickElementByXPATH(td.my_call_box_xpath)
        self.pause(3)
        self.clickElementByXPATH(td.states_icon_xpath)
        self.pause(2)
        resolution = self.getElementTextByXpath(td.resolution_xpath)
        print(self.calculate_screensize(resolution))
        res_v2 = self.calculate_screensize(resolution)
        assert res_v1 > res_v2
        self.pause(2)
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c taskkill /f /im clumsy.exe*')
        self.pause(15)
        self.pause(2)
        self.clickElementByXPATH(td.my_call_box_xpath)
        self.pause(3)
        self.clickElementByXPATH(td.states_icon_xpath)
        self.pause(2)
        resolution = self.getElementTextByXpath(td.resolution_xpath)
        print(self.calculate_screensize(resolution))
        res_v3 = self.calculate_screensize(resolution)
        assert res_v2 < res_v3
        self.teardown()


import pytest
from page import TestPage
from assertionsClass import Assertions
from testdata import TestData as td
import cmd_test
from time import sleep


class Test(object):
    ts = TestPage()
    assertion = Assertions()

    @pytest.mark.login
    def test_login(self):
        self.ts.login()

    @pytest.mark.join_call
    def test_join_call(self):
        """This case join the call from available meeting and for this calender should be synced"""
        self.ts.join_call()

    @pytest.mark.test
    def test_sync_calender(self):
        """This case sync the calender of user to 8x8 account and create new meeting"""
        self.ts.calender_sync()

    @pytest.mark.rtc_data_check
    def test_check_webRTC_Data(self):
        self.ts.fetch_webrtc_data()

    @pytest.mark.test
    def test_audio_video(self):
        """This case check audio and video quality"""
        self.ts.get_audio_video_quality()

    @pytest.mark.test
    def test_audio_vdo_mute_unmute(self):
        """This case check audio and video mute and unmute """
        self.ts.audio_video_mute_unmute()

    @pytest.mark.test
    def test_packet_loss(self):
        self.ts.packet_loss()

    @pytest.mark.test3
    def test_all(self):
        try:
            self.ts.master_test_case()
            print("Test Case Passed")
        except :
            print("Test Case Failed")
            self.ts.teardown_page()



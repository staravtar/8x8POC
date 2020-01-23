import pytest
from page import TestPage
from assertionsClass import Assertions
from testdata import TestData as td


class Test:
    ts = TestPage()
    assertion = Assertions()

    @pytest.mark.login
    def test_login(self):
        self.ts.login()

    @pytest.mark.join_call
    def test_join_call(self):
        self.ts.join_call()

    @pytest.mark.sync_calender
    def test_sync_calender(self):
        self.ts.calender_sync()

    @pytest.mark.rtc_data_check
    def test_check_webRTC_Data(self):
        self.ts.fetch_webrtc_data()


    @pytest.mark.audio_video_quality
    def test_audio_video(self):
        self.ts.get_audio_video_quality()

    @pytest.mark.av_mute_unmute
    def test_audio_vdo_mute_unmute(self):
        self.ts.audio_video_mute_unmute()

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


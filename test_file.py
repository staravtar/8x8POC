import pytest
from page import TestPage
from assertionsClass import Assertions


class Test:
    ts = TestPage()
    assertion = Assertions()

    def test_1(self):
        self.ts.scenario1_login()

    def test_2(self):
        self.ts.scenario1_login()

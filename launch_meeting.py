# use python launch_meeting.py url name
#url = meeting url
#name = name of the joynee


from baseClass import SeleniumWebdriverBase
from testdata import TestData as TD
import sys


class Launch_Custom_URL(SeleniumWebdriverBase):

    print(sys.argv[1])
    def launch_the_browser(self):
        self.open_custom_uri(sys.argv[1])
        self.pause(10)
        self.typeTextByXPath(sys.argv[2],TD.enter_name_meeting_joining_xpath)
        self.clickElementByXPATH(TD.button_to_setName)

if __name__=="__main__":
    l=Launch_Custom_URL()
    l.launch_the_browser()
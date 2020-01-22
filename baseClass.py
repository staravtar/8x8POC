import time
import unittest
import os
import re
import datetime

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser


class SeleniumWebdriverBase:
    BY_NAME = "name"
    BY_CSSLOCATOR = "css_locator"
    BY_ID = "id"
    BASE_URL = 'https://app.8x8.vc/'
    """
    Setup Browser type
    """

    def setup(self):
        opt = Options()
        """
        setup webdriver
        :param none"""
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1})

        self.driver = webdriver.Chrome(chrome_options=opt, executable_path="./chromedriver77.exe")
        self.driver.get(self.BASE_URL)
        self.driver.implicitly_wait(30)
        title = self.driver.title
        self.driver.maximize_window()

    def teardown(self):
        """
        teardown webdriver
        :param none
        """

        self.driver.quit()

    def open_custom_uri(self,uri):

        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(executable_path="./chromedriver77.exe",options=opt,)
        self.driver.get(uri)
        title = self.driver.title

    def pause(self, timeInSeconds):
        """
        sleep
        :param timeInSeconds
        """
        time.sleep(timeInSeconds)

    def waitSetUp(self):
        """
        wait webdriver
        :param none
        """
        wait = WebDriverWait(self.driver, 10)

    def getElementClassById(self, id):
        """
        get element by id
        :param id
        """
        print("click on id " + id)
        ele_class = self.driver.find_element_by_id(id).get_attribute("class")
        return ele_class

    def getElementsByClass_manydays(self, tester, css_selector):
        """
        get element by class many-days
        :param none
        """
        element_dict = {}
        class_list = []
        elements = self.driver.find_elements_by_css_selector(css_selector)
        for element in elements:
            print(element.get_attribute("class"))
            print(element.get_attribute("id"))
            if element.get_attribute("class") == "source-item many-days":
                element_dict[element.get_attribute("id")] = element.get_attribute("class")
        return element_dict

    def getElementsByClass_twodays(self, tester, css_selector):
        """"
        get element by class two-days
        :param none
        """
        element_dict = {}
        class_list = []
        elements = self.driver.find_elements_by_css_selector(css_selector)
        for element in elements:
            print(element.get_attribute("class"))
            print(element.get_attribute("id"))
            if element.get_attribute("class") == "source-item two-days":
                element_dict[element.get_attribute("id")] = element.get_attribute("class")
        return element_dict

    def mouseHoverJS(self, element):
        """
        Calls mouse hover event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseover")

    def mouseDownJS(self, element):
        """
        Calls mouse down event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mousedown")

    def mouseUpJS(self, element):
        """
        Calls mouse up event using Java Script
        :param element - Web Element
        """
        self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseup")

    def mouseHover(self, element):
        """
        Calls mouse hover using actions
        :param element - Web Element
        """
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element)
        actionChains.perform()

    def mouseHoverByCss(self, locator):
        """
        Calls mouse hover by Css
        :param element - Web Element
        """
        element = self.driver.find_element_by_css_selector(locator)
        self.mouseHover(element)

    def mouseHoverById(self, id):
        """
        Calls mouse hover by Id
        :param element - Web Element
        """
        element = self.driver.find_element_by_id(id)
        self.mouseHover(element)

    def typeTextByLocator(self, text, locator, clear=None):
        """
        Type Text
        :param element - text, locator
        """
        if (text != "none"):
            element = self.driver.find_element_by_css_selector(locator)
            element.click()
            if clear != False:
                element.clear()
            element.send_keys(text)

    def typeTextByXPath(self, text, locator, clear=None):
        """
        Type Text
        :param element - text, locator
        """
        if (text != "none"):
            element = self.driver.find_element_by_xpath(locator)
            element.click()
            if clear != False:
                element.clear()
            element.send_keys(text)

    def typeText(self, text, byCriteria, value):
        """
        Type Text by criteria
        :param element - text, locator
        """
        print("Type Text " + text)
        if (text != "none"):
            element = self.driver.find_element(by=byCriteria, value=value)
            element.click()
            element.clear()
            element.send_keys(text)

    def typeTextById(self, text, elementId):
        """
        Type Text by id
        :param element - text, id
        """
        print("Type Text " + text)
        if (text != "none"):
            element = self.driver.find_element_by_id(elementId)
            element.click()
            element.clear()
            element.send_keys(text)

    def typeTextByName(self, text, elementName):
        """
        Type Text
        :param element - text, name
        """
        print("Type Text " + text)
        if (text != "none"):
            element = self.driver.find_element_by_name(elementName)
            element.click()
            element.clear()
            element.send_keys(text)

    def search(self, text, locator, clear=None):
        """
        Search Text
        :param element - text, id
        """
        if (text != "none"):
            element = self.driver.find_element_by_css_selector(locator)
            element.click()
            if clear != False:
                element.clear()
            element.send_keys(text, Keys.RETURN)

    def clickElementByLocator(self, css_selector):
        """
        Click Element
        :param element - text, locator
        """
        print("click on css " + css_selector)
        self.driver.find_element_by_css_selector(css_selector).click()

    def clickElementById(self, id):
        """
        Click Element
        :param element - id
        """
        print("click on id " + id)
        self.driver.find_element_by_id(id).click()

    def clickElementByName(self, name):
        """
        Click Element by name
        :param element - name
        """
        self.driver.find_element_by_name(name).click()

    def clickElementByLinkText(self, text):
        """
        Click button by text
        :param element - link-text
        """
        print("click on Link text " + text)
        if (text != "none"):
            self.driver.find_element_by_link_text(text).click()

    def clickElementByXPATH(self, path):
        """
        Click button by xpath
        :param element - xpath
        """
        print("click on xpath " + path)

        actions = ActionChains(self.driver)


        if (path != "none"):

            elements = self.driver.find_elements_by_xpath(path)
            actions.move_to_element(elements[0])
            actions.click(elements[0])
            actions.perform()

    def openURL(self, url):
        """
        Open URL
        :param- URL
        """
        if (url != "none"):
            self.driver.get(url)
            # self.close_alert()

    def close_alert(self):
        """
        lose alert if present when open URL
        :param - none
        """
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            pass

    def clickButtonByText(self, textExpected, locator):
        """
        clicks certain element. It can be button, radio button and so on.
        :param- text, locator
        """
        if (textExpected != "none"):
            webElements = []
            webElements = self.driver.find_elements_by_css_selector(locator)
            for element in webElements:
                textActual = element.text
                if (textActual == textExpected):
                    # if(textActual.equals(textExpected)):

                    element.click()
                    return

    def clickButtonByTextById(self, textExpected, id):
        """
        clicks certain element. It can be button, radio button and so on.
        :param- text, id
        """
        if (textExpected != "none"):
            webElements = []
            webElements = self.driver.find_elements_by_id(id)
            for element in webElements:
                textActual = element.text
                if (textActual == textExpected):
                    element.click()
                    return

    def findElementWithText(self, textExpected, locator):
        """
        Find a certain element. It can be button, radio button and so on.
        :param- text, locator
        """
        if (textExpected != "none"):
            webElements = []
            webElements = self.driver.find_elements_by_css_selector(locator)

            for element in webElements:
                textActual = element.text

                if (textActual == textExpected):
                    print(element)
                    return element

    def doubleClickElement(self, webElement):
        """
        Double click on element
        :param - element
        """
        webElement.click();
        actionChains = ActionChains(self.driver)
        actionChains.doubleClick(webElement).build()
        actionChains.perform()

    def doubleClickElementById(self, elementId):
        """
        Double click element by Id
        :param - elementId
        """
        self.doubleClickElement(self.driver.find_element_by_id(elementId))

    def doubleClickElementByCss(self, locator):
        """
        Double click element by Id
        :param - locator
        """
        self.doubleClickElement(self.driver.find_element_by_css_selector(locator))

    def selectCheckBox(self, locator):
        """
        Checkbox - check/uncheck
        :param - locator
        """
        print("click on checkbox " + locator)
        checkBox = self.driver.find_element_by_css_selector(locator)
        checkBox.click()

    def selectCheckBoxById(self, elementId):
        """
        Checkbox - check/uncheck by Id
        :param - locator
        """
        checkBox = self.driver.find_element_by_id(elementId)
        checkBox.click();

    def verifyElementText(self, expectedText, locator):
        """
       Verify element text
       :param - text, locator
       """
        if (expectedText != "none"):
            element = self.driver.find_element_by_css_selector(locator)
            actualText = element.text
            if (expectedText != actualText):
                self.assert_false((expectedText != actualText), " element does not contain correct text")
        self.pause(2)

    def getElementText(self, locator):
        """
        get element text
       :param -  locator
       """
        element = self.driver.find_element_by_css_selector(locator)
        actualText = element.text
        return actualText

    def getElementTextById(self, id):
        """
        get element text by id
       :param -  id
       """
        element = self.driver.find_element_by_id(id)
        actualText = element.text
        return actualText

    def getAttrribute(self, locator, attribute):
        """
       Verify element attribute
       :param - attribute
       """
        try:
            element = self.driver.find_element_by_css_selector(locator)
            elementAttribute = element.get_attribute(attribute)
            return elementAttribute
        except:
            return "Attribute not found"

    def selectDropDownItem(self, item, locator):
        """
       Select Drop Down Item
       :param - item, locator
       """
        if (item != "none"):
            oSingleSelection = Select(self.driver.find_element_by_css_selector(locator))
            oSingleSelection.select_by_visible_text(item)

    def getSelectedDropDownItem(self, locator):
        """
       get Selected Drop Down Item
       :param - locator
       """
        try:
            oSingleSelection = Select(self.driver.find_element_by_css_selector(locator))
            return oSingleSelection.first_selected_option.text
        except:
            return "selected drop down item not found"

    def upload(self, locator, fileLocation):
        """
       upload a file
       :param - locator, filelocation
       """
        self.driver.find_element_by_css_selector(locator).send_keys(fileLocation)
        self.pause(1)

    def selectValueInList(self, locator, value):
        """
       select a item in a list
       :param - locator, value
       """
        webElement = self.driver.find_element_by_css_selector(locator)

        webElementsList = webElement.find_elements_by_tag_name("option")

        for element in webElementsList:
            if (element.text == value):
                element.click()
                break

    def refresh(self):
        """
       refresh page
       :param - none
       """
        self.driver.refresh()

    def delete_cookies(self, name):
        """
       refresh page
       :param - none
       """
        self.driver.delete_cookie(name);

    def take_screenshot(self, filename, save_location):
        """
        Save a screenshot of the current page.
        :param filename The name of the file to save
        :param save_location Where to save the screenshot
        """
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.driver.get_screenshot_as_file(save_location + '//' + time + '_' + filename + '.png')

    def scroll_down(self, locator):
        # self.driver.find_element_by_css_selector(locator).send_keys(Keys.END)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.pause(1)

    def switch_to_window(self, window_index):
        win_handl = self.driver.window_handles
        open_win = [win for win in win_handl]
        self.driver.switch_to.window(open_win[window_index])

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")

    def read_data_fromfile(self,section,key):
        configr = ConfigParser()
        configr.read("./datahelper.ini")
        return configr.get(section,key)

    def update_data_in_testdatafile(self,section,key,value):
        parser = ConfigParser()
        parser.read("./datahelper.ini")
        parser.set(section,key,value)
        files = open("./datahelper.ini",'w+')
        parser.write(files)
        files.close()

    def get_element_text_byindex_xpath(self,locator,index):
        elements = self.driver.find_elements_by_xpath(locator)

        return elements[index].text
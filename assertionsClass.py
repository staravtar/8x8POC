from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from baseClass import SeleniumWebdriverBase
import re


class Assertions(SeleniumWebdriverBase):
    '''
    classdocs
    '''

    repeatTimes = 6
    waitTime = 1000

    def isTextPresentByLocator(self, expectedText, locator):
        elementsFound = self.driver.find_elements_by_css_selector(locator)
        # expectedText = re.sub(r'[^a-zA-Z0-9 ]',r'',expectedText)
        for element in elementsFound:
            actualText = element.text
            # actualText = re.sub(r'[^a-zA-Z0-9 ]',r'',actualText)
            if (actualText == expectedText):
                return True
        try:
            return (expectedText in self.driver.find_elements_by_css_selector(locator).text)
        except:
            print("Text " + str(expectedText) + " not present")
            return False

    def isTextPresentById(self, expectedText, id):
        elementsFound = self.driver.find_elements_by_id(id)
        for element in elementsFound:
            actualText = element.text
            if (actualText == expectedText):
                return True
        try:
            return (expectedText in self.driver.find_elements_by_id(id).text)
        except:
            print("Text " + str(expectedText) + " not present")
            return False

    def isTextPresentByXPATH(self, expectedText, xpath):
        elementsFound = self.driver.find_elements_by_xpath(xpath)
        for element in elementsFound:
            actualText = element.text
            if (actualText == expectedText):
                return True
        try:
            return (expectedText in self.driver.find_elements_by_id(xpath).text)
        except:
            print("Text " + str(expectedText) + " not present")
            return False

    def isTextPresentByLocator_backup(self, expectedText, locator):
        elementsFound = self.driver.find_elements_by_css_selector(locator)
        for element in elementsFound:
            actualText = element.text
            if (actualText == expectedText):
                return True
            else:
                return False
                print("Text:" + str(expectedText) + "with specified locator is not present")

    def isTextPresent(self, expectedText):
        try:
            return (expectedText in self.driver.find_element_by_css_selector("html>body").text)
        except:
            print("Text:" + str(expectedText) + " not present")
            return False

    def waitForTextPresentByLocatorWithMessage(self, tester, expectedText, locator, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isTextPresentByLocator(expectedText, locator)):
                return
            try:
                print("waiting.....")
                self.pause(waitInterval)
            except:
                print("Text: " + str(expectedText) + " is not present")
        # tester.assertTrue((self.isTextPresentByLocator(expectedText, locator)), message)

    def waitForTextPresentByLocator(self, tester, expectedText, locator):
        self.waitForTextPresentByLocatorWithMessage(tester, expectedText, locator,
                                                    "There is no '" + expectedText + "' text within locator")

    def waitForTextPresent(self, tester, expectedText):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isTextPresent(expectedText)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Text " + str(expectedText) + "Not Present")
        # tester.assertTrue((self.isTextPresent(expectedText)), "There is no '" +  expectedText + "' text on the page")

    '''
    Using Implicit wait
    '''

    def isElementPresentByLocator(self, locator):
        try:

            self.driver.implicitly_wait(2)
            self.driver.find_element_by_css_selector(locator)
            print("check if Element by css_selector is present: " + str(locator))
            return True
        except:

            print("Element by css_selector: " + str(locator) + " is not present")
            return False

    def isElementPresentByLinkText(self, link_text):
        try:

            self.driver.implicitly_wait(2)
            self.driver.find_element_by_link_text(link_text)
            print("check if Element by link_text is present: " + str(link_text))
            return True
        except:

            print("Element by link_text: " + str(link_text) + " is not present")
            return False

    def isElementVisibleByLinkText(self, link_text):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_link_text(link_text).is_enabled()
            print("check if Element by link_text is present: " + str(link_text))
            return True
        except:

            print("Element by link_text: " + str(link_text) + " is not present")
            return False

    def isElementPresentByXPATH(self, xpath):
        try:

            self.driver.implicitly_wait(2)
            self.driver.find_element_by_xpath(xpath)
            print("check if Element by xpath is present: " + str(xpath))
            return True
        except:

            print("Element by xpath: " + str(xpath) + " is not present")
            return False

    def isElementPresentById(self, id):
        try:

            self.driver.implicitly_wait(2)
            self.driver.find_element_by_id(id)
            print("check if Element by id is present: " + str(id))
            return True
        except:
            print("Element by id: " + str(id) + " is not present")
            return False

    def isElementNotPresentById(self, id):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_id(id)
            print("check if Element by id is present: " + str(id))
            return False
        except:
            print("Element by id: " + str(id) + " is not present")
            return False

    def isElementNotPresentByLocator(self, locator):
        try:

            self.driver.implicitly_wait(2)
            self.driver.find_element_by_css_selector(locator)
            return False
        except:

            print("Element by css_selector: " + str(locator) + " is present")
            return False

    def isElementPresent(self, byCriteria, value):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element(by=byCriteria, value=value)
            return True

        except:
            print("Element by criteria: " + str(byCriteria) + " is not present")
            return False

    def isElementPresentByName(self, name):
        try:
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_name(name)

            return True
        except:
            print("Element by name:" + str(name) + " not present")
            return False

    def isElementDisplayed(self, locator):
        try:
            self.driver.implicitly_wait(2)
            return self.driver.find_element_by_css_selector(locator).is_Displayed()
        except:
            print("Element by locator:" + str(locator) + " not present")
            return False

    def isElementEnabled(self, locator):
        try:
            self.driver.implicitly_wait(2)
            return self.driver.find_element_by_css_selector(locator).is_Enabled()
        except:
            return False

    def isElementEnabledWithText(self, text, locator):
        try:
            self.driver.implicitly_wait(2)
            return self.findElementWithText(text, locator).is_Enabled()
        except:
            return False

    def waitForElementEnabledWithText(self, tester, text, locator):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementEnabledWithText(text, locator)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element not enabled")
        # tester.assertTrue((self.isElementEnabled(locator)), "Element with text" + text + "is not enabled")

    def waitForElementPresentByLocatorWithMessage(self, tester, locator, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementPresentByLocator(locator)):
                return
            try:
                'waiting...'
                self.pause(waitInterval)
            except:
                print("Element by locator:" + str(locator) + " not present")
        # tester.assertTrue((self.isElementPresentByLocator(locator)), message)

    def waitForElementPresentByIdWithMessage(self, tester, id, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementPresentById(id)):
                return
            try:
                'waiting...'
                self.pause(waitInterval)
            except:
                print("Element by locator:" + str(id) + " not present")

    def waitForElementPresentByLocator(self, tester, locator):
        self.waitForElementPresentByLocatorWithMessage(tester, locator,
                                                       "Element by" + str(locator) + " not present on page!")

    def waitForElementPresentById(self, tester, id):
        self.waitForElementPresentByIdWithMessage(tester, id, "Element by" + str(id) + " not present on page!")

    def waitForElementDisplayedByLocatorWithMessage(self, tester, locator, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementDisplayed(locator)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element by locator:" + str(locator) + " not displayed")
        # tester.assertTrue((self.isElementPresentByLocator(locator)), message)

    def waitForElementDisplayedByIdWithMessage(self, tester, id, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementDisplayed(id)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element by id:" + str(id) + " not displayed")
        # tester.assertTrue((self.isElementPresentByLocator(locator)), message)

    def waitForElementDisplayedByLocator(self, tester, locator):
        self.waitForElementDisplayedByLocatorWithMessage(tester, locator,
                                                         "Element by" + str(locator) + " not present on page!")

    def waitForElementPresentAndVisible(self, tester, locator):
        self.waitForElementPresentByLocator(tester, locator)
        self.waitForElementDisplayedByLocator(tester, locator)

    def waitForElementEnabled(self, tester, locator):
        self.waitForElementEnabledByLocatorWithMessage(tester, locator, "Element by" + str(locator) + " is not enabled")

    def waitForElementEnabledByLocatorWithMessage(self, tester, locator, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementEnabled(locator)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element by locator:" + str(locator) + "not enabled")
        tester.assertTrue((self.isElementEnabled(locator)), message)

    def assertTextPresent(self, tester, expectedText):
        print("asserting Text " + expectedText)
        assert self.isTextPresent(expectedText) == True, "Text \"" + str(
            expectedText) + "\" not present on page!" + self.driver.find_element_by_css_selector("html>body").text

    def assertElementPresentById(self, tester, id):
        assert self.isElementPresentById(id), "Element by id \"" + str(id) + "\" not present on page!"

    def assertTextNotPresent(self, tester, expectedText):
        assert self.isTextNotPresent(expectedText) == True, "Text \"" + str(expectedText) + "\" is present on page!"

    def assertTextNotPresentById(self, tester, expectedText, locator):
        assert (self.isTextNotPresentById(expectedText, locator)), "Text \"" + str(
            expectedText) + "\" is present on page!"

    def assertTextPresentByLocator(self, tester, expectedText, locator):
        print("asserting Text " + expectedText)
        assert self.isTextPresentByLocator(expectedText, locator) == True, "Text \"" + str(
            expectedText) + " by Locator " + str(locator) + " not present"

    def assertAttributePresentByLocator(self, tester, expected_value, attribute_value):
        print("assert attribute value " + expected_value)
        assert (expected_value == attribute_value), "expected value \"" + str(
            expected_value) + " and attribute value " + str(attribute_value) + " are not same"

    def assertTextPresentByXPATH(self, tester, expectedText, xpath):
        print("asserting Text " + expectedText + " in " + xpath)
        assert self.isTextPresentByXPATH(expectedText, xpath) == True, "Text \"" + str(
            expectedText) + " by xpath " + str(xpath) + " not present"

    def assertTextNotPresentByLocator(self, tester, expectedText, locator):
        assert self.isTextNotPresentByCssSelector(expectedText, locator) == True, "Text \"" + str(
            expectedText) + " by Locator " + str(locator) + " present"

    def assertLabelPresentByLocator(self, tester, label, locator):
        assert (self.isTextPresentByLocator(label, locator)), "Label \"" + str(label) + " by Locator " + str(
            locator) + " not present"

    def assertElementContainsText(self, tester, expectedText, locator):
        print("asserting Text " + expectedText)
        assert (self.isTextPresentByLocator(expectedText, locator)), "Text \"" + str(
            expectedText) + " by Locator " + str(locator) + " not present"

    def assertElementContainsTextById(self, tester, expectedText, id):
        assert (self.isTextPresentById(expectedText, id)), "Text \"" + str(expectedText) + " by Locator " + str(
            id) + " not present"

    def assertElementPresentByLocator(self, tester, locator):
        assert (self.isElementPresentByLocator(locator)), "Element by locator \"" + str(
            locator) + "\" not present on page!"

    def assertElementPresentByLinkText(self, tester, link_text):
        assert (self.isElementPresentByLinkText(link_text)), "Element by link_text \"" + str(
            link_text) + "\" not present on page!"

    def assertElementPresentByXPATH(self, tester, xpath):
        assert (self.isElementPresentByXPATH(xpath)), "Element by link_text \"" + str(xpath) + "\" not present on page!"

    def isElementSelected(self, locator):
        if (self.driver.find_element_by_css_selector(locator).is_selected()):
            return True
        else:
            return False

    def isElementSelectedById(self, id):
        if (self.driver.find_element_by_id(id).is_selected()):
            return True
        else:
            return False

    def isElementWithTextSelected(self, expectedText, locator):
        result = False
        elementsFound = self.driver.find_elements_by_css_selector(locator)
        for element in elementsFound:
            actualText = element.text
            if (actualText == expectedText):

                print(actualText)
                print(str(element))
                print(str(element.is_selected()))
                if (element.is_selected()):
                    result = True
                else:
                    result = False

        return result

    def assertElementPresent(self, tester, byCriteria, value):
        if (self.isElementPresent(byCriteria, value)):
            print("True")
        else:
            print("False")
        assert (self.isElementPresent(byCriteria, value)), "Element by criteria: \"" + str(
            byCriteria) + "\" not present on page!"

    def waitForTitleWithExtraTime(self, tester, title, extra_milliseconds):
        waitInterval = self.waitTime + int(extra_milliseconds) / 100;
        try:
            # Wait before checking the page
            self.pause(1);
        except:
            print("Element not present")
        i = 0
        for i in xrange(self.repeatTimes):
            i = i + 1
            if (self.driver.title.strip() == title):
                print(self.driver.title.strip())
                return
            else:
                try:
                    self.pause(waitInterval)
                except:
                    print("Title:" + title + "not present")
        # TODO: assert self.driver.title.strip(),title, "Current title is equal '" + self.driver.title.strip() + "', but expected to be '" + title + "'"

    '''
     Will wait for some time until the page title will be shown
     @param title - page title
    '''

    def waitForTitle(self, tester, title):
        self.waitForTitleWithExtraTime(tester, title, 0)

    '''
     Is the specified title present on page
     @param title - Page Title
     @return - true if title present, else in other case
    '''

    def isTitlePresent(self, tester, title):
        return tester.assertEqual(self.driver.title.strip(), title,
                                  "Current title is equal '" + self.driver.title.strip() + "', but expected to be '" + title + "'")

    '''
     Assert title present on page
     @param title - Page Title
    '''

    def assertTitle(self, tester, title):
        assert self.isTitlePresent(title) == True

    def waitForElementPresent(self, tester, byCriteria, value):
        self.waitForElementPresentWithMessage(tester, byCriteria, value,
                                              "Element by" + str(byCriteria) + "=" + value + " not present on page!")

    def waitForElementPresentByName(self, tester, name):
        self.waitForElementPresentByNameWithMessage(tester, name,
                                                    "Element with name =" + str(name) + " not present on page!")

    def isTextNotPresentByCssSelector(self, expectedText, locator):
        elementsFound = self.driver.find_elements_by_css_selector(locator)
        for element in elementsFound:
            actualText = element.text
            if (actualText == element.text):
                return False
        return True

    def isTextNotPresent(self, expectedText):
        try:
            result = expectedText not in (self.driver.find_element_by_css_selector("html>body").text)
            return result
        except:
            print("Text:" + str(expectedText) + " is not present")
        return False

    def waitForElementPresentByLocatorWithMessage_OK(self, tester, locator, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            try:
                if (self.isElementPresentByLocator(locator)):
                    return
                self.pause(waitInterval)
            except:
                # Exception
                pass
                print("Element not present")
        tester.assertTrue((self.isElementPresentByLocator(locator)), message)

    '''
    Using Web Driver Wait
    '''

    def isElementPresentByLocator_OK(self, locator):
        wait = WebDriverWait(self.driver, 10)

        def present(element):
            if element.is_displayed():
                return element
            return False

        element = wait.until(lambda d: present(d.find_element_by_css_selector(locator)))
        if (element == False):

            return False
        else:
            return True

    def waitForElementPresentWithMessage(self, tester, byCriteria, value, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementPresent(byCriteria, value)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element by criteria:" + str(byCriteria) + " not present")

    def waitForElementPresentByNameWithMessage(self, tester, name, message):
        waitInterval = self.waitTime / 100
        i = 0
        for i in range(self.repeatTimes):
            i = i + 1
            if (self.isElementPresentByName(name)):
                return
            try:
                self.pause(waitInterval)
            except:
                print("Element by name:" + str(name) + " not present")

    # @brief: Wait for text on the page and assert if the text is present
    # param :expectedText: any text message
    # description: Wait for text on the page to be present until the expected wait time and assert if the text is present

    def waitAndAssertTextPresentOnPage(self, tester, expectedText):
        self.waitForTextPresent(tester, expectedText)
        tester.assertTrue((self.isTextPresent(expectedText)), "There is no '" + expectedText + "' text on the page")

    # 
    # Brief Description : hide Work Hub locator from download page when Public hub is selected for iOS

    def isCheckboxSelectedBySelector(self, locator):
        element = self.driver.find_element_by_css_selector(locator)
        return element.get_attribute("checked")

    def assertElementNotPresentByLocator(self, tester, locator):
        assert self.isElementNotPresentByLocator(locator) != True, "Element by locator \"" + str(
            locator) + "\" presents on page!"

    def assertElementNotPresentByXpath(self, tester, xpath):
        assert self.isElementNotPresentByXpath(xpath) != True, "Element by xpath \"" + str(
            xpath) + "\" presents on page!"

    def assertElementNotDisplayedById(self, tester, id):
        assert self.isElementDisplayedById(id) != True, "Element by id \"" + str(id) + "\" displayed on page!"

    def assertElementNotPresentByName(self, tester, name):
        assert self.isElementPresentByName(name) != True, "Element by name \"" + str(name) + "\" not present on page!"

    def assertCheckboxNotSelectedBySelector(self, tester, locator):
        element = self.driver.find_element_by_css_selector(locator)
        assert element.get_attribute("checked") == True

    def assertCheckboxSelectedBySelector(self, tester, locator):
        element = self.driver.find_element_by_css_selector(locator)
        assert element.get_attribute("checked") == True

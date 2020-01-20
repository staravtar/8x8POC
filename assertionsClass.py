from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from baseClass import BaseClass


class Assertions(BaseClass):

    def get_text_from_element(driver,locator):
        wait = WebDriverWait(driver,20)
        try:
            webelement =wait.until(ec.visibility_of_element_located((By.XPATH,locator)))
            text = webelement.text
            return text
        except :
            print(f"get_text_from_element assertion failed for {locator} element")

    def get_current_window_ID(driver):
        try:
            ids = driver.window_handles
            #id = driver.current_window_handle
            return ids[-1]
        except :
            print(f"get_current_window_ID assertion failed")

    def get_list_ofelements_byXpath(driver,locator):
        wait = WebDriverWait(driver,20)
        try:
            elements =wait.until(ec.visibility_of_any_elements_located((By.XPATH,locator)))
            if len(elements) > 0:
                return elements
        except:
            print(f"get_list_ofelements_byXpath assertion failed for {locator} element")

    def get_list_ofelements_byCss(driver,locator):
        wait = WebDriverWait(driver,20)
        try:
            elements = wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR,locator)))
            if len(elements) > 0:
                return elements
        except:
            print(f"get_list_ofelements_byCss assertion failed for {locator} element")

    def set_text_to_element(driver,locator,text):
        try:
            element = driver.find_element_by_xpath(locator)
            element.clear()
            element.send_keys(text)
            return True
        except:
            print(f"set_text_to_element assertion failed for {locator} element")

    def verify_element_visibility(driver,locator):
        wait = WebDriverWait(driver,10)
        try:
            elements =wait.until(ec.visibility_of_all_elements_located((By.XPATH,locator)))
            if len(elements) > 0 and elements[0].is_displayed():
                return True
        except:
            print(f"verify_element_visibility assertion failed for {locator} element")

    def verify_element_enable(driver,locator):
        wait = WebDriverWait(driver,10)
        try:
            elements =wait.until(ec.presence_of_all_elements_located((By.XPATH,locator)))
            if len(elements) > 0 and elements[0].is_enabled():
                return True
        except:
            print(f"verify_element_enable assertion failed for {locator} element")

    def click_onElement(driver,locator):
        #print(type(locator))
        wait = WebDriverWait(driver,10)
        actions = ActionChains(driver)

        try:
            if(str == type(locator)):
                elements = wait.until(ec.visibility_of_all_elements_located((By.XPATH,locator)))
                actions.move_to_element(elements[0]).click(elements[0])
                actions.perform()
                return True
            else:
                driver.implicitly_wait(15)
                actions.move_to_element(locator).click(locator)
                actions.perform()
                return True

        except :
            print(f"click_onElement assertion failed for {locator} element")

    def set_focus_onIframe(driver,locator):
        wait = WebDriverWait(driver,10)
        try:
            elements = wait.until(ec.visibility_of_all_elements_located((By.XPATH,locator)))
            driver.switch_to.frame(elements[0])
            return True
        except :
            print(f"set_focus_onIframe assertion failed for {locator} element")

    def set_focus_onwindow(driver):
        try:
            driver.switch_to_window(self.get_current_window_ID(driver))
            return True
        except :
            print("set_focus_onwindow assertion failed.")

    def implicitWait(driver):
        driver.implicitly_wait(20)
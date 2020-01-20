from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser
from os import path
import sys

class  BaseClass():



    def new_webdriver(self):
        driver = webdriver.Chrome(executable_path="./chromedriver77.exe")
        return driver

    def kill_driver(self):
        self.driver.quiet()


    def read_data_fromFile(self,section,key):
        configr = ConfigParser()
        configr.read("./datahelper.ini")
        return configr.get(self,section,key)

    def update_data_in_datafile(self,section,key,value):
        parser = ConfigParser()
        parser.read("./datahelper.ini")
        parser.set(section,key,value)
        files = open("./datahelper.ini",'w+')
        parser.write(files)
        files.close()
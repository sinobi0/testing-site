from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import unittest
import pytest
from selenium.webdriver.chrome.options import Options

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


def test(browser):
    browser.get(link)
    button = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button')
    assert button, 'No way'

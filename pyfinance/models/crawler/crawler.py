# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import pandas

import pandas_datareader
import requests

import datetime
from datetime import timedelta


def get_csv(word):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "https://trends.google.com.tw/trends/explore?date=2012-05-06%202017-04-23&q="+word
    verificationErrors = []
    accept_next_alert = True

    driver.get(base_url)
    driver.find_element_by_css_selector(".widget-actions-menu").click()
    driver.find_element_by_xpath("//button[3]").click()
    driver.close()






def get_yahoo(number):
    yahoo_d = pandas_datareader.DataReader(number, data_source='yahoo',
                                          start=datetime.datetime(2012, 5, 6),
                                          end=datetime.datetime(2017, 4, 23))
    yahoo_d.index = yahoo_d.index.map(lambda e: e - timedelta(days=1))
    return yahoo_d


def merge_csv_and_yahoo(yahoo):
    csv = pandas.read_csv('data/multiTimeline.csv', header=1, index_col=['週'], parse_dates=True)
    results = yahoo.merge(csv, left_index=True, right_index=True, how='inner')
    data = results[['Close', 'iphone: (全球)']]
    return data



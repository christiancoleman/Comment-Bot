#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser


# In[2]:


from bs4 import BeautifulSoup
from config import user, password, the_assignment
import time


# In[3]:


executable_path = {'executable_path': '/home/datavisualization/DV/python-homework-scraper/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


browser.visit("https://bootcampspot.com")


# In[5]:


browser.find_by_css("#emailAddress").type(user)
browser.find_by_css("#password").type(password)
browser.find_by_css("button.btn-submit").click()


# In[6]:


time.sleep(2)
browser.find_by_css("td.col-md-3:nth-child(3)").click()
browser.find_by_css("span").click()


# In[7]:


browser.find_by_xpath(".//a[contains(@href,'gradebook')]").click()
browser.find_option_by_text(the_assignment).first.click()
browser.find_option_by_text("0: Data Prework").first.click()
time.sleep(2)
browser.find_option_by_text(the_assignment).first.click()


# In[8]:


def calll():
    try:
        browser.find_by_css("button.btn-save").click()
    except:
        print("error")

stage = 0
with open("comment.txt") as fp:
    line = fp.readline()
    while line:
        
        if len(line) == 1:
            stage += 1
            
        if stage == 0:
            browser.find_by_text(line.strip()).find_by_xpath('..').find_by_css("a.text-link").click()
        elif stage == 1:
            browser.find_by_tag("textarea").type(line.strip())
            calll()
        elif stage == 2:
            print(line.strip())
            
            try:
                browser.find_option_by_text(line.strip()).first.click()
            except:
                print("no grade")
        elif stage == 3:
            try:
                browser.find_option_by_text(line.strip()).first.click()
            except:
                print("no grade")
                
            if line.strip() == "END":
                stage = 0
                browser.find_by_xpath(".//a[contains(@href,'gradebook')]").click()
                browser.find_option_by_text(the_assignment).first.click()
                browser.find_option_by_text("0: Data Prework").first.click()
                time.sleep(2)
                browser.find_option_by_text(the_assignment).first.click()
                         
        line = fp.readline()
        time.sleep(2)
browser.quit()


# In[ ]:





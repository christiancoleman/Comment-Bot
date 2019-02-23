from splinter import Browser
from bs4 import BeautifulSoup
from config import user, password, the_assignment
import time
from sys import platform
import os

executable_path = None

if platform == "linux" or platform == "linux2":
    executable_path = {'executable_path': os.path.join("binaries", "chromedriver-linux")}
elif platform == "darwin":
    executable_path = {'executable_path': os.path.join("binaries", "chromedriver-mac")}
elif platform == "win32":
    executable_path = {'executable_path': os.path.join("binaries", "chromedriver-windows.exe")}

print(executable_path)

browser = Browser('chrome', **executable_path, headless=False)

#Input your credentials
browser.visit("https://bootcampspot.com")
browser.find_by_css("#emailAddress").type(user)
browser.find_by_css("#password").type(password)
browser.find_by_css("button.btn-submit").click()
time.sleep(2)

#Navigate to the main menu, comment out lines 17 - 18 if you went directly to the main menu
browser.find_by_css("td.col-md-3:nth-child(3)").click()
browser.find_by_css("span").click()

#main menu
browser.find_by_xpath(".//a[contains(@href,'gradebook')]").click()

#gradeook
browser.find_option_by_text(the_assignment).first.click()
browser.find_option_by_text("0: Data Prework").first.click()
time.sleep(2)
browser.find_option_by_text(the_assignment).first.click()

# function used for saving comments
def calll():
    try:
        browser.find_by_css("button.btn-save").click()
    except:
        print("error")

#Start Reading Comments
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
        
 #Quit Browser
browser.quit()

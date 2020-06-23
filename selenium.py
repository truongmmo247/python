#pip install selenium
#http://chromedriver.chromium.org/downloads
#chuyên py sang .exe pyinstaller --onefile -w tkinter_demo.py

from selenium import webdriver
from time import sleep
 
 
class HelloSelenium:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
 
    def get_site_info(self):
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        sleep(5)
        self.driver.save_screenshot('screen_shot.png')
 
 
if __name__ == '__main__':
    hello = HelloSelenium('https://nguyenvanhieu.vn')
    hello.get_site_info()
    # Close driver
    hello.driver.close()
 

from asyncio.format_helpers import extract_stack
from selenium import webdriver
from time import sleep 
from login_details import email, password
from selenium.webdriver.common.keys import Keys
import random

class TinderBot():
    def __init__(self): # automatically run
        self.driver = webdriver.Chrome()  #control de browser
    

    # Test open tinder
    def open_tinder(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        login = self.driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]') # select the login element
        login.click()
        sleep(1)
        self.facebook_login()

        sleep(6)
        try:
           allow_location_button = self.driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[3]/button[1]')
           allow_location_button.click()
        except:
          print('no location popup')

        try:
           allow_notification_button = self.driver.find_element('xpath','/html/body/div[2]/main/div/div/div/div[3]/button[2]')
           allow_notification_button.click()
        except:
          print('no notification popup')
            
        sleep(1)

        # cookies close wd
        cookies_denied_btn = self.driver.find_element('xpath','/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button')
        cookies_denied_btn.click()

        sleep(5)

        # close welcome promotion

        """ base_window = self.driver.window_handles[0]  # Tinder window
        waiting_matches_popup_wd = self.driver.window_handles[1]
        self.driver.switch_to.window(waiting_matches_popup_wd) 
        mayb_after_btn = self.driver.find_element('xpath','/html/body/div[2]/main/div/div/div[3]/button[2]')
        mayb_after_btn.click()
        self.driver.switch_to.window(base_window) """


        mayb_after_popup = self.driver.find_element('xpath','/html/body/div[2]/main/div/div/div[3]/button[2]/span')
        mayb_after_popup.click()

        """ add_to_principal_popup = self.driver.find_element('xpath','/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]')
        add_to_principal_popup.click()  """

        
    # fb login 
    def facebook_login(self):
        # find and clck fb login btn
        login_with_fb = self.driver.find_element('xpath','/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_with_fb.click()

        # save references to main and fb windows
        sleep(2)
        base_window = self.driver.window_handles[0]  # Tinder window
        fb_popup_wd = self.driver.window_handles[1]

        # Switch to Fb window
        self.driver.switch_to.window(fb_popup_wd)

        # find enter email, pwd, login
        # cookies fb
            # cookies_accept_button = self.driver.find_element('xpath',)
            # cookies_accept_button.click()

        # Login to FB
        email_field = self.driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pwd_field = self.driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_btn = self.driver.find_element('xpath','/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')

        # enter email, pwd and login
        email_field.send_keys(email)
        pwd_field.send_keys(password)
        login_btn.click()
        self.driver.switch_to.window(base_window)

    def extra_popup(self):
        add_to_principal_popup = self.driver.find_element('xpath','/html/body/div[2]/main/div/div[2]/button[2]/div[2]/span[2]')
        add_to_principal_popup.click() 

    def riht_swipe(self):
        try:
            doc = self.driver.find_element('xpath','//*[@id="Tinder"]/body')
            doc.send_keys(Keys.ARROW_RIGHT)
        except:
            self.extra_popup()
            
            

    def dislike(self):
        doc = self.driver.find_element('xpath','//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)

    def auto_swipe(self):  # keep swiping
        liking_odds = .95

        while True:
            if random.random() < liking_odds:
                try:
                    self.riht_swipe()
                except:
                    self.close_match()

            else:
                self.dislike()

            random_sleep = random.random() *2
            sleep(random_sleep)  # time.sleep
             
            

    def close_match(self):
        match_popup = self.driver.find_element('xpath','//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    
# mimicking human behaivour

bot = TinderBot()
bot.open_tinder()
sleep(10)
bot.auto_swipe()


#based on https://github.com/tuomaskivioja/tinderBot/blob/master/tinder_bot.py
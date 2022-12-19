from self import self
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from flask import Flask
from flask import Flask, session
import time
import csv

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    # "automationName": "UiAutomator"

}
self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

with open('data.csv','r') as csv_file:
    with open('log.txt', "w") as outfile:
        # oline = outfile.write()
        csv_reader = csv.reader(csv_file)

        count = 0
        def setUp(self):
            for line in csv_reader:
                # driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="YouGotaGift"]').click()
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'//android.widget.TextView[@content-desc="YouGotaGift"]'))).click()
                time.sleep(3)

                # click myaccount
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[5]'))).click()
                time.sleep(1)
                
                # click profile
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]'))).click()
                time.sleep(1)
                
                # # Click add number
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView[2]'))).click()
                time.sleep(1)
                
                # # click country code
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout'))).click()
                time.sleep(1)
                
                # # type country
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText'))).send_keys("pakistan")
                time.sleep(1)
                
                # click pakistan
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout'))).click()
                time.sleep(1)
                
                # paste number
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(line[0])
                time.sleep(1)
                
                # click verify
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[2]'))).click()
                time.sleep(1)
                
                # verify otp field
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText'))).click()
                # time.sleep(1)

                count = count + 1
                print(count)
                print(line[0])
                outfile.write(line[0]+"\n")

            def tearDown(self):
                self.driver.quit()

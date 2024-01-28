from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from .utils import PATH


desired_caps = dict(
    platformName='Android',
    platformVersion='9',
    automationName='uiautomator2',
    deviceName='Bluestacks App Player',
    appPackage='id.ac.telkomuniversity.celoestudent',
    appActivity='.MainActivity',
    noReset='true',
    ignoreUnimportantViews='true',
    # enableMultiWindows=True
)
driver = webdriver.Remote('http://localhost:4723', desired_caps)

def wait(sec):
    try:
        WebDriverWait(driver, sec).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="wait"]')))
    except:
        pass

class BaseModel:
    def setUpModel(self):
        global driver
        self.driver = driver


class CeloeModel(BaseModel):

    def v_LoginPage(self):
        pass

    def e_LoginSuccessful(self):
        pass

    def e_LoginFailed(self):
        pass

    def v_Home(self):
        pass

    def e_SelectDashboard(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-tab-3-tab"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-tab-3-tab"]')
        element.click()

    def v_Dashboard(self):
        wait(1)

    def e_SelectCourse(self):
        self.driver.swipe(600, 500, 600, 10, 1000)
        self.driver.swipe(600, 500, 600, 10, 1000)
        # self.driver.swipe(600, 500, 600, 10, 1000)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '(//android.view.View[@text="Test Course 3"])[1]')))
        element = self.driver.find_element_by_xpath('(//android.view.View[@text="Test Course 3"])[1]')
        element.click()

    def v_CourseView(self):
        wait(1)

    def e_SelectAssignment(self):
        pass

    def v_Assignment(self):
        pass

    def e_SelectForum(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3724972"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3724972"]')
        element.click()

    def v_Forum(self):
        wait(3)

    def e_SelectFile(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3725737"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3725737"]')
        element.click()

    def v_File(self):
        wait(1)

    def e_SelectQuiz(self):
        pass

    def v_Quiz(self):
        pass

    ### ASSIGNMENT FEATURE ###
    def e_SelectNotSubmitted(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3724365"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3724365"]')
        element.click()

    def v_NotSubmitted(self):
        wait(1)

    def e_AddSubmission(self):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'EDIT SUBMISSION')))
            element = self.driver.find_element_by_accessibility_id('EDIT SUBMISSION')
            element.click()
        except:
            TouchAction(driver).tap(None, 500, 600, 2).perform()

    def v_AddingSubmission(self):
        wait(1)

    def e_Submit(self):
        # click add file
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'add ADD FILE')))
        element = self.driver.find_element_by_accessibility_id('add ADD FILE')
        element.click()
        # click folder
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="folder File"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="folder File"]')
        element.click()
        # click sm
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'android:id/summary')))
        element = self.driver.find_element_by_id('android:id/summary')
        element.click()
        # click dcim
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="DCIM"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="DCIM"]')
        element.click()
        # click sharedfolder
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="SharedFolder"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="SharedFolder"]')
        element.click()
        # click pdf
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="File.pdf"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="File.pdf"]')
        element.click()
        # click save
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Save"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="Save"]')
        element.click()
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="OK"]')))
            element = self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]')
            element.click()
        except:
            pass

    def e_SelectSubmitted(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3751679"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3751679"]')
        element.click()

    def v_Submitted(self):
        wait(1)

    def e_BackAssignment(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})
    
    def v_Submitted(self):
        wait(1)

    def e_EditSubmission(self):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'EDIT SUBMISSION')))
            element = self.driver.find_element_by_accessibility_id('EDIT SUBMISSION')
            element.click()
        except:
            TouchAction(driver).tap(None, 500, 600, 2).perform()

    def v_EditingSubmission(self):
        wait(1)

    def e_SaveSubmission(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Save"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="Save"]')
        element.click()
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="OK"]')))
            element = self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]')
            element.click()
        except:
            pass

    def e_ReplaceSubmission(self):
        # click add file
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'add ADD FILE')))
        element = self.driver.find_element_by_accessibility_id('add ADD FILE')
        element.click()
        # click folder
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="folder File"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="folder File"]')
        element.click()
        # click sm
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'android:id/summary')))
        element = self.driver.find_element_by_id('android:id/summary')
        element.click()
        # click dcim
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="DCIM"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="DCIM"]')
        element.click()
        # click sharedfolder
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="SharedFolder"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="SharedFolder"]')
        element.click()
        # click pdf
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="File.pdf"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="android:id/title" and @text="File.pdf"]')
        element.click()
        # delete previous file
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Delete"]')))
            element = self.driver.find_elements_by_xpath('//android.widget.Button[@text="Delete"]')
            element[0].click()

            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="DELETE"]')))
            element = self.driver.find_element_by_xpath('//android.widget.Button[@text="DELETE"]')
            element.click()
        except:
            pass

    ### END OF ASSIGNMENT FEATURE ###


    ### FORUM FEATURE ###
    def e_BackForum(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})
    
    def e_AddDiscussion(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Add a new discussion topic"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="Add a new discussion topic"]')
        element.click()

        wait(1)

        # input subject
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText')))
        element = self.driver.find_elements_by_xpath('//android.widget.EditText')
        element[0].click()
        element[0].send_keys("subject")
        # input message
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text="​"]')))
        element = self.driver.find_element_by_xpath('//android.widget.EditText[@text="​"]')
        element.click()
        element.send_keys("his is a message")
        self.driver.press_keycode(48)
        # post to forum
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="POST TO FORUM"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="POST TO FORUM"]')
        element.click()

    def v_DiscussionAdded(self):
        wait(1)

    def e_DeleteDiscussion(self):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="subject"]')))
            element = self.driver.find_elements_by_xpath('//android.view.View[@text="subject"]')
            element[0].click()
        except:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="subject edited"]')))
            element = self.driver.find_elements_by_xpath('//android.view.View[@text="subject edited"]')
            element[0].click()

        wait(2)

        # click 3 dots
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Display options"]')))
        element = self.driver.find_elements_by_xpath('//android.widget.Button[@text="Display options"]')
        element[1].click()

        wait(2)

        # click delete
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Delete"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Delete"]')
        element.click()
        # click delete dialog
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="DELETE"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="DELETE"]')
        element.click()

    def e_SelectDiscussion(self):
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="subject"]')))
            element = self.driver.find_elements_by_xpath('//android.view.View[@text="subject"]')
            element[0].click()
        except:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="subject edited"]')))
            element = self.driver.find_elements_by_xpath('//android.view.View[@text="subject edited"]')
            element[0].click()

    def v_Discussion(self):
        wait(3)

    def e_BackDiscussion(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})

    def e_ParticipateDiscussion(self):
        # click reply
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="REPLY"]')))
        element = self.driver.find_elements_by_xpath('//android.widget.Button[@text="REPLY"]')
        element[0].click()
        # input reply
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@text="​"]')))
            element = self.driver.find_element_by_xpath('//android.widget.EditText[@text="​"]')
            element.click()
            self.driver.press_keycode(29)
        except:
            TouchAction(driver).tap(None, 500, 1000, 2).perform()
            self.driver.press_keycode(29)

        # post to forum
        self.driver.swipe(600, 400, 600, 10, 1000)
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="POST TO FORUM"]')))
            element = self.driver.find_element_by_xpath('//android.widget.Button[@text="POST TO FORUM"]')
            element.click()
        except:
            self.driver.swipe(600, 400, 600, 10, 1000)
            TouchAction(driver).tap(None, 300, 1515, 2).perform()

        wait(3)

        # delete reply
        # click 3 dots
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Display options"]')))
        element = self.driver.find_elements_by_xpath('//android.widget.Button[@text="Display options"]')
        element[-1].click()
        
        wait(1)

        # click delete
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Delete"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Delete"]')
        element.click()
        # click delete dialog
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="DELETE"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="DELETE"]')
        element.click()

    def e_EditDiscussion(self):
        # click 3 dots
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Display options"]')))
        element = self.driver.find_elements_by_xpath('//android.widget.Button[@text="Display options"]')
        element[1].click()

        wait(1)

        # click edit
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Edit"]')))
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Edit"]')
        element.click()

    def v_EditingDiscussion(self):
        wait(1)

    def e_SaveDiscussion(self):
        # edit subject
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText')))
        element = self.driver.find_elements_by_xpath('//android.widget.EditText')
        element[0].click()
        element[0].send_keys("subject edited")
        # save changes
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="SAVE CHANGES"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="SAVE CHANGES"]')
        element.click()

    ### END OF FORUM FEATURE ###


    ### FILE FEATURE ###
    def e_BackFile(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})

    def e_OpenFile(self):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'document OPEN THE FILE')))
        element = self.driver.find_element_by_accessibility_id('document OPEN THE FILE')
        element.click()

    def v_OpeningFile(self):
        wait(1)

    def e_CloseFile(self):
        wait(3)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})

    ### END OF FILE FEATURE ###


    ### QUIZ FEATURE ###
    def e_BackQuiz(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})

    def e_SelectNotAttempted(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3725738"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3725738"]')
        element.click()

    def v_NotAttempted(self):
        wait(1)

    def e_AttemptQuiz(self):
        wait(2)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="PREVIEW QUIZ NOW"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="PREVIEW QUIZ NOW"]')
        element.click()

    def v_InProgress(self):
        wait(3)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.RadioButton')))
        element = self.driver.find_elements_by_xpath('//android.widget.RadioButton')
        element[0].click()

    def e_FinishAttempt(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="NEXT arrow forward"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="NEXT arrow forward"]')
        element.click()

    def v_FinishingAttempt(self):
        wait(1)

    def e_ReturnAttempt(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'RETURN TO ATTEMPT')))
        element = self.driver.find_element_by_accessibility_id('RETURN TO ATTEMPT')
        element.click()

    def e_SubmitAttempt(self):
        # click submit
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'SUBMIT ALL AND FINISH')))
        element = self.driver.find_element_by_accessibility_id('SUBMIT ALL AND FINISH')
        element.click()
        # click ok
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="OK"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]')
        element.click()

    def v_ReviewingAttempt(self):
        wait(1)

    def e_FinishReview(self):
        wait(1)
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})

    def e_SelectAttempted(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="core-course-module-3751664"]')))
        element = self.driver.find_element_by_xpath('//android.view.View[@resource-id="core-course-module-3751664"]')
        element.click()

    def e_Attempted(self):
        wait(1)

    def e_ReviewAttempt(self):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Click here to see more detail')))
        element = self.driver.find_element_by_accessibility_id('Click here to see more detail')
        element.click()

    def v_Attempted(self):
        wait(1)

    def e_AttemptAgain(self):
        wait(2)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="PREVIEW QUIZ NOW"]')))
        element = self.driver.find_element_by_xpath('//android.widget.Button[@text="PREVIEW QUIZ NOW"]')
        element.click()

    ### END OF QUIZ FEATURE ###
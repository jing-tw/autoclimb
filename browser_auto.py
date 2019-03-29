import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains   # for auto scroll


class BrowserAuto:
    WAIT_SEC = 0.4
    MAX_WAIT_CNT = 500

    def __init__(self, addr_park):
        self.addr_park= addr_park
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.get(self.addr_park)
        self.driver.implicitly_wait(10)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click(self, strTitle):

        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                time.sleep(self.WAIT_SEC) 
                str_comm = '//*[@title="' + strTitle + '"]'
                element = self.driver.find_element_by_xpath(str_comm)
                self.scroll_to_element(element)
                element.click()
                bRun = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1

    def click_id(self, strID):
        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                element = self._get_elm_id(strID)
                #self.scroll_to_element(element)
                element.click()
                bRun = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1

    def fill_text(self, strID, strText):
        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                # fill_text
                element = self._get_elm_id(strID)
                self.scroll_to_element(element)
                element.send_keys(strText)
                # end of fill_text
                bRun = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1

    def select_inx(self, strID, inx):
        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                # select
                time.sleep(self.WAIT_SEC)
                element = self._get_elm_id(strID)
                self.scroll_to_element(element)
                sele = Select(element)
                sele.select_by_index(inx)
                # end of select
                bRun = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1
    
    def set_yyyymmdd(self, strID, yyyy, mm, date):
        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                # set_yyyymmdd
                self._set_yyyymmdd(strID, yyyy, mm, date)
                # end of set_yyyymmdd
                bRun = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1

    def _set_yyyymmdd(self, strID, yyyy, mm, date):
        self.click_id(strID)
        time.sleep(self.WAIT_SEC)
        element = self.driver.find_element_by_class_name('ui-datepicker-year')
        sele = Select(element)
        sele.select_by_index(int(yyyy)-1929)  # 0: 1929
        
        time.sleep(self.WAIT_SEC)
        element = self.driver.find_element_by_class_name('ui-datepicker-month')
        sele = Select(element)
        sele.select_by_index(int(mm)-1)  # 0: 一月

        elements = self.driver.find_elements_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
        for dates in elements:
            if(dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("innerText")) == str(date)):
                dates.click()

    def handle_alert_popup(self):
        # wait for alert window  
        # prevent: 
        #  Message: unexpected alert open: {Alert text :      
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        element = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present() 
        )

        # accept
        alert = self.driver.switch_to_alert()
        alert.accept()

    def _get_elm_id(self, strID):
        # https://selenium-python.readthedocs.io/waits.html
        
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        time.sleep(self.WAIT_SEC) 
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, strID)) and 
            EC.element_to_be_clickable((By.ID, strID))
        )
        
        return element
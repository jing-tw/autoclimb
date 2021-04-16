'''
The browser automatic fill module.
'''
from datetime import datetime
import traceback
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.action_chains import ActionChains   # for auto scroll
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class BrowserAuto:
    '''
    Broswer automatic fill class
    '''
    SPEED_DEFAULT = 1  # wait sec
    MAX_WAIT_CNT = 500

    def __init__(self, addr_park):
        self.addr_park = addr_park
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # self.driver = webdriver.Chrome(chrome_options=options)
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.addr_park)
        self.driver.implicitly_wait(10)
        self.__wait_sec__ = 1
        self.speed_init()

    def speed_init(self):
        '''
        Init the auto fill speed.
        '''
        self.__wait_sec__ = self.SPEED_DEFAULT
        self.__wait_sec_calendar__ = self.SPEED_DEFAULT

    def speed_up(self):
        '''
        Increase the speed.
        '''
        self.__wait_sec__ = 0.05

    def __scroll_to_element__(self, element):
        str_script_center = 'var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);' \
                            + 'var elementTop = arguments[0].getBoundingClientRect().top;' \
                            + 'window.scrollBy(0, elementTop-(viewPortHeight/2));'

        self.driver.execute_script(str_script_center, element)

    def sleep(self, int_unit):
        '''
        sleep in unit __wait_sec__ sec.
        '''
        time.sleep(self.__wait_sec__ * int_unit)

    def __do_action__(self, str_cmd, dict_arg):
        b_run = True
        cnt = 0
        b_ok = 0
        msg = 'false'

        while b_run:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT')
                    b_run = False
                time.sleep(self.__wait_sec__)
                b_ok, msg = self.__switch__(str_cmd, dict_arg)
                b_run = False
            except (selenium.common.exceptions.StaleElementReferenceException, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementNotInteractableException) as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1

        return b_ok, msg

    def __switch__(self, str_cmd, dict_arg):
        fun_switch = {
            'click': self.__click__,
            'click_id': self.__click_id__,
            'fill_text': self.__fill_text__,
            'select_inx': self.__select_inx__,
            'set_yyyymmdd': self.__set_yyyymmdd__,
            'fill_text_verify':self._fill_text_verify,
        }

        return fun_switch[str_cmd](dict_arg)

    def click(self, str_title):
        '''
        Click web element.
        '''
        dict_arg = {}
        dict_arg['str_title'] = str_title
        return self.__do_action__('click', dict_arg)

    def __click__(self, dict_arg):
        str_title = dict_arg['str_title']
        str_cmd = '//*[@title="' + str_title + '"]'
        element = self.driver.find_element_by_xpath(str_cmd)
        self.__scroll_to_element__(element)
        element.click()
        return 1, 'ok'

    def get_attribute(self, str_type, str_id):
        '''
        Get the element value.
        '''
        element = self._get_elm_id(str_id)
        str_value = element.get_attribute(str_type)
        print('str_id = ', str_id, ' str_value = ', str_value)
        return str_value

    def click_id(self, str_id):
        '''
        Click web element by id.
        '''
        self.sleep(1)
        dict_arg = {}
        dict_arg['str_id'] = str_id
        return self.__do_action__('click_id', dict_arg)

    def __click_id__(self, dict_arg):
        str_id = dict_arg['str_id']
        element = self._get_elm_id(str_id)
        element.click()

        return 1, 'ok'

    def fill_text(self, str_id, str_text, b_refilled):
        '''
        Fill text.
        '''
        return self.__fill_text_core__('fill_text', str_id, str_text, b_refilled)

    def fill_text_verify(self, str_id, str_text):
        '''
        Fill text.
        '''
        try:
            _, msg = self.__fill_text_core__('fill_text_verify', str_id, str_text, 0)
            return 1, msg
        except Exception:
            traceback.print_exc()
            return 0, 'self.__fill_text_core__ Exception'

    def __fill_text_core__(self, str_fun_name, str_id, str_text, b_refilled):
        dict_arg = {}
        dict_arg['str_id'] = str_id
        dict_arg['str_text'] = str_text
        dict_arg['b_refilled'] = b_refilled

        return self.__do_action__(str_fun_name, dict_arg)

    def __fill_text__(self, dict_arg):
        str_id = dict_arg['str_id']
        str_text = dict_arg['str_text']
        b_refilled = dict_arg['b_refilled']
        element = self._get_elm_id(str_id)
        self.__scroll_to_element__(element)

        if b_refilled:

            element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(str_text)

        return 1, 'ok'

    def _fill_text_verify(self, dict_arg):
        str_id = dict_arg['str_id']
        str_text = dict_arg['str_text']
        element = self._get_elm_id(str_id)
        self.__scroll_to_element__(element)
        if element.get_attribute('value') == str_text:
            return 1, 'ok'
        else:
            return 0, 'Not Matched: element.text = {}, str_text = {}\n'.format(element.text, str_text)

    def select_inx(self, str_id, inx):
        '''
        Select web element by index.
        '''
        dict_arg = {}
        dict_arg['str_id'] = str_id
        dict_arg['inx'] = inx
        return self.__do_action__('select_inx', dict_arg)

    def __select_inx__(self, dict_arg):
        str_id = dict_arg['str_id']
        inx = dict_arg['inx']
        element = self._get_elm_id(str_id)
        self.__scroll_to_element__(element)
        sele = Select(element)
        sele.select_by_index(inx)

        return 1, 'ok'

    def set_yyyymmdd(self, str_id, yyyy, month, date):
        '''
        Setup the date.
        '''
        dict_arg = {}
        dict_arg['str_id'] = str_id
        dict_arg['yyyy'] = yyyy
        dict_arg['month'] = month
        dict_arg['date'] = date
        return self.__do_action__('set_yyyymmdd', dict_arg)

    def __set_yyyymmdd__(self, dict_arg):
        str_id = dict_arg['str_id']
        yyyy = dict_arg['yyyy']
        month = dict_arg['month']
        date = dict_arg['date']

        self.click_id(str_id)
        time.sleep(self.__wait_sec_calendar__)
        element = self.driver.find_element_by_class_name('ui-datepicker-year')
        sele = Select(element)
        sele.select_by_index(int(yyyy) - datetime.now().year + 90)  # idx 0 of year: current - 90

        time.sleep(self.__wait_sec_calendar__)
        element = self.driver.find_element_by_class_name('ui-datepicker-month')
        sele = Select(element)
        sele.select_by_index(int(month)-1)  # 0: 一月

        elements = self.driver.find_elements_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
        for dates in elements:
            if(dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("innerText")) == str(date)):
                dates.click()

        return 1, 'ok'

    def handle_alert_popup(self):
        '''
        Process the alert popup window.
        '''
        # wait for alert window
        # prevent:
        #  Message: unexpected alert open: {Alert text :

        _ = WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

        # accept
        alert = self.driver.switch_to_alert()
        alert.accept()

    def _get_elm_id(self, str_id):
        # https://selenium-python.readthedocs.io/waits.html
        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, str_id)) and
            EC.element_to_be_clickable((By.ID, str_id))
        )

        return element

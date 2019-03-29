import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains   # for auto scroll
import argparse

class BrowserAuto:
    WAIT_SEC = 0.2
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
        str_comm = '//*[@title="' + strTitle + '"]'
        element = self.driver.find_element_by_xpath(str_comm)
        self.scroll_to_element(element)
        element.click()


    def click_id(self, strID):
        bRun = True
        cnt = 0
        while bRun:
            try:
                if cnt > self.MAX_WAIT_CNT:
                    print('Error: cnt > self.MAX_WAIT_CNT') 
                    bRun = False
                time.sleep(self.WAIT_SEC) 
                element = self._get_elm_id(strID)
                #self.scroll_to_element(element)
                element.click()
                bRun = False
            except selenium.common.exceptions.StaleElementReferenceException as err:
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
                time.sleep(self.WAIT_SEC) 
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
            except selenium.common.exceptions.StaleElementReferenceException as err:
                print('Exception: ', err)
                print('Wait and try again')
                cnt = cnt + 1
    
    def set_yyyymmdd(self, strID, yyyy, mm, date):
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

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, strID)) and 
            EC.element_to_be_clickable((By.ID, strID))
        )
        
        return element
        

        '''
        def find(driver):
            element = driver.find_elements_by_id(strID)
            if element:
                return element
            else:
                return False
        element = WebDriverWait(self.driver, 10).until(find)
        '''


class ParkAuto:
    name_park = {}
    addr_park = 'https://npm.cpami.gov.tw/apply_1.aspx'

    id_tab_schedule = 'ContentPlaceHolder1_menu5'
    id_tab_applyer = 'ContentPlaceHolder1_menu1'
    id_tab_leader = 'ContentPlaceHolder1_menu2'
    id_tab_member = 'ContentPlaceHolder1_menu3'
    id_tab_keeper = 'ContentPlaceHolder1_menu4'

    def __init__(self, park, lst_mem):
        print('Start Taiwan National Park Automation ')
        self.park = park

        count_member = len(lst_mem)

        # team
        self.dict_team = {
            'name': 'Sloss Huang 的浪漫',
            'climbline_main_idx': 1,       # 主路線 (default idx)
            'climbline_sub_idx': 1,        # 次路線 (default idx)
            'total_day': 1,                # 總天數 (default)
            'date_applystart_idx': 1,           # 入園日期 (default idx)
            'member_count': count_member,
        }

        # member list
        self.lst_mem = lst_mem

        
        
    def run(self):
        self.browser = BrowserAuto(self.addr_park)
        switch = {  0 : self._Yushan,
                    1 : self._Taroko,
                    2 : self._Sheipa,
        }
        switch[self.park]()

        time.sleep(10) # Let the user actually see something!

    def ok(self):
        self.browser.click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self.browser.click_id('ContentPlaceHolder1_btnagree')

    def _Yushan(self):
        self.browser.click('玉山國家公園')
        self.ok()

        # 入園線上申請
        self.fill_form_schedule(self.id_tab_schedule)
        self.fill_form_applyer(self.id_tab_applyer)
        self.fill_form_leader(self.id_tab_leader)
        self.fill_form_member(self.id_tab_member)
        self.fill_form_keeper(self.id_tab_keeper)

    def _Taroko(self):
        self.browser.click('太魯閣國家公園')
        self.browser.click_id('chk[]10') # 確認已於申請前詳閱並明瞭「 錐麓古道入園收費須知」，現場購票與入園查核時間每日上午7時~上午10時止，並轉知全體隊員
        self.ok()

        # 入園線上申請
        self.fill_form_schedule(self.id_tab_schedule)
        self.fill_form_applyer(self.id_tab_applyer)
        self.fill_form_leader(self.id_tab_leader)
        self.fill_form_member(self.id_tab_member)
        self.fill_form_keeper(self.id_tab_keeper)

    def _Sheipa(self):
        self.browser.click('雪霸國家公園')
        self.browser.click_id('chk[]0') # 請申請人瞭解所填具之隊員資料與行程計畫等，如明知為不實或冒用他人資料填載入園申請之事項，將渉犯刑法第210條偽造文書罪嫌，或刑法第214條使公務員登載不實罪嫌，本處將依法先予以退件處理，並立即將申請人停權處分，另將涉案相關資料向司法機關依法告發
        self.browser.click_id('chk[]9') # 攀登路線如為B、C、C+級者，申請人及領隊應確認全體隊員均分別符合A、B、C級登山經驗能力才能申請，雪季期間另依公告辦理。
        self.ok()

        # 入園線上申請
        self.fill_form_schedule(self.id_tab_schedule)
        self.fill_form_applyer(self.id_tab_applyer)
        self.fill_form_leader(self.id_tab_leader)
        self.fill_form_member(self.id_tab_member)
        #self.fill_form_keeper(self.id_tab_keeper)



    def fill_form_schedule(self, id_tab_schedule):
        dict_team = self.dict_team
        # 路線行程規劃
        self.browser.click_id(id_tab_schedule)
        
        self.browser.fill_text('ContentPlaceHolder1_teams_name', dict_team['name']) # 隊名
        self.browser.select_inx('ContentPlaceHolder1_climblinemain', dict_team['climbline_main_idx']) # 主路線
        self.browser.select_inx('ContentPlaceHolder1_climbline', dict_team['climbline_sub_idx']) #次路線
        self.browser.select_inx('ContentPlaceHolder1_sumday', dict_team['total_day']) # 總天數
        self.browser.select_inx('ContentPlaceHolder1_applystart', dict_team['date_applystart_idx']) # 入園日期

        # the pseudo schedule: test passed for three parks
        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山登山口
        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山東峰
        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山登山口
        self.browser.click_id('ContentPlaceHolder1_btnover')   # 完成今日路線
        self.browser.select_inx('ContentPlaceHolder1_teams_count', dict_team['member_count']) # 人數
        
    def fill_form_applyer(self, id_tab_applyer):
        self.browser.click_id(id_tab_applyer)

        dict_id={}
        dict_id['id_name'] = 'ContentPlaceHolder1_apply_name'
        dict_id['id_tel'] = 'ContentPlaceHolder1_apply_tel'
        dict_id['id_contry'] = 'ContentPlaceHolder1_ddlapply_country'
        dict_id['id_city'] = 'ContentPlaceHolder1_ddlapply_city'
        dict_id['id_address'] = 'ContentPlaceHolder1_apply_addr'
        dict_id['id_mobile'] = 'ContentPlaceHolder1_apply_mobile'
        dict_id['id_fax'] = 'ContentPlaceHolder1_apply_fax'
        dict_id['id_email'] = 'ContentPlaceHolder1_apply_email'
        dict_id['id_pid_nation'] = 'ContentPlaceHolder1_apply_nation'
        dict_id['id_pid_num'] = 'ContentPlaceHolder1_apply_sid'
        dict_id['id_sex'] = 'ContentPlaceHolder1_apply_sex'
        dict_id['id_birthday'] = 'ContentPlaceHolder1_apply_birthday'
        dict_id['id_contact_name'] = 'ContentPlaceHolder1_apply_contactname'
        dict_id['id_contact_tel'] = 'ContentPlaceHolder1_apply_contacttel'

        self.browser.click_id('ContentPlaceHolder1_applycheck') # 請確認領隊或隊員同意委託申請人代理蒐集當事人個人資料，並委託其上網向國家公園管理處提出入園申請，以免違反相關法令

        # leader
        self._fill_member_detail(0, dict_id, self.lst_mem)

    def fill_form_leader(self, id_tab_leader):
        id_leader = 'ContentPlaceHolder1_copyapply'
        self.browser.click_id(id_tab_leader)
        self.browser.click_id(id_leader)
        
    def fill_form_member(self, id_tab_member):
        id_confirm = 'ContentPlaceHolder1_member_keytype' # 請確認領隊或隊員同意委託申請人代理蒐集當事人個人資料，並委託其上網向國家公園管理處提出入園申請，以免違反相關法令。
        self.browser.click_id(id_tab_member)
        self.browser.click_id(id_confirm)
        print('self.browser.driver.window_handles = ', self.browser.driver.window_handles)
        self.browser.handle_alert_popup()

        dict_id={}
        dict_id['id_name'] = 'ContentPlaceHolder1_lisMem_member_name'
        dict_id['id_tel'] = 'ContentPlaceHolder1_lisMem_member_tel'
        dict_id['id_contry'] = 'ContentPlaceHolder1_lisMem_ddlmember_country'
        dict_id['id_city'] = 'ContentPlaceHolder1_lisMem_ddlmember_city'
        dict_id['id_address'] = 'ContentPlaceHolder1_lisMem_member_addr'
        dict_id['id_mobile'] = 'ContentPlaceHolder1_lisMem_member_mobile'
        dict_id['id_email'] = 'ContentPlaceHolder1_lisMem_member_email'
        dict_id['id_pid_nation'] = 'ContentPlaceHolder1_lisMem_member_nation'
        dict_id['id_pid_num'] = 'ContentPlaceHolder1_lisMem_member_sid'
        dict_id['id_sex'] = 'ContentPlaceHolder1_lisMem_member_sex'
        dict_id['id_birthday'] = 'ContentPlaceHolder1_lisMem_member_birthday'
        dict_id['id_contact_name'] = 'ContentPlaceHolder1_lisMem_member_contactname'
        dict_id['id_contact_tel'] = 'ContentPlaceHolder1_lisMem_member_contacttel'

        lst_mem = self.lst_mem
        for i in range(1, len(lst_mem)):
            self._fill_member_detail(i, dict_id, lst_mem)
            
    def _fill_member_detail(self, i, dict_id, lst_mem):
        if i == 0:
            strIdx = ''
        else:
            strIdx = '_' + str(i - 1)
        self.browser.fill_text(dict_id['id_name']+strIdx, lst_mem[i]['id_name'])
        self.browser.fill_text(dict_id['id_tel']+strIdx, lst_mem[i]['id_tel']) # 電話
        self.browser.fill_text(dict_id['id_contry']+strIdx, lst_mem[i]['id_contry']) # contry
        self.browser.fill_text(dict_id['id_city']+strIdx, lst_mem[i]['id_city']) # city
        self.browser.fill_text(dict_id['id_address']+strIdx, lst_mem[i]['id_address']) # address
        self.browser.fill_text(dict_id['id_mobile']+strIdx, lst_mem[i]['id_mobile']) # mobile
        if  i == 0:
            self.browser.fill_text(dict_id['id_fax']+strIdx, lst_mem[i]['id_fax'])
        self.browser.fill_text(dict_id['id_email']+strIdx, lst_mem[i]['id_email']) # email
        self.browser.fill_text(dict_id['id_pid_nation']+strIdx, lst_mem[i]['id_pid_nation'])
        self.browser.fill_text(dict_id['id_pid_num']+strIdx, lst_mem[i]['id_pid_num'])
        self.browser.fill_text(dict_id['id_sex']+strIdx, lst_mem[i]['id_sex'])
        self.browser.set_yyyymmdd(dict_id['id_birthday']+strIdx, lst_mem[i]['id_birthday_yyyy'],lst_mem[i]['id_birthday_mm'],lst_mem[i]['id_birthday_dd'])
        self.browser.fill_text(dict_id['id_contact_name']+strIdx, lst_mem[i]['id_contact_name'])
        self.browser.fill_text(dict_id['id_contact_tel']+strIdx, lst_mem[i]['id_contact_tel'])

    def fill_form_keeper(self, id_tab_keeper):
        self.browser.click_id(id_tab_keeper)

def read_member_list(strFile):
    import pandas as pd
    from pandas import ExcelWriter
    from pandas import ExcelFile
    
    df = pd.read_excel('sample.xlsx', sheet_name='Sheet1')
    #print("Column headings:")
    #print(df.columns)

    list_person = []
    for i in df.index:
        dict_person = {}
        for key in df.columns:
            dict_person[key] = df[key][i]
        list_person.append(dict_person)
        #print('one person = ', dict_person)  

    return list_person


def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--park', type=int, default = 2, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")
    parser.add_argument('-list', '--memberlist', default = 'sample.xlsx', help='sample.xlsx')

    args = parser.parse_args()
    #print("args.park =", args.park)
    return 1, {'park':args.park, 'memberlist':args.memberlist}


def main():
    bValid, dict_arg = init_arg()

    lst_mem = read_member_list(dict_arg['memberlist'])

    obj_auto = ParkAuto(dict_arg['park'], lst_mem)
    obj_auto.run()
    

if __name__ == '__main__':
    main()

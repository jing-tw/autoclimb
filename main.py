import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains   # for auto scroll
import argparse

class BrowserAuto:
    def __init__(self, addr_park):
        self.addr_park= addr_park
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()
        self.driver.get(self.addr_park)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #print('scroll')

    def click(self, strTitle):
        str_comm = '//*[@title="' + strTitle + '"]'
        element = self.driver.find_element_by_xpath(str_comm)
        self.scroll_to_element(element)
        element.click()

    def click_id(self, strID):
        time.sleep(0.5) 
        element = self._get_elm_id(strID)
        #self.scroll_to_element(element)
        element.click()

    def fill_text(self, strID, strText):
        try:
            element = self._get_elm_id(strID)
            self.scroll_to_element(element)
            element.send_keys(strText)
        except selenium.common.exceptions.NoSuchElementException as reason:
            print('Exception:')
            print('strText = ', strText)
            print('reason = ', reason)
            print('result = , Keep going.')
    

    def select_inx(self, strID, inx):
        time.sleep(1)
        element = self._get_elm_id(strID)
        self.scroll_to_element(element)
        sele = Select(element)
        sele.select_by_index(inx)

    def _get_elm_id(self, strID):
        return self.driver.find_element_by_id(strID)

class ParkAuto:
    name_park = {}
    addr_park = 'https://npm.cpami.gov.tw/apply_1.aspx'

    id_tab_schedule = 'ContentPlaceHolder1_menu5'
    id_tab_applyer = 'ContentPlaceHolder1_menu1'
    id_tab_leader = 'ContentPlaceHolder1_menu2'
    id_tab_member = 'ContentPlaceHolder1_menu3'
    id_tab_keeper = 'ContentPlaceHolder1_menu4'

    def __init__(self, park, count_member):
        print('Start Taiwan National Park Automation ')
        self.park = park
        self.count_member = count_member
        
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
        self.fill_form_keeper(self.id_tab_keeper)

    def fill_form_schedule(self, id_tab_schedule):
        # 路線行程規劃
        self.browser.click_id(id_tab_schedule)
        
        self.browser.fill_text('ContentPlaceHolder1_teams_name', 'Sloss Huang 的浪漫') # 隊名
        # self.browser.fill_text('ContentPlaceHolder1_climblinemain', '其他路線') # 主路線
        self.browser.select_inx('ContentPlaceHolder1_climblinemain', 1) 
        self.browser.select_inx('ContentPlaceHolder1_climbline', 1) #次路線: C 級其他路線
        self.browser.select_inx('ContentPlaceHolder1_sumday', 1) # 總天數
        self.browser.select_inx('ContentPlaceHolder1_applystart', 1) # 入園日期

        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山登山口
        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山東峰
        self.browser.click_id('ContentPlaceHolder1_rblNode_0') # 雪山登山口
        self.browser.click_id('ContentPlaceHolder1_btnover')   # 完成今日路線
        self.browser.select_inx('ContentPlaceHolder1_teams_count', self.count_member) # 人數
        
    def fill_form_applyer(self, id_tab_applyer):
        self.browser.click_id(id_tab_applyer)

    def fill_form_leader(self, id_tab_leader):
        self.browser.click_id(id_tab_leader)

    def fill_form_member(self, id_tab_member):
        self.browser.click_id(id_tab_member)

    def fill_form_keeper(self, id_tab_keeper):
        self.browser.click_id(id_tab_keeper)



def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--park', type=int, default = 0, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")

    args = parser.parse_args()
    print("args.park =", args.park)
    return 1, {'park':args.park}


def main():
    bValid, dict_arg = init_arg()

    obj_auto = ParkAuto(dict_arg['park'], 3)
    obj_auto.run()
    

if __name__ == '__main__':
    main()
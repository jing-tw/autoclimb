import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

import argparse

class ParkAuto:
    name_park = {}
    def __init__(self, park):
        print('Start Taiwan National Park Automation ')
        self.park = park
        
    def run(self):
        # Using Chrome to access web
        self.driver = webdriver.Chrome()
        # Open the website
        self.driver.get('https://npm.cpami.gov.tw/apply_1.aspx')
        #time.sleep(1) # Let the user actually see something!

        switch = {  0 : self._Yushan,
                    1 : self._Taroko,
                    2 : self._Sheipa,
        }
        switch[self.park]()

        time.sleep(10) # Let the user actually see something!
    
    def _click(self, strTitle):
        str_comm = '//*[@title="' + strTitle + '"]'
        print('str_comm =', str_comm)
        self.driver.find_element_by_xpath(str_comm).click()

    def _click_id(self, strID):
        print(self.driver.find_element_by_id(strID))
        self._get_elm_id(strID).click()

    def _get_elm_id(self, strID):
        return self.driver.find_element_by_id(strID)

    def _fill_text(self, strID, strText):
        elm = self._get_elm_id(strID)
        elm.send_keys(strText)

    def _select_inx(self, strID, inx):
        time.sleep(1)
        elm = self._get_elm_id(strID)
        print('elm = ', elm)
        sele = Select(elm)
        sele.select_by_index(inx)

    def _Yushan(self):
        self._click('玉山國家公園')
        self._click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self._click_id('ContentPlaceHolder1_btnagree')

        # 入園線上申請

    def _Taroko(self):
        self._click('太魯閣國家公園')
        self._click_id('chk[]10') # 確認已於申請前詳閱並明瞭「 錐麓古道入園收費須知」，現場購票與入園查核時間每日上午7時~上午10時止，並轉知全體隊員
        self._click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self._click_id('ContentPlaceHolder1_btnagree')

        # 入園線上申請

    def _Sheipa(self):
        self._click('雪霸國家公園')
        self._click_id('chk[]0') # 請申請人瞭解所填具之隊員資料與行程計畫等，如明知為不實或冒用他人資料填載入園申請之事項，將渉犯刑法第210條偽造文書罪嫌，或刑法第214條使公務員登載不實罪嫌，本處將依法先予以退件處理，並立即將申請人停權處分，另將涉案相關資料向司法機關依法告發
        self._click_id('chk[]9') # 攀登路線如為B、C、C+級者，申請人及領隊應確認全體隊員均分別符合A、B、C級登山經驗能力才能申請，雪季期間另依公告辦理。
        self._click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self._click_id('ContentPlaceHolder1_btnagree')

        # 入園線上申請:  路線行程規劃
        self._fill_text('ContentPlaceHolder1_teams_name', 'Sloss Huang 的浪漫') # 隊名
        self._fill_text('ContentPlaceHolder1_climblinemain', '其他路線') # 主路線
        self._select_inx('ContentPlaceHolder1_climbline', 1) #次路線: C 級其他路線
        self._select_inx('ContentPlaceHolder1_sumday', 1) # 總天數
        
        #self._fill_text('ContentPlaceHolder1_Literal1', '共一天')
        

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--park', type=int, default = 0, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")

    args = parser.parse_args()
    print("args.park =", args.park)
    return 1, {'park':args.park}


def main():
    bValid, dict_arg = init_arg()

    obj_auto = ParkAuto(dict_arg['park'])
    obj_auto.run()
    

if __name__ == '__main__':
    main()
'''
The National Park autofill module.
'''
from datetime import datetime, timedelta
import traceback
import time
from selenium.common.exceptions import TimeoutException
from browser_auto import BrowserAuto

class EnumTabID():
    '''
    Store the National Park Tab IDs
    '''
    id_tab_schedule = 'ContentPlaceHolder1_menu5'
    id_tab_applyer = 'ContentPlaceHolder1_menu1'
    id_tab_leader = 'ContentPlaceHolder1_menu2'
    id_tab_member = 'ContentPlaceHolder1_menu3'
    id_tab_stay = 'ContentPlaceHolder1_menu4'

class TarokoPark():
    ''' 太魯閣國家公園 Class
    '''
    @staticmethod
    def is_reject():
        ''' Reject the request when condition is true.
        '''
        local_time = time.localtime()
        if local_time.tm_hour < 7 or local_time.tm_hour > 23:
            return 1, '[reject] 太魯閣國家公園: 系統開放每日7:00-23:00可進行線上申請.'
        return 0, 'pass'
class YushanPark():
    ''' 玉山國家公園 Class
    '''
    @staticmethod
    def is_reject():
        ''' Reject the request when condition is true.
        '''
        return 0, 'pass'

class SheipaPark():
    ''' 雪霸國家公園 Class
    '''
    @staticmethod
    def is_reject():
        ''' Reject the request when condition is true.
        '''
        return 0, 'pass'

class ParkAuto():
    '''
    The class for Taiwan National Park autofill.
    '''
    name_park = {}
    addr_park = 'https://npm.cpami.gov.tw/apply_1.aspx'

    def __init__(self, dict_arg, team, lst_mem, lst_stay):
        print('Start Taiwan National Park Automation ')
        self.dict_arg = dict_arg;
        self.park = dict_arg['park']
        self.auto_fill_member_list_at_start_for_demo = dict_arg['auto_fill_member_list_at_start_for_demo']
        self.wait_combox_in_sec = 0.5

        count_member = len(lst_mem)

        # team
        self.dict_team = team
        self.dict_team['member_count'] = count_member

        # member list
        self.lst_mem = lst_mem

        # stay list
        self.lst_stay = lst_stay
        self.browser = None
        self.cur_park = None

    def run(self):
        '''
        The run method.
        '''
        self.browser = BrowserAuto(self.addr_park)
        switch = {0 : self.__run_yushan__,
                  1 : self.__run__taroko__,
                  2 : self.__run__sheipa__,}
        switch[self.park]()

    def click_ok(self):
        '''
        Click ok button.
        '''
        self.browser.click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self.browser.click_id('ContentPlaceHolder1_btnagree')

    def fill_member(self, b_refilled):
        '''
        Fill member data.
        '''
        self.__fill_form_member__(EnumTabID.id_tab_member, b_refilled)

    def __apply__(self):
        self.__fill_form_schedule__(EnumTabID.id_tab_schedule)
        self.__fill_form_applyer__(EnumTabID.id_tab_applyer)
        self.__fill_form_leader__(EnumTabID.id_tab_leader)

        print('apply')
        self.fill_member(b_refilled=0)
        self.__fill_form_stay__(EnumTabID.id_tab_stay)
        self.dict_arg['WidgetMain'].notify_msgbox('Compolete', '<html> <p style="font-size:16pt">完成.<br></p> <p style="font-size:16pt">請回到瀏覽器按下一步, 檢查行程與成員資料, 沒問題後, 完成送出. <br></p></html>')        

    def __run_yushan__(self):
        self.cur_park = 'Yushan'
        self.browser.click('玉山國家公園')

        self.browser.click_id('chk[]0') # 確認已於申請前詳閱「進入玉山國家公園生態保護區申請案件個人資料運用說明」，已轉知並取得全體隊員同意使用當事人個人資料辦理入園申請相關事宜。
        self.browser.click_id('chk[]16')# 入園期間應攜帶入園許可證及身分證明文件正本俾利查核，未攜帶身分證明文件或所攜帶身分證明文件與入園許可證名冊不符者，禁止其入園。已入園者得令其離園。不聽制止或未依前段規定入園者，得依國家公園法第 19條規定處罰。
        self.browser.click_id('chk[]17')# 領隊已明確告知以下相關事項：
                                        #    1.隊伍成員如為中央流行疫情指揮中心公告之「符合通報定義」之人員(詳見:https://www.cdc.gov.tw)，應自行取消入園。
                                        #    2.隊伍成員入園前若有發燒、呼吸道不適或嚴重咳嗽者等症狀，應自行取消入園。
                                        #    3.隊伍所有成員應加強自主健康管理，入園之後如有疑似相關症狀發生，應使用口罩或足可遮掩口鼻物品進入山屋，保護自己也尊重他人。。
        self.browser.click_id('chk[]18')# 入園申請隊員若具有學生身分或參加學校社團活動，請務必自行通報學校相關單位，作為緊急應變之用。
        self.click_ok()
        self.__apply__()

    def __run__taroko__(self):
        self.cur_park = 'Taroko'
        self.browser.click('太魯閣國家公園')
        self.browser.click_id('chk[]10')# 確認已於申請前詳閱並明瞭「 錐麓古道入園收費須知」，現場購票與入園查核時間每日上午7時~上午10時止，並轉知全體隊員
        self.browser.click_id('chk[]11')# 隊伍所有成員於入園前一日皆「非」中央疫情指揮中心所公告居家隔離、居家檢疫及自主健康管理之人員。(詳見:https://www.cdc.gov.tw)。
        self.browser.click_id('chk[]12')# 入園申請隊員若具有學生身分或參加學校社團活動，請務必自行通報學校相關單位，作為緊急應變之用。
        self.click_ok()
        self.__apply__()

    def __run__sheipa__(self):
        self.cur_park = 'Sheipa'
        self.browser.click('雪霸國家公園')
        self.browser.click_id('chk[]0') # 請申請人瞭解所填具之隊員資料與行程計畫等，如明知為不實或冒用他人資料填載入園申請之事項，將渉犯刑法第210條偽造文書罪嫌，或刑法第214條使公務員登載不實罪嫌，本處將依法先予以退件處理，並立即將申請人停權處分，另將涉案相關資料向司法機關依法告發
        self.browser.click_id('chk[]9') # 攀登路線如為B、C、C+級者，申請人及領隊應確認全體隊員均分別符合A、B、C級登山經驗能力才能申請，雪季期間另依公告辦理。
        self.browser.click_id('chk[]10')# 欲申請雪山西稜線之隊伍，請於申請前詳閱230林道注意事項
        self.browser.click_id('chk[]11')# 單人獨攀通知: 單人獨攀隊伍(者)應確實規劃登山計畫與風險評估，包含宿營地點.時間. 糧食. 飲水與裝備等， 並辦妥登山或旅遊保險，且攜帶衛星電話、GPS或有效之定位器材。另請依照路線地形審酌攜帶確保繩及安全頭盔等特殊裝備。獨攀者應定期向留守人作安全回報(留守人必須是有效留守)， 如本人未依登山計畫時間下山，也已交代留守人於第一時間通知管理處或消防單位以確保救援時效
        self.browser.click_id('chk[]12')# 隊伍所有成員於入園前一日皆「非」中央疫情指揮中心所公告居家隔離、居家檢疫及自主健康管理之人員。(詳見:https://www.cdc.gov.tw)。
        self.click_ok()
        self.__apply__()

    def __fill_form_schedule__(self, id_tab_schedule):
        dict_team = self.dict_team
        # 路線行程規劃
        if self.cur_park != 'Taroko':
            self.browser.fill_text('ContentPlaceHolder1_teams_name', dict_team['name'] + datetime.now().strftime("%Y%m%d%H%M%S"), 0) # 隊名
            self.browser.sleep(1); # wait for server checking/response the team name.
        
        id_next_step = 'ContentPlaceHolder1_btnToStep22'

        str_infix = '_'
        id_climbline_main = 'ContentPlaceHolder1'+str_infix+'climblinemain'
        if self.cur_park == 'Taroko':
            str_infix = '_step1_'
            id_climbline_main = 'climblinemain'
            id_next_step = 'ContentPlaceHolder1_step1_bt_Next_D'

        if self.cur_park == 'Sheipa':
            id_next_step = 'ContentPlaceHolder1_btnstepdown'

        id_climbline_sub = 'ContentPlaceHolder1'+str_infix+'climbline'
        id_sum_day = 'ContentPlaceHolder1'+str_infix+'sumday'
        id_date_applystart = 'ContentPlaceHolder1'+str_infix+'applystart'

        self.browser.select_inx(id_climbline_main, dict_team['climbline_main_idx']) # 主路線
        self.browser.sleep(1); # wait for server checking/response the team name.
        self.browser.select_inx(id_climbline_sub, dict_team['climbline_sub_idx']) #次路線
        self.browser.sleep(1); # wait for server checking/response the team name.
        self.browser.select_inx(id_sum_day, dict_team['total_day']) # 總天數

        if self.cur_park == 'Taroko':
            self.browser.click_id('ContentPlaceHolder1_step1_noteCheck_CheckBox') # 奇萊主北線與奇萊連峰線為共同承載量(平日40人、假日60人)。自109年2月21日零時起免辦入山許可證。
                                                                                  # 依中央流行疫情指揮中心及營建署「國家公園區域因應COVID-19疫情警戒第2級之遊憩人流出入管制措施」指引，自8/10日至8/23日生態保護區內各登山路線依平日承載量降載開放。
        try:
            date_applystart_idx = (datetime.strptime(dict_team['date_applystart'], '%Y-%m-%d') - (datetime.now() + timedelta(4))).days + 1 # 入園日期
        except Exception as ex:
            print(ex)
            date_applystart_idx = 1 # 入園日期 (default idx = 1)
        print('date_applystart_idx: ', date_applystart_idx)
        self.browser.select_inx(id_date_applystart, date_applystart_idx)

        # Create pseudo travel plan
        if self.cur_park == 'Yushan':
            # Pseudo Plan: 登山口排雲登山服務中心→登山口塔塔加登山口→一般玉山前峰→登山口塔塔加登山口→登山口排雲登山服務中心
            print('Use default')

        if self.cur_park == 'Taroko':
            # Pseudo Plan: 登山口奇萊登山口→宿營地黑水塘山屋→登山口奇萊登山口
            self.browser.click_id('ContentPlaceHolder1_step1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_step1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_step1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_step1_btnover') # 完成今日路線
            print('Use default')

        if self.cur_park == 'Sheipa':
            # Pseudo Plan: 雪山登山口→雪山東峰→雪山登山口
            self.browser.click_id('ContentPlaceHolder1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_rblNode_0')
            self.browser.click_id('ContentPlaceHolder1_btnover') # 完成今日路線
            print('Use default')

        self.dict_arg['WidgetMain'].notify_msgbox('Edit', '<html> <p style="font-size:16pt">Step 1: 請開始編修你的行程：主路線, 次路線, 登山總日數, 入園日期, 路線規劃.<br></p> <p style="font-size:16pt">Step 2: 完成後回到此視窗按 OK. <br></p><p>程式會自動繼續幫你填寫隊員資料. <br></p></html>');
        self.browser.click_id(id_next_step) # new: [下一步] button

    def __fill_form_applyer__(self, id_tab_applyer):
        id_applycheck = 'ContentPlaceHolder1_applycheck'
        str_infix = '_';
        if self.cur_park == 'Taroko':
            str_infix = '_step2_'
        id_applycheck = 'ContentPlaceHolder1'+str_infix+'applycheck'

        self.browser.click_id('headingOne') # open '申請人資料' collapse
        self.browser.click_id(id_applycheck) # 請確認領隊或隊員同意委託申請人代理蒐集當事人個人資料，並委託其上網向國家公園管理處提出入園申請，以免違反相關法令

        dict_id = {}
        dict_id['id_name'] = 'ContentPlaceHolder1'+str_infix+'apply_name'
        dict_id['id_tel'] = 'ContentPlaceHolder1'+str_infix+'apply_tel'
        dict_id['id_country'] = 'ContentPlaceHolder1'+str_infix+'ddlapply_country'
        dict_id['id_city'] = 'ContentPlaceHolder1'+str_infix+'ddlapply_city'
        dict_id['id_address'] = 'ContentPlaceHolder1'+str_infix+'apply_addr'
        dict_id['id_mobile'] = 'ContentPlaceHolder1'+str_infix+'apply_mobile'
        dict_id['id_fax'] = 'ContentPlaceHolder1'+str_infix+'apply_fax'
        dict_id['id_email'] = 'ContentPlaceHolder1'+str_infix+'apply_email'
        dict_id['id_pid_nation'] = 'ContentPlaceHolder1'+str_infix+'apply_nation'
        dict_id['id_pid_num'] = 'ContentPlaceHolder1'+str_infix+'apply_sid'
        dict_id['id_sex'] = 'ContentPlaceHolder1'+str_infix+'apply_sex'
        dict_id['id_birthday'] = 'ContentPlaceHolder1'+str_infix+'apply_birthday'
        dict_id['id_contact_name'] = 'ContentPlaceHolder1'+str_infix+'apply_contactname'
        dict_id['id_contact_tel'] = 'ContentPlaceHolder1'+str_infix+'apply_contacttel'

        # leader
        self.__fill_member_detail__(0, dict_id, self.lst_mem, 0, False)

        # # verify
        # self.browser.click_id(id_tab_applyer)
        # ok, set_failure_key, msg = self.__fill_member_detail_verify__(0, dict_id, self.lst_mem)

    def __fill_form_leader__(self, id_tab_leader):
        str_infix = '_';
        if self.cur_park == 'Taroko':
            str_infix = '_step2_'

        self.browser.click_id('headingTwo') # Open '領隊資料' collapse
        id_leader = 'ContentPlaceHolder1'+str_infix+'copyapply'
        self.browser.click_id(id_leader) # The same as the "applyer"

    def __fill_form_member__(self, id_tab_member, b_refilled):
        id_add_member = 'ContentPlaceHolder1_lbInsMember'
        str_infix = '_';
        if self.cur_park == 'Taroko':
            str_infix = '_step2_'
            id_add_member = 'ContentPlaceHolder1_step2_addmember'

        if self.cur_park == 'Sheipa':
            id_add_member = 'ContentPlaceHolder1_addmember'

        self.browser.click_id('headingThree') # Open '隊員資料' collapse
        id_confirm = 'ContentPlaceHolder1'+str_infix+'member_keytype' # 請確認領隊或隊員同意委託申請人代理蒐集當事人個人資料，並委託其上網向國家公園管理處提出入園申請，以免違反相關法令。
        if self.browser.get_attribute('checked', id_confirm) != 'true':
            self.browser.click_id(id_confirm)
            print('self.browser.driver.window_handles = ', self.browser.driver.window_handles)
            self.browser.handle_alert_popup()

        dict_id = {}
        dict_id['id_name'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_name'
        dict_id['id_tel'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_tel'
        dict_id['id_country'] = 'ContentPlaceHolder1'+str_infix+'lisMem_ddlmember_country'
        dict_id['id_city'] = 'ContentPlaceHolder1'+str_infix+'lisMem_ddlmember_city'
        dict_id['id_address'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_addr'
        dict_id['id_mobile'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_mobile'
        dict_id['id_email'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_email'
        dict_id['id_pid_nation'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_nation'
        dict_id['id_pid_num'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_sid'
        dict_id['id_sex'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_sex'
        dict_id['id_birthday'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_birthday'
        dict_id['id_contact_name'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_contactname'
        dict_id['id_contact_tel'] = 'ContentPlaceHolder1'+str_infix+'lisMem_member_contacttel'

        lst_mem = self.lst_mem
        for i in range(1, len(lst_mem)):
            time.sleep(self.wait_combox_in_sec)
            self.browser.click_id(id_add_member) # Click '新增隊員'
            if self.cur_park == 'Taroko' or self.cur_park == 'Sheipa':
                self.browser.click_by_xpath('//*[@id="accordion2"]/div[' + str(i) + ']/div[1]/h4/a[1]')
            self.__fill_member_detail__(i, dict_id, lst_mem, b_refilled, True)

        # # verify
        # for i in range(1, len(lst_mem)):
        #     ok, set_failure_key, msg = self.__fill_member_detail_verify__(i, dict_id, self.lst_mem)

    def __fill_member_detail__(self, i, dict_id, lst_mem, b_refilled, b_fill_member):
        self.browser.speed_up()
        if i == 0:
            str_idx = ''
        else:
            str_idx = '_' + str(i - 1)
        self.browser.fill_text(dict_id['id_name']+str_idx, lst_mem[i]['id_name'], b_refilled)
        self.browser.fill_text(dict_id['id_tel']+str_idx, lst_mem[i]['id_tel'], b_refilled) # 電話
        self.browser.fill_text(dict_id['id_country']+str_idx, lst_mem[i]['id_country'], b_refilled) # contry
        time.sleep(self.wait_combox_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去

        if b_fill_member:
            if self.cur_park == 'Yushan':
                self.browser.click_id('headingThree') # [Server Bug?] Open '隊員資料' collapse
            
            if self.cur_park == 'Taroko':
                self.browser.click_id('headingThree') # [Server Bug?] Open '隊員資料' collapse
                if i == 1: #[Server Bug?] 隊員資料未展開
                    self.browser.click_by_xpath('//*[@id="accordion2"]/div/div[1]/h4/a[1]')
                else:
                    self.browser.click_by_xpath('//*[@id="accordion2"]/div[' + str(i) + ']/div[1]/h4/a[1]')

        self.browser.fill_text(dict_id['id_city']+str_idx, lst_mem[i]['id_city'], b_refilled) # city
        time.sleep(self.wait_combox_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去
        self.browser.fill_text(dict_id['id_address']+str_idx, lst_mem[i]['id_address'], b_refilled) # address
        self.browser.fill_text(dict_id['id_mobile']+str_idx, lst_mem[i]['id_mobile'], b_refilled) # mobile
        if  i == 0:
            self.browser.fill_text(dict_id['id_fax']+str_idx, lst_mem[i]['id_fax'], b_refilled)
        self.browser.fill_text(dict_id['id_email']+str_idx, lst_mem[i]['id_email'], b_refilled) # email
        self.browser.fill_text(dict_id['id_pid_nation']+str_idx, lst_mem[i]['id_pid_nation'], b_refilled)
        time.sleep(self.wait_combox_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去

        if  b_fill_member and self.cur_park == 'Yushan':
            self.browser.click_id('headingThree') # [Server Render Bug?]  Open '隊員資料' collapse

        self.browser.fill_text(dict_id['id_pid_num']+str_idx, lst_mem[i]['id_pid_num'], b_refilled)
        self.browser.fill_text(dict_id['id_sex']+str_idx, lst_mem[i]['id_sex'], b_refilled)
        self.browser.set_yyyymmdd(dict_id['id_birthday']+str_idx, lst_mem[i]['id_birthday_yyyy'], lst_mem[i]['id_birthday_mm'], lst_mem[i]['id_birthday_dd'])
        self.browser.fill_text(dict_id['id_contact_name']+str_idx, lst_mem[i]['id_contact_name'], b_refilled)
        self.browser.fill_text(dict_id['id_contact_tel']+str_idx, lst_mem[i]['id_contact_tel'], b_refilled)
        self.browser.speed_init()

        return 1, 'ok'

    def __fill_member_detail_verify__(self, i, dict_id, lst_mem):
        self.browser.speed_up()
        if i == 0:
            str_idx = ''
        else:
            str_idx = '_' + str(i - 1)

        # verify
        print('Verifyin the content ...')
        lst_key_fill_text = ['id_name', 'id_tel', 'id_address', 'id_mobile', 'id_email', 'id_pid_nation', 'id_pid_num', 'id_sex', 'id_contact_name', 'id_contact_tel']
        b_ok = 1
        msg = 'ok'
        set_failure_key = set()

        try_num = 0
        restart = 1
        while restart:
            item_len = len(lst_key_fill_text)
            for j in range(0, item_len):
                str_key = lst_key_fill_text[j]
                if j == item_len - 1 or try_num > 5:
                    restart = 0
                b_ok, msg = self.browser.fill_text_verify(dict_id[str_key]+str_idx, lst_mem[i][str_key])
                if not b_ok:
                    msg = '{} checked, failure.\nmsg = {}'.format(str_key, msg)
                    b_ok = 0
                    print(msg)
                    set_failure_key.add(str_key)

                    print('try again... str_key = {}, data = {}'.format(str_key, lst_mem[i][str_key]))
                    time.sleep(2)
                    try:
                        self.browser.fill_text(dict_id[str_key]+str_idx, lst_mem[i][str_key], 1)
                    except TimeoutException as err:

                        traceback.print_exc()
                        print('Exception: ' + str(err))

                    try_num = try_num + 1
                    j = j - 1
                    continue
                print('--------------------> {} checked, {} pass.'.format(str_key, lst_mem[i][str_key]))

        self.browser.speed_init()
        return b_ok, set_failure_key, msg

    def __fill_form_stay__(self, id_tab_stay):
        str_infix = '_';
        if self.cur_park == 'Taroko':
            str_infix = '_step2_'

        self.browser.click_id('headingFour') # Open '留守人' collapse
        # self.browser.click_id(id_tab_stay)

        dict_id = {}
        pre = 'ContentPlaceHolder1' + str_infix +'stay'
        dict_id['id_name'] = pre + '_name'
        dict_id['id_tel'] = pre + '_tel'
        dict_id['id_mobile'] = pre + '_mobile'
        dict_id['id_email'] = pre + '_email'

        self.browser.speed_up()
        lst_mem = self.lst_stay
        i = 0
        self.browser.fill_text(dict_id['id_name'], lst_mem[i]['id_name'], 0)
        if self.cur_park != 'Yushan':
            self.browser.fill_text(dict_id['id_tel'], lst_mem[i]['id_tel'], 0) # 電話
        self.browser.fill_text(dict_id['id_mobile'], lst_mem[i]['id_tel'], 0) # 手機
        self.browser.fill_text(dict_id['id_email'], lst_mem[i]['id_email'], 0) # email

        self.browser.speed_init()

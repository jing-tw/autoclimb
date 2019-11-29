
import time
from browser_auto import BrowserAuto

class ParkAuto:
    name_park = {}
    addr_park = 'https://npm.cpami.gov.tw/apply_1.aspx'

    id_tab_schedule = 'ContentPlaceHolder1_menu5'
    id_tab_applyer = 'ContentPlaceHolder1_menu1'
    id_tab_leader = 'ContentPlaceHolder1_menu2'
    id_tab_member = 'ContentPlaceHolder1_menu3'
    id_tab_stay = 'ContentPlaceHolder1_menu4'

    def __init__(self, dict_arg, lst_mem, lst_stay):
        print('Start Taiwan National Park Automation ')
        self.park = dict_arg['park']
        self.auto_fill_member_list_at_start_for_demo = dict_arg['auto_fill_member_list_at_start_for_demo']
        self.WAIT_COMBOX_in_sec = 0.5

        count_member = len(lst_mem)

        # team
        self.dict_team = {
            'name': '平安喜樂開心',
            'climbline_main_idx': 1,       # 主路線 (default idx)
            'climbline_sub_idx': 1,        # 次路線 (default idx)
            'total_day': 1,                # 總天數 (default)
            'date_applystart_idx': 1,           # 入園日期 (default idx)
            'member_count': count_member,
        }

        # member list
        self.lst_mem = lst_mem

        # stay list
        self.lst_stay = lst_stay

    def run(self):
        self.browser = BrowserAuto(self.addr_park)
        switch = {  0 : self._Yushan,
                    1 : self._Taroko,
                    2 : self._Sheipa,
        }
        switch[self.park]()

        #time.sleep(10) # Let the user actually see something!

    def ok(self):
        self.browser.click_id('chk[]')  # 本人已閱讀並充分瞭解上述注意事項，並會遵守國家公園各項規定
        self.browser.click_id('ContentPlaceHolder1_btnagree')

    def run_fill_form_member(self, b_refilled):
        self.fill_form_member(self.id_tab_member, b_refilled)

    def apply(self):
        self.fill_form_schedule(self.id_tab_schedule)
        self.fill_form_applyer(self.id_tab_applyer)
        self.fill_form_leader(self.id_tab_leader)

        print('apply')
        if self.auto_fill_member_list_at_start_for_demo:
            self.run_fill_form_member(b_refilled=0)

        self.fill_form_stay(self.id_tab_stay)


    def _Yushan(self):
        self.curPark = 'Yushan'
        self.browser.click('玉山國家公園')
        self.ok()
        self.apply()

    def _Taroko(self):
        self.curPark = 'Taroko'
        self.browser.click('太魯閣國家公園')
        self.browser.click_id('chk[]10') # 確認已於申請前詳閱並明瞭「 錐麓古道入園收費須知」，現場購票與入園查核時間每日上午7時~上午10時止，並轉知全體隊員
        self.ok()
        self.apply()

    def _Sheipa(self):
        self.curPark = 'Sheipa'
        self.browser.click('雪霸國家公園')
        self.browser.click_id('chk[]0') # 請申請人瞭解所填具之隊員資料與行程計畫等，如明知為不實或冒用他人資料填載入園申請之事項，將渉犯刑法第210條偽造文書罪嫌，或刑法第214條使公務員登載不實罪嫌，本處將依法先予以退件處理，並立即將申請人停權處分，另將涉案相關資料向司法機關依法告發
        self.browser.click_id('chk[]9') # 攀登路線如為B、C、C+級者，申請人及領隊應確認全體隊員均分別符合A、B、C級登山經驗能力才能申請，雪季期間另依公告辦理。
        self.browser.click_id('chk[]10')# 單人獨攀通知: 單人獨攀隊伍(者)應確實規劃登山計畫與風險評估，包含宿營地點.時間. 糧食. 飲水與裝備等， 並辦妥登山或旅遊保險，且攜帶衛星電話、GPS或有效之定位器材。另請依照路線地形審酌攜帶確保繩及安全頭盔等特殊裝備。獨攀者應定期向留守人作安全回報(留守人必須是有效留守)， 如本人未依登山計畫時間下山，也已交代留守人於第一時間通知管理處或消防單位以確保救援時效
        self.ok()
        self.apply()

    def fill_form_schedule(self, id_tab_schedule):
        dict_team = self.dict_team
        # 路線行程規劃
        self.browser.click_id(id_tab_schedule)

        if self.curPark != 'Taroko':
            self.browser.fill_text('ContentPlaceHolder1_teams_name', dict_team['name'], 0) # 隊名
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
        dict_id['id_country'] = 'ContentPlaceHolder1_ddlapply_country'
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
        self._fill_member_detail(0, dict_id, self.lst_mem, 0)

        # # verify
        # self.browser.click_id(id_tab_applyer)
        # ok, set_failure_key, msg = self._fill_member_detail_verify(0, dict_id, self.lst_mem)

    def fill_form_leader(self, id_tab_leader):
        id_leader = 'ContentPlaceHolder1_copyapply'
        self.browser.click_id(id_tab_leader)
        self.browser.click_id(id_leader)

    def fill_form_member(self, id_tab_member, b_refilled):
        id_confirm = 'ContentPlaceHolder1_member_keytype' # 請確認領隊或隊員同意委託申請人代理蒐集當事人個人資料，並委託其上網向國家公園管理處提出入園申請，以免違反相關法令。
        self.browser.click_id(id_tab_member)

        if self.browser.get_attribute('checked', id_confirm) != 'true':
            self.browser.click_id(id_confirm)
            print('self.browser.driver.window_handles = ', self.browser.driver.window_handles)
            self.browser.handle_alert_popup()

        dict_id={}
        dict_id['id_name'] = 'ContentPlaceHolder1_lisMem_member_name'
        dict_id['id_tel'] = 'ContentPlaceHolder1_lisMem_member_tel'
        dict_id['id_country'] = 'ContentPlaceHolder1_lisMem_ddlmember_country'
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
            self._fill_member_detail(i, dict_id, lst_mem, b_refilled)

        # # verify
        # for i in range(1, len(lst_mem)):
        #     ok, set_failure_key, msg = self._fill_member_detail_verify(i, dict_id, self.lst_mem)

    def _fill_member_detail(self, i, dict_id, lst_mem, b_refilled):
        self.browser.speed_up()
        if i == 0:
            strIdx = ''
        else:
            strIdx = '_' + str(i - 1)
        self.browser.fill_text(dict_id['id_name']+strIdx, lst_mem[i]['id_name'], b_refilled)
        self.browser.fill_text(dict_id['id_tel']+strIdx, lst_mem[i]['id_tel'], b_refilled) # 電話
        self.browser.fill_text(dict_id['id_country']+strIdx, lst_mem[i]['id_country'], b_refilled) # contry
        time.sleep(self.WAIT_COMBOX_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去
        self.browser.fill_text(dict_id['id_city']+strIdx, lst_mem[i]['id_city'], b_refilled) # city
        time.sleep(self.WAIT_COMBOX_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去
        self.browser.fill_text(dict_id['id_address']+strIdx, lst_mem[i]['id_address'], b_refilled) # address
        self.browser.fill_text(dict_id['id_mobile']+strIdx, lst_mem[i]['id_mobile'], b_refilled) # mobile
        if  i == 0:
            self.browser.fill_text(dict_id['id_fax']+strIdx, lst_mem[i]['id_fax'], b_refilled)
        self.browser.fill_text(dict_id['id_email']+strIdx, lst_mem[i]['id_email'], b_refilled) # email
        self.browser.fill_text(dict_id['id_pid_nation']+strIdx, lst_mem[i]['id_pid_nation'], b_refilled)
        time.sleep(self.WAIT_COMBOX_in_sec) # 因為前面是下拉, 所以要等一下, 讓下拉收回去
        self.browser.fill_text(dict_id['id_pid_num']+strIdx, lst_mem[i]['id_pid_num'], b_refilled)
        self.browser.fill_text(dict_id['id_sex']+strIdx, lst_mem[i]['id_sex'], b_refilled)
        self.browser.set_yyyymmdd(dict_id['id_birthday']+strIdx, lst_mem[i]['id_birthday_yyyy'],lst_mem[i]['id_birthday_mm'],lst_mem[i]['id_birthday_dd'])
        self.browser.fill_text(dict_id['id_contact_name']+strIdx, lst_mem[i]['id_contact_name'], b_refilled)
        self.browser.fill_text(dict_id['id_contact_tel']+strIdx, lst_mem[i]['id_contact_tel'], b_refilled)
        self.browser.speed_init()

        return 1, 'ok'

    def _fill_member_detail_verify(self, i, dict_id, lst_mem):
        self.browser.speed_up()
        if i == 0:
            strIdx = ''
        else:
            strIdx = '_' + str(i - 1)

        # verify
        print('Verifyin the content ...')
        lst_key_fill_text = ['id_name', 'id_tel', 'id_address', 'id_mobile', 'id_email', 'id_pid_nation', 'id_pid_num', 'id_sex', 'id_contact_name', 'id_contact_tel']
        ok = 1; msg = 'ok'
        set_failure_key = set()

        try_num = 0
        restart = 1
        while restart:
            item_len = len(lst_key_fill_text)
            for ii in range(0, item_len):
                str_key = lst_key_fill_text[ii]
                if ii == item_len - 1 or try_num > 5:
                    restart = 0
                ok, msg = self.browser.fill_text_verify(dict_id[str_key]+strIdx, lst_mem[i][str_key])
                if not ok:
                    msg = '{} checked, failure.\nmsg = '.format(str_key, msg)
                    ok = 0
                    print(msg)
                    set_failure_key.add(str_key)

                    print('try again... str_key = {}, data = {}'.format(str_key, lst_mem[i][str_key]))
                    time.sleep(2)
                    try:
                        self.browser.fill_text(dict_id[str_key]+strIdx, lst_mem[i][str_key], 1)
                    except TimeoutException as e:
                        import traceback
                        traceback.print_exc()
                        print('Exception: ' + str(e))

                    try_num = try_num + 1
                    ii = ii - 1
                    continue

                else:
                    print('--------------------> {} checked, {} pass.'.format(str_key, lst_mem[i][str_key]))

        self.browser.speed_init()
        return ok, set_failure_key, msg

    def fill_form_stay(self, id_tab_stay):
        self.browser.click_id(id_tab_stay)

        dict_id={}
        pre = 'ContentPlaceHolder1' + '_stay'
        dict_id['id_name'] = pre + '_name'
        dict_id['id_mobile'] = pre + '_mobile'
        dict_id['id_email'] = pre + '_email'

        self.browser.speed_up()
        lst_mem = self.lst_stay
        i = 0
        self.browser.fill_text(dict_id['id_name'], lst_mem[i]['id_name'], 0)
        self.browser.fill_text(dict_id['id_mobile'], lst_mem[i]['id_tel'], 0) # 電話
        self.browser.fill_text(dict_id['id_email'], lst_mem[i]['id_email'], 0) # email

        self.browser.speed_init()

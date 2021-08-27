'''
The main module to run auto fill data progrom.
'''
import sys
import subprocess
import traceback


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from ui_button import PicButton
from park_auto import ParkAuto
from park_auto import TarokoPark, YushanPark, SheipaPark
from autotest_layer_widget import AutoTestLayerWidget
from utility_io import util_read_data_xlsx, utl_read_data

PROG_NAME = 'autoclimb.py'
DEFAULT_GUI = 1
DEFAULT_PARK = 2
DEFAULT_MEMBERLIST = 'sample.xlsx'

class AutoClimbWidget(AutoTestLayerWidget):
    '''The main window widget.
    '''
    def __init__(self):
        super().__init__(None)
        self.obj_auto = None
        #self.bt_fill_member = None
        self.text_status = None
        self.dict_arg = None

    def __init_ui__(self):
        # add button
        bt_yushan = PicButton(QPixmap('./res/img/Yushan.png'))
        bt_taroko = PicButton(QPixmap('./res/img/Taroko.png'))
        bt_sheipa = PicButton(QPixmap('./res/img/Sheipa.png'))
        #self.bt_fill_member = PicButton(QPixmap('./res/img/member_auto.png'))

        self.autotest_add(bt_yushan, 'bt_yushan')
        self.autotest_add(bt_taroko, 'bt_taroko')
        self.autotest_add(bt_sheipa, 'bt_sheipa')

        # add status label
        self.text_status = QLabel("Status")
        self.text_status.setAlignment(QtCore.Qt.AlignCenter)
        font = self.text_status.font()
        font.setPointSize(14)
        self.text_status.setFont(font)

        # layout: upper
        box_button = QtWidgets.QHBoxLayout()
        box_button.addStretch(1)
        box_button.addWidget(bt_yushan)
        box_button.addWidget(bt_taroko)
        box_button.addWidget(bt_sheipa)
        # layouer: middle
        box_button2 = QtWidgets.QHBoxLayout()
        box_button2.addStretch(1)
        #box_button2.addWidget(self.bt_fill_member)
        #self.bt_fill_member.setVisible(False)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(box_button)
        self.layout.addLayout(box_button2)
        self.layout.addWidget(self.text_status)
        self.setLayout(self.layout)

        bt_yushan.clicked.connect(self.__run_yushan__)
        bt_taroko.clicked.connect(self.__run_taroko__)
        bt_sheipa.clicked.connect(self.__run_sheipa__)
        #self.bt_fill_member.clicked.connect(self.__run_fill_member__) # re-fill the member data

        self.dict_arg = {}
        self.dict_arg['memberlist'] = DEFAULT_MEMBERLIST
        self.dict_arg['park'] = DEFAULT_PARK
        self.dict_arg['auto_fill_member_list_at_start_for_demo'] = False
        self.dict_arg['ui'] = self
        self.__loc_center__()

        self.text_status.setText('正在檢查版本 ...')
        QtCore.QTimer.singleShot(200, self.__check_version__)

    def __set_window_title__(self, strversion):
        self.setWindowTitle(PROG_NAME + '(commit id): ' + strversion)

    def __check_version__(self):
        ret, desc, local_id = __check_update__()
        if ret == 0:
            return
        out = desc + '<div align=\"left\">' + \
                     '版本號碼:' + local_id.decode("utf-8").rstrip() + '.</div>'
        print(out)
        self.text_status.setText(out)
        _ = QMessageBox.question(self, '訊息', \
                     '<html> <p style="font-size:16pt"> ' + desc + '</p></html>', QMessageBox.Ok)

    def __run_fill_member__(self):
        if self.obj_auto is not None:
            if self.dict_arg['auto_fill_member_list_at_start_for_demo']:
                self.obj_auto.fill_member(b_refilled=1)
            else:
                self.obj_auto.fill_member(b_refilled=0)

    def __update_status__(self, str_status):
        print(str_status)
        self.text_status.setText(str_status)

    def __run_yushan__(self):
        b_reject, msg = YushanPark.is_reject()
        if b_reject:
            self.__show_reject_message__(msg)
            return
        self.__update_status__('玉山國家公園')
        self.dict_arg['park'] = 0
        self.run()

    def __run_taroko__(self):
        b_reject, msg = TarokoPark.is_reject()
        if b_reject:
            self.__show_reject_message__(msg)
            return
        self.__update_status__('太魯閣國家公園')
        self.dict_arg['park'] = 1
        self.run()

    def __run_sheipa__(self):
        b_reject, msg = SheipaPark.is_reject()
        if b_reject:
            self.__show_reject_message__(msg)
            return
        self.__update_status__('雪霸國家公園')
        self.dict_arg['park'] = 2
        self.run()

    def run(self):
        '''Execute the auto fill procedure.
        '''
        try:
            b_ok, filename, msg = self.__get_filename__()
            if not b_ok:
                print(msg)
                return
            self.dict_arg['memberlist'] = filename

            # for old data file that has no 'team' sheet in the file.
            dict_team_default = {
                'name': 'Lemna 快樂登山隊',
                'climbline_main_idx': 1,       # 主路線 (default idx)
                'climbline_sub_idx': 1,        # 次路線 (default idx)
                'total_day': 1,                # 總天數 (default)
                'date_applystart_idx': 1,      # 入園日期 (default idx)
                'member_count': 0 # the value will be filled, later.
            }

            lst_dict_meta_default = list()
            lst_dict_meta_default.append({'item': 'version', 'value': 'v0.0.0'}) # default version for the data formation

            b_ok, team, lst_mem, lst_stay, lst_meta = utl_read_data(self.dict_arg['memberlist'], dict_team_default, lst_dict_meta_default)
            if not b_ok:
                print('Error: utl_read_data failure')
                return

            print('資料檔格式資訊\n\t{} : {}'.format(lst_meta[0]['item'], lst_meta[0]['value'])) # 資料檔版本資訊 index = 0
            self.dict_arg['WidgetMain'] = self;
            self.obj_auto = ParkAuto(self.dict_arg, team, lst_mem, lst_stay)
            self.obj_auto.run()

            # Todo: remove bt_fill_member
            # show re-fill member button only when obj_auto_run exist
            # self.bt_fill_member.setVisible(True)
            # self.__update_status__('完成. <br> 右側按鈕: 可以自動填入隊員資料')

            self.activateWindow()  # show the control panel
            # self.__ack_continue_fill_schedule__()
        except Exception as err:
            traceback.print_exc()
            msg = '\n\n查閱上方錯誤訊息, 進行檢測.\n\n1.請確定你的機器是否連上網際網路\n2.瀏覽器是否已經被關閉了\n3.有可能是瀏覽器版本太舊了, 請更新你的瀏覽器版本.\n4.若前面都檢查過, 那可能是其他問題, 請複製上方錯誤資訊 call stack 發出 error issue 到 github.\n\nDetail:{}'.format(format(err))
            print(msg)
            msg = '更新 Chrome 最新版本的指令:\nUbuntu:\n{}'.format('sudo apt-get --only-upgrade install google-chrome-stable')
            print(msg)
            return

    def __show_reject_message__(self, msg):
        self.__update_status__(msg)
        self.__notify_message__('條件不足無法自動填寫', msg)

    def __notify_message__(self, str_line1, str_line2):
        reply = QMessageBox.question(self, '訊息', \
                    '<html> <p style="font-size:16pt">{} <br>{} </p></html>'.format(str_line1, str_line2), \
                    QMessageBox.Ok)
        return reply

    def notify_msgbox(self, str_title, str_content):
        reply = QMessageBox.question(None, str_title, str_content, QMessageBox.Ok)
        return reply

    def __ack_continue_fill_schedule__(self):
        reply = QMessageBox.question(self, '你可以開始動手編輯團隊登山行程', \
                    '<html> <p style="font-size:16pt">隊員資料自動填寫完成. 請編修你的登山行程<br></p><p style="font-size:16pt">Step 1. 回到瀏覽器視窗<br></p><p style="font-size:16pt">Step 2.切到 [行程] 頁面, 修改自己的行程.<br></p><p style="font-size:16pt">Step 3. 點選下面 [自動填入成員資料] 按鈕<br></p></html>', \
                    QMessageBox.Ok)
        return reply

    def __get_filename__(self):
        print('load')
        lst_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.', '*.xlsx')
        if lst_filename:
            print(lst_filename[0])
            return 1, lst_filename[0], 'ok'
        return 0, None, '[Warning] getOpenFileName Failure or Cancel.'

    def __loc_center__(self):
        screen_geo = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        loc_x = screen_geo.width()/2 - widget.width()/2 + screen_geo.width()/6
        loc_y = screen_geo.height()/2 - widget.height()/2
        self.move(int(loc_x), int(loc_y))

def __check_update__():
    # ref: https://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git
    try:
        print('checking version ...')
        subprocess.check_output('git fetch'.split())  # update ref
        local = subprocess.check_output('git rev-parse @'.split()) # return local HEAD id
        remote = subprocess.check_output('git rev-parse @{u}'.split()) # return remote HEAD id
        comm_base = subprocess.check_output('git merge-base @ @{u}'.split()) # return comm id

        if local == remote:
            desc = '<div align=\"left\"><br>狀態: 目前是最新版.</div>'
            return 0, desc, local
        if local == comm_base:
            desc = '<div align=\"left\">版本檢查結果<br>這個工具已經有新版本發布, 請到命令列執行 git pull 更新.</div>'
            return 1, desc, local

        if remote == comm_base:
            desc = '<div align=\"left\">版本檢查結果<br>狀態: Local changed. Require git push.</div>'
            return 2, desc, local

        desc = '<div align=\"left\">版本檢查結果<br>狀態: Source diverged</div>'
        return 3, desc, local

    except subprocess.CalledProcessError:
        desc = '<div align=\"left\">版本檢查結果<br>狀態: [Error] Unable to get git information</div>'
        return 4, desc, local

def main():
    ''' Main function.
    '''
    app = QtWidgets.QApplication([])
    widget = AutoClimbWidget()
    widget.__init_ui__()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

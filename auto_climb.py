'''
The main module to run auto fill data progrom.
'''
import sys
import subprocess
import traceback
import pandas as pd

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDesktopWidget, QMessageBox
from PySide2.QtGui import QPixmap
from ui_button import PicButton
from park_auto import ParkAuto

PROG_NAME = 'auto_climb.py'
DEFAULT_GUI = 1
DEFAULT_PARK = 2
DEFAULT_MEMBERLIST = 'sample.xlsx'

def util_read_data_xlsx(filename, sheet):
    '''
    Utility to read member data from Excel file.
    '''
    if filename.split('.')[1] == 'xlsx':
        data_frame = pd.read_excel(filename, sheet, dtype='str')
    else:
        return False, None

    list_data = []
    for i in data_frame.index:
        dict_data = {}
        for key in data_frame.columns:
            dict_data[key] = data_frame[key][i]
        list_data.append(dict_data)

    return True, list_data

def utl_read_data(filename):
    '''
    Utility to read member data from file.
    '''
    print('read file ', filename)
    def ret_error(title):
        print('Error: ', title)
        return False, None, None

    obj_data = UserData(filename)
    b_ok, lst_mem = obj_data.get_member_list()
    if not b_ok:
        return ret_error(' get_member_list failure')
    if len(lst_mem) == 0:
        return ret_error(' len(lst_mem) == 0')

    b_ok, lst_stay = obj_data.get_stay_data()
    if not b_ok:
        return ret_error(' get_stay_data failure')
    if len(lst_stay) == 0:
        return ret_error(' len(lst_stay) == 0')
    return True, lst_mem, lst_stay
class UserData:
    '''
    Management the user data.
    '''
    def __init__(self, filename):
        self.filename = filename

    def get_member_list(self):
        '''
        Return the member list.
        '''
        return util_read_data_xlsx(self.filename, 'member')

    def get_stay_data(self):
        '''
        Return the contact person information.
        '''
        return util_read_data_xlsx(self.filename, 'stay')

class MainWidget(QtWidgets.QWidget):
    '''
    The main window widget.
    '''
    def __init__(self):
        super().__init__()
        self.obj_auto = None

        # add button
        bt_yushan = PicButton(QPixmap('./res/img/Yushan.png'))
        bt_taroko = PicButton(QPixmap('./res/img/Taroko.png'))
        bt_sheipa = PicButton(QPixmap('./res/img/Sheipa.png'))
        self.bt_fill_member = PicButton(QPixmap('./res/img/member_auto.png'))

        # add status label
        self.text_status = QtWidgets.QLabel("Status")
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
        box_button2.addWidget(self.bt_fill_member)
        self.bt_fill_member.setVisible(False)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(box_button)
        self.layout.addLayout(box_button2)
        self.layout.addWidget(self.text_status)
        self.setLayout(self.layout)

        bt_yushan.clicked.connect(self.__run_yushan__)
        bt_taroko.clicked.connect(self.__run_taroko__)
        bt_sheipa.clicked.connect(self.__run_sheipa__)
        self.bt_fill_member.clicked.connect(self.__run_fill_member__) # re-fill the member data

        self.dict_arg = {}
        self.dict_arg['memberlist'] = DEFAULT_MEMBERLIST
        self.dict_arg['park'] = DEFAULT_PARK
        self.dict_arg['auto_fill_member_list_at_start_for_demo'] = 1
        self.dict_arg['ui'] = self
        self.__loc_center__()

        self.text_status.setText('正在檢查版本 ...')
        QtCore.QTimer.singleShot(200, self.__check_version__)

    def __set_window_title__(self, strversion):
        self.setWindowTitle(PROG_NAME + '(commit id): ' + strversion)

    def __check_version__(self):
        _, desc, local_id = __check_update__()
        out = desc + '<div align=\"left\">' + \
                     '版本號碼:' + local_id.decode("utf-8").rstrip() + '.</div>'
        print(out)
        self.text_status.setText(out)
        _ = QMessageBox.question(self, '訊息', \
                     '<html> <p style="font-size:16pt"> ' + desc + '</p></html>', QMessageBox.Ok)

    def __run_fill_member__(self):
        if self.obj_auto is not None:
            if self.dict_arg['auto_fill_member_list_at_start_for_demo']:
                self.obj_auto.run_fill_form_member(b_refilled=1)
            else:
                self.obj_auto.run_fill_form_member(b_refilled=0)

    def __update_status__(self, str_status):
        print(str_status)
        self.text_status.setText(str_status)

    def __run_yushan__(self):
        self.__update_status__('玉山國家公園')
        self.dict_arg['park'] = 0
        self.run()

    def __run_taroko__(self):
        self.__update_status__('太魯閣國家公園')
        self.dict_arg['park'] = 1
        self.run()

    def __run_sheipa__(self):
        self.__update_status__('雪霸國家公園')
        self.dict_arg['park'] = 2
        self.run()

    def run(self):
        '''
        Execute the auto fill procedure.
        '''
        try:
            self.__load_memlst__()
            b_ok, lst_mem, lst_stay = utl_read_data(self.dict_arg['memberlist'])
            if not b_ok:
                print('Error: utl_read_data failure')
                return

            reply = QMessageBox.question(self, 'Continue?', \
                    '<html> <p style="font-size:16pt"> 自動填入隊員資料? (稍後可重複動作) </p></html>', \
                    QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print('reply = ', 'Yes')
                self.dict_arg['auto_fill_member_list_at_start_for_demo'] = True
            else:
                print('reply = ', 'NO')
                self.dict_arg['auto_fill_member_list_at_start_for_demo'] = False

            print('reply = ', reply)

            self.obj_auto = ParkAuto(self.dict_arg, lst_mem, lst_stay)
            self.obj_auto.run()

            # show re-fill member button only when obj_auto_run exist
            self.bt_fill_member.setVisible(True)
            self.__update_status__('完成. <br> 右側按鈕: 可以自動填入隊員資料')

            self.activateWindow()  # show the control panel
            reply = QMessageBox.question(self, '訊息', \
                    '<html> <p style="font-size:16pt"> 請修改自己的行程 <br> 完成修改後, 點選 [自動填入隊員資料] 按鈕 </p></html>', \
                    QMessageBox.Ok)
        except Exception as err:
            traceback.print_exc()
            msg = '\n\n查閱上方錯誤訊息, 進行檢測.\n\n1.請確定你的機器是否連上網際網路\n2.瀏覽器是否已經被關閉了\n3.有可能是瀏覽器版本太舊了, 請更新你的瀏覽器版本.\n\nDetail:{}'.format(format(err))
            print(msg)
            msg = '更新 Chrome 最新版本的指令:\nUbuntu:\n{}'.format('sudo apt-get --only-upgrade install google-chrome-stable')
            print(msg)
            return

    def __load_memlst__(self):
        print('load')
        lst_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Member Data', '.', selectedFilter='*.xlsx')
        if lst_filename:
            print(lst_filename[0])
            self.dict_arg['memberlist'] = lst_filename[0]

    def __loc_center__(self):
        screen_geo = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        loc_x = screen_geo.width()/2 - widget.width()/2 + screen_geo.width()/6
        loc_y = screen_geo.height()/2 - widget.height()/2
        self.move(loc_x, loc_y)

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
        return 3, desc

    except subprocess.CalledProcessError:
        desc = '<div align=\"left\">版本檢查結果<br>狀態: [Error] Unable to get git information</div>'
        return 4, desc, local

def main():
    '''
    Main function.
    '''
    app = QtWidgets.QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

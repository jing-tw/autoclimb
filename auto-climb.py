
import argparse
import time

from park_auto import ParkAuto

PROG_NAME = 'auto-climb.py'
DEFAULT_GUI = 1
DEFAULT_PARK = 2
DEFAULT_MEMBERLIST = 'sample.xlsx'

def read_data_xlsx(filename, sheet):
    import pandas as pd
    from pandas import ExcelWriter
    from pandas import ExcelFile
    
    if filename.split('.')[1] == 'xlsx':
        df = pd.read_excel(filename, sheet, dtype='str')
    else:
        return False, None
    #print("Column headings:")
    #print(df.columns)

    list_data = []
    for i in df.index:
        dict_data = {}
        for key in df.columns:
            dict_data[key] = df[key][i]
        list_data.append(dict_data)
        #print('one person = ', dict_person)  

    return True, list_data

def utl_read_data(filename):
    print('read file ', filename)
    def ret_error(title):
        print('Error: ', title)
        return False, None, None

    obj_data = UserData(filename)
    ok, lst_mem = obj_data.get_member_list()
    if not ok:
        return ret_error(' get_member_list failure')
    if len(lst_mem) == 0:
        return ret_error(' len(lst_mem) == 0')

    ok, lst_stay = obj_data.get_stay_data()
    if not ok:
        return ret_error(' get_stay_data failure')
    if len(lst_stay) == 0:
        return ret_error(' len(lst_stay) == 0')
        
    
    return True, lst_mem, lst_stay

class UserData:
    def __init__(self, filename):
        self.filename = filename

    def get_member_list(self):
        return read_data_xlsx(self.filename, 'member')

    def get_stay_data(self):
        return read_data_xlsx(self.filename, 'stay')
    
import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QDesktopWidget, QMessageBox
from PySide2.QtGui import QPixmap


from gui_button import PicButton

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # auto park object
        self.obj_auto = None

        # add button
        self.bt_yushan = PicButton(QPixmap('./res/img/Yushan.png'))
        self.bt_taroko = PicButton(QPixmap('./res/img/Taroko.png'))
        self.bt_sheipa = PicButton(QPixmap('./res/img/Sheipa.png'))
        self.bt_fill_member = QPushButton('自動填入成員資料')

        # add status label
        self.text_status = QtWidgets.QLabel("Status")
        self.text_status.setAlignment(QtCore.Qt.AlignCenter)

        # layout: upper
        box_button = QtWidgets.QHBoxLayout()
        box_button.addStretch(1)
        box_button.addWidget(self.bt_yushan)
        box_button.addWidget(self.bt_taroko)
        box_button.addWidget(self.bt_sheipa)
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

        self.bt_yushan.clicked.connect(self.run_yushan)
        self.bt_taroko.clicked.connect(self.run_taroko)
        self.bt_sheipa.clicked.connect(self.run_sheipa)
        self.bt_fill_member.clicked.connect(self.run_fill_member) # re-fill the member data

        self.dict_arg = {}
        self.dict_arg['memberlist'] = DEFAULT_MEMBERLIST
        self.dict_arg['park'] = DEFAULT_PARK
        self.dict_arg['auto_fill_member_list_at_start_for_demo'] = 1
        self.dict_arg['ui'] = self
        self.loc_center()

        self.text_status.setText('正在檢查版本 ...')
        QtCore.QTimer.singleShot(200, self.check_version)

        
        

    def set_window_title(self, strversion):
        self.setWindowTitle(PROG_NAME + '(commit id): ' + strversion)

    def check_version(self):
        res, desc, local_id = check_update()
        out = desc + '<br>(' + local_id.decode("utf-8").rstrip() + ')'
        print(out)
        self.text_status.setText(out)
        

    def run_fill_member(self):
        if self.obj_auto != None:
            self.obj_auto.run_fill_form_member()

    def update_status(self, strStatus):
        print(strStatus)
        self.text_status.setText(strStatus)

    def run_yushan(self):
        self.update_status('玉山國家公園')
        self.dict_arg['park'] = 0
        self.run()
        

    def run_taroko(self):
        self.update_status('太魯閣國家公園')
        self.dict_arg['park'] = 1
        self.run()
        

    def run_sheipa(self):
        self.update_status('雪霸國家公園')
        self.dict_arg['park'] = 2
        self.run()
        

    def run(self):
        try:
            self.load_memlst()
            ok, lst_mem, lst_stay = utl_read_data(self.dict_arg['memberlist'])
            if not ok: print('Error: utl_read_data failure'); return
            
            reply = QMessageBox.question(self, 'Continue?', 
                    '<html> <p style="font-size:16pt"> 是否現在要自動填入隊員資料? <br> (請放心! 選擇 No, 稍後還可以自動填入隊員資料) </p></html>', QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print('reply = ', 'Yes')
                self.dict_arg['auto_fill_member_list_at_start_for_demo'] = True
            else:
                print('reply = ', 'NO')
                self.dict_arg['auto_fill_member_list_at_start_for_demo'] = False
            
            print('reply = ', reply)

            self.obj_auto = ParkAuto(self.dict_arg, lst_mem, lst_stay)
            self.obj_auto.run()
            # self.show()

            # show re-fill member button only when obj_auto_run exist
            self.bt_fill_member.setVisible(True)
            self.update_status('完成. <br> 右側按鈕: 可以自動填入隊員資料')
        except Exception as e:
            msg = '請確定機器連線, 並更新你的瀏覽器版本'
            msg = msg + '\nformat(e) = ' + format(e)
            print(msg)
            return
    
    def load_memlst(self):
        print('load')
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Member Data', '.', selectedFilter='*.xlsx')
        if fileName:
            print(fileName[0])
            self.dict_arg['memberlist'] = fileName[0]

    def loc_center(self):
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = sg.width()/2 - widget.width()/2
        y = sg.height()/2 - widget.height()/2
        self.move(x, y)

def check_update():
    # ref: https://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git

    import subprocess

    try:
        print('checking version ...')
        subprocess.check_output('git fetch'.split())  # update ref
        local = subprocess.check_output('git rev-parse @'.split()) # return local HEAD id
        remote = subprocess.check_output('git rev-parse @{u}'.split()) # return remote HEAD id
        comm_base = subprocess.check_output('git merge-base @ @{u}'.split()) # return comm id

        if local == remote:
            desc = '版本檢查: 目前是最新版'
            return 0, desc, local
        elif local == comm_base:
            desc = '版本檢查: 發現有新版本, 可執行 git pull 更新'
            return 1, desc, local

        elif remote == comm_base:
            desc = '版本檢查: Need to push'
            return 2, desc, local

        else:
            desc = '版本檢查: Diverged'
            return 3, desc
        
    except subprocess.CalledProcessError:
        desc = '版本檢查: [Error] Unable to get git information'
        return 4, desc, local

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gui', '--gui', type=int, default = DEFAULT_GUI, help="Enable GUI mode")
    parser.add_argument('-p', '--park', type=int, default = DEFAULT_PARK, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")
    parser.add_argument('-list', '--memberlist', default = DEFAULT_MEMBERLIST, help='sample.xlsx')

    args = parser.parse_args()
    return 1, {'park':args.park, 'memberlist':args.memberlist, 'gui': args.gui}

def main():
    bValid, dict_arg = init_arg()

    if dict_arg['gui'] == 0:
        print('Console mode was obsoleted. Use: python autoclimb.py')
        # ok, lst_mem, lst_stay = utl_read_data(dict_arg['memberlist'])
        # if not ok: print('Error: utl_read_data failure'); return
        # obj_auto = ParkAuto(dict_arg['park'], lst_mem, lst_stay)
        # obj_auto.run()
    else:
        app = QtWidgets.QApplication([])
        widget = MyWidget()
        widget.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

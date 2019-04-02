
import argparse
from park_auto import ParkAuto

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
from PySide2.QtWidgets import QAbstractButton
from PySide2.QtGui import QPixmap, QPainter

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.enter = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

        if self.enter:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.drawRectangles(qp, event.rect())
            qp.end()

    def drawRectangles(self, qp, rec):
        qp.setBrush(QtGui.QColor(000, 000, 255, 255/4))
        qp.drawRect(rec.left(), rec.top(), rec.width(), rec.height())

    def enterEvent(self, event):
        self.enter = True
        self.update()

    def leaveEvent(self, event):
        self.enter = False
        self.update()

    def sizeHint(self):
        return self.pixmap.size()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # auto park object
        self.obj_auto = None

        # add button
        self.bt_yushan = PicButton(QPixmap('./res/img/Yushan.png'))
        self.bt_taroko = PicButton(QPixmap('./res/img/Taroko.png'))
        self.bt_sheipa = PicButton(QPixmap('./res/img/Sheipa.png'))
        self.bt_fill_member = QPushButton('填入成員資料')

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

    def run_fill_member(self):
        if self.obj_auto != None:
            self.obj_auto.run_fill_form_member()

    def run_yushan(self):
        print('run')
        self.dict_arg['park'] = 0
        self.run()

    def run_taroko(self):
        print('run')
        self.dict_arg['park'] = 1
        self.run()

    def run_sheipa(self):
        print('run')
        self.dict_arg['park'] = 2
        self.run()

    def run(self):
        self.load_memlst()
        ok, lst_mem, lst_stay = utl_read_data(self.dict_arg['memberlist'])
        if not ok: print('Error: utl_read_data failure'); return

        self.obj_auto = ParkAuto(self.dict_arg['park'], lst_mem, lst_stay)
        self.obj_auto.run()
        self.show()

        # show re-fill member button only when obj_auto_run exist
        self.bt_fill_member.setVisible(True)
    
    def load_memlst(self):
        print('load')
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Member Data', '.', selectedFilter='*.xlsx')
        if fileName:
            print(fileName[0])
            self.dict_arg['memberlist'] = fileName[0]

def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gui', '--gui', type=int, default = DEFAULT_GUI, help="Enable GUI mode")
    parser.add_argument('-p', '--park', type=int, default = DEFAULT_PARK, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")
    parser.add_argument('-list', '--memberlist', default = DEFAULT_MEMBERLIST, help='sample.xlsx')

    args = parser.parse_args()
    #print("args.park =", args.park)
    return 1, {'park':args.park, 'memberlist':args.memberlist, 'gui': args.gui}


def main():
    bValid, dict_arg = init_arg()

    if dict_arg['gui'] == 0:
        ok, lst_mem, lst_stay = utl_read_data(dict_arg['memberlist'])
        if not ok: print('Error: utl_read_data failure'); return
        obj_auto = ParkAuto(dict_arg['park'], lst_mem, lst_stay)
        obj_auto.run()
    else:
        app = QtWidgets.QApplication([])
        widget = MyWidget()
        widget.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

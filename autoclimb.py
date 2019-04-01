
import argparse

from park_auto import ParkAuto

DEFAULT_GUI = 1
DEFAULT_PARK = 2
DEFAULT_MEMBERLIST = 'sample.xlsx'


def read_member_list(strFile):
    import pandas as pd
    from pandas import ExcelWriter
    from pandas import ExcelFile
    
    df = pd.read_excel('sample.xlsx', sheet_name='member', dtype='str')
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









import sys
import random
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
        
        # add button
        self.bt_yushan = PicButton(QPixmap('./res/img/Yushan.png'))
        self.bt_taroko = PicButton(QPixmap('./res/img/Taroko.png'))
        self.bt_sheipa = PicButton(QPixmap('./res/img/Sheipa.png'))
        # self.bt_load_memlst= QtWidgets.QPushButton("Load Member List")

        # add status label
        self.text_status = QtWidgets.QLabel("Status")
        self.text_status.setAlignment(QtCore.Qt.AlignCenter)

        # layout
        box_button = QtWidgets.QHBoxLayout()
        box_button.addStretch(1)
        #box_button.addWidget(self.bt_load_memlst)
        box_button.addWidget(self.bt_yushan)
        box_button.addWidget(self.bt_taroko)
        box_button.addWidget(self.bt_sheipa)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.text_status)
        self.layout.addLayout(box_button)
        self.setLayout(self.layout)

        self.bt_yushan.clicked.connect(self.run_yushan)
        self.bt_taroko.clicked.connect(self.run_taroko)
        self.bt_sheipa.clicked.connect(self.run_sheipa)
        # self.bt_load_memlst.clicked.connect(self.load_memlst)

        
        # self.resize(300, 100)
        # self.show()

        self.dict_arg = {}
        self.dict_arg['memberlist'] = DEFAULT_MEMBERLIST
        self.dict_arg['park'] = DEFAULT_PARK

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
        lst_mem = read_member_list(self.dict_arg['memberlist'])
        obj_auto = ParkAuto(self.dict_arg['park'], lst_mem)
        obj_auto.run()
    

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
        lst_mem = read_member_list(dict_arg['memberlist'])
        obj_auto = ParkAuto(dict_arg['park'], lst_mem)
        obj_auto.run()
    else:
        app = QtWidgets.QApplication([])
        widget = MyWidget()
        widget.resize(800, 600)
        widget.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

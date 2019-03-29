
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

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        

        self.bt_run = QtWidgets.QPushButton("Run!")
        self.bt_load_memlst= QtWidgets.QPushButton("Load Member List")

        self.text_status = QtWidgets.QLabel("Status")
        self.text_status.setAlignment(QtCore.Qt.AlignCenter)

        box_v = QtWidgets.QVBoxLayout()
        box_v.addStretch(1)
        box_v.addWidget(self.bt_load_memlst)
        box_v.addWidget(self.bt_run)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.text_status)
        self.layout.addLayout(box_v)
        

        self.setLayout(self.layout)

        self.bt_run.clicked.connect(self.run)
        self.bt_load_memlst.clicked.connect(self.load_memlst)

        
        # self.resize(300, 100)
        # self.show()

        self.dict_arg = {}
        self.dict_arg['memberlist'] = DEFAULT_MEMBERLIST
        self.dict_arg['park'] = DEFAULT_PARK

    def run(self):
        print('run')
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

import inspect
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

#from ...autotest_layer_widget import AutoTestLayerWidget
#from ...autoclimb import AutoClimbWidget
from test.util.test_utility import TestBaseWidget
from test.test_vector.test_vector import TestVector




class TestAutoClimbWidgetDemo(TestBaseWidget):
    def test_item_init(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')

        self.window = self.__begin__(qtbot, '...autoclimb', 'AutoClimbWidget', str_title)  # direct debug the component
        self.window.show()

        def fn_action_1_check_data():
            bt_yushan = self.window.autotest_get('bt_yushan')
            qtbot.mouseClick(bt_yushan, Qt.LeftButton)
            #self.autotest_add(bt_taroko, 'bt_taroko')
            #self.autotest_add(bt_sheipa, 'bt_sheipa')

            # pass
            # widget_table = self.window.autotest_get('widget_table')
            # test_vector_lst_item_rd = self.window.autotest_get('test_vector_lst_item_rd')
            # test_vector_lst_visible_str_key = self.window.autotest_get('test_vector_lst_visible_str_key')
            # assert(widget_table.columnCount() == len(test_vector_lst_visible_str_key))
            # assert(widget_table.rowCount() == len(test_vector_lst_item_rd))

        def fn_action_2_bt_add():
            pass

        def on_timeout_close():
            #self.window.close()
            pass

        self.lst_fun = [fn_action_1_check_data, fn_action_2_bt_add, on_timeout_close]
        self.__run__(self.lst_fun, 2000)

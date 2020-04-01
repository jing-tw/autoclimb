import inspect
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize

#from ...autotest_layer_widget import AutoTestLayerWidget
#from ...autoclimb import AutoClimbWidget
from test.util.test_utility import TestBaseWidget
from test.test_vector.test_vector import TestVector


# Usage:
# class AutoClimbWidgetDemo(AutoTestLayerWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#     def __init_ui__(self):
#         bt_OK = QPushButton('ok')
#         widget_table_view = AutoClimbWidget(None)
#         test_vector_lst_item_rd = TestVector.get_item_rd_small()
#         test_vector_lst_visible_str_key = ['品項:str', '單價:float']
#         widget_table_view.load_and_update(test_vector_lst_item_rd, test_vector_lst_visible_str_key)

#         layout = QVBoxLayout()
#         layout.addWidget(widget_table_view)
#         layout.addWidget(bt_OK)
#         self.setLayout(layout)

#         self.autotest_add(widget_table_view.autotest_get('widget_table'), 'widget_table')
#         self.autotest_add(test_vector_lst_item_rd, 'test_vector_lst_item_rd')
#         self.autotest_add(test_vector_lst_visible_str_key, 'test_vector_lst_visible_str_key')


class TestAutoClimbWidgetDemo(TestBaseWidget):
    def test_item_init(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')

        test_usage = 0
        if test_usage:
            self.window = self.__begin__(qtbot, 'test.test_package.test_ListViewWidget', 'AutoClimbWidgetDemo', str_title)
        else:
            self.window = self.__begin__(qtbot, '...autoclimb', 'AutoClimbWidget', str_title)  # direct debug the component
        self.window.show()

        def fn_action_1_check_data():
            pass
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
        self.__run__(self.lst_fun, 500)

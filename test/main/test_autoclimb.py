#pylint: disable=line-too-long, attribute-defined-outside-init, missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, unused-argument, arguments-differ

import inspect
import sys
from test.test_vector.test_vector import TestVector
from test.util.test_utility import TestBaseWidget2
from test.util.test_utility import add_method
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from autoclimb import AutoClimbWidget
@add_method(AutoClimbWidget)
def __check_version__():
    ''' OVERRIDE: No check version.
    '''
    #pylint: disable = unused-variable
    print('[auto-test] override method: __check_version__')
    return

@add_method(AutoClimbWidget)
def __get_filename__():
    ''' OVERRIDE: Use sample file.
    '''
    #pylint: disable = unused-variable
    print('[auto-test] override method: __get_filename__')
    return 1, TestVector.get_test_member_file(), 'ok'

@add_method(AutoClimbWidget)
def __ask_autofill_member__():
    ''' OVERRIDE: Auto fill member.
    '''
    #pylint: disable = unused-variable
    print('[auto-test] override method: __ask_autofill_member__')
    return 1

@add_method(AutoClimbWidget)
def __ack_continue_fill_schedule__():
    ''' OVERRIDE: Auto accept.
    '''
    #pylint: disable = unused-variable
    print('[auto-test] override method: __ack_continue_fill_schedule__')
    return 1


class TestAutoClimbWidgetDemo(TestBaseWidget2):
    def test_all(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')


        self.index = 0
        self.app = QApplication([sys.argv])

        self.window = AutoClimbWidget()
        self.window.__init_ui__()
        self.window.setWindowTitle(str_title)
        self.window.show()
        self.window.__ack_continue_fill_schedule__()
        qtbot.add_widget(self.window)

        def fn_action_1():
            bt_yushan = self.window.autotest_get('bt_yushan')
            qtbot.mouseClick(bt_yushan, Qt.LeftButton)

        def fn_action_2():
            bt_taroko = self.window.autotest_get('bt_taroko')
            qtbot.mouseClick(bt_taroko, Qt.LeftButton)

        def fn_action_3():
            bt_sheipa = self.window.autotest_get('bt_sheipa')
            qtbot.mouseClick(bt_sheipa, Qt.LeftButton)

        def on_timeout_close():
            self.window.close()
            #pass

        self.lst_fun = [fn_action_1, fn_action_2, fn_action_3, on_timeout_close]
        self.__run__(self.lst_fun, 1000)

    def test_yushan(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')


        self.index = 0
        self.app = QApplication([sys.argv])

        self.window = AutoClimbWidget()
        self.window.__init_ui__()
        self.window.setWindowTitle(str_title)
        self.window.show()
        self.window.__ack_continue_fill_schedule__()
        qtbot.add_widget(self.window)

        def fn_action_1():
            bt_yushan = self.window.autotest_get('bt_yushan')
            qtbot.mouseClick(bt_yushan, Qt.LeftButton)

        def on_timeout_close():
            self.window.close()
            #pass

        self.lst_fun = [fn_action_1, on_timeout_close]
        self.__run__(self.lst_fun, 10000)

    def test_taroko(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')

        self.index = 0
        self.app = QApplication([sys.argv])

        self.window = AutoClimbWidget()
        self.window.__init_ui__()
        self.window.setWindowTitle(str_title)
        self.window.show()
        self.window.__ack_continue_fill_schedule__()
        qtbot.add_widget(self.window)

        def fn_action_1():
            bt_taroko = self.window.autotest_get('bt_taroko')
            qtbot.mouseClick(bt_taroko, Qt.LeftButton)


        def on_timeout_close():
            self.window.close()
            #pass

        self.lst_fun = [fn_action_1, on_timeout_close]
        self.__run__(self.lst_fun, 10000)

    def test_sheipa(self, qtbot, monkeypatch):
        print('test_item_init')
        str_title = 'Testing: ' + inspect.currentframe().f_code.co_name
        print(str_title + ' testing... ')


        self.index = 0
        self.app = QApplication([sys.argv])

        self.window = AutoClimbWidget()
        self.window.__init_ui__()
        self.window.setWindowTitle(str_title)
        self.window.show()
        self.window.__ack_continue_fill_schedule__()
        qtbot.add_widget(self.window)

        def fn_action_1():
            bt_sheipa = self.window.autotest_get('bt_sheipa')
            qtbot.mouseClick(bt_sheipa, Qt.LeftButton)

        def on_timeout_close():
            self.window.close()
            #pass

        self.lst_fun = [fn_action_1, on_timeout_close]
        self.__run__(self.lst_fun, 10000)

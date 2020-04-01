#pylint: disable=line-too-long, attribute-defined-outside-init, missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, unused-argument, arguments-differ

import sys
import inspect
import importlib
from functools import wraps # This convenience func preserves name and docstring
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

class UtilityTest():
    @staticmethod
    def get_menu_action_static(widget, menu, str_name):
        if menu is None:
            return 0, None, 'Menu is None.'
        for act in menu.actions():
            if act.menu():
                ok, act, msg = widget.get_menu_action_static(menu, str_name)
                if not ok:
                    return 0, None, msg
            if str_name in act.text():
                return 1, act, 'ok'
        return 0, None, 'Not found'


class TestUIBase2():
    app = None # ensure only one QApplication instance

    def __run__(self, lst_fun, int_delay_ms=200):
        self.index = 0
        # QTime chain invoking
        def on_timeout_fun():
            if self.index < len(lst_fun):
                lst_fun[self.index]()
                QTimer.singleShot(int_delay_ms, on_timeout_fun)
            self.index = self.index + 1

        QTimer.singleShot(int_delay_ms, on_timeout_fun)
        self.index = 0


    # def __get_window_target__(self, qtbot, str_module, str_class, str_title):
    #     module = importlib.import_module(str_module)
    #     class_ = getattr(module, str_class)
    #     window = class_()
    #     window.__init_ui__()
    #     window.setWindowTitle(str_title)
    #     qtbot.add_widget(window)
    #     #qtbot.waitUntil(lambda: window.isVisible())
    #     return window

class TestBaseWidget2(TestUIBase2):
    # def __begin__(self, qtbot, str_module, str_class, str_title):
    #     super().__begin__()
    #     window = self.__get_window_target__(qtbot, str_module, str_class, str_title)
    #     return window

    def __run__(self, lst_fun, int_delay_ms=200):
        super().__run__(lst_fun, int_delay_ms)
        #TestBaseWidget.app.exec_()
        self.app.exec_()



class TestBaseDlg2(TestUIBase2):
    def __run__(self, target_dlg, lst_fun, int_delay_ms=200):
        super().__run__(lst_fun, int_delay_ms)
        target_dlg.exec_()


def add_method(cls):
    '''Dynamic override or add an instance method.
    Reference: https://medium.com/@mgarod/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6
    '''
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func # returning func means func can still be used normally
    return decorator

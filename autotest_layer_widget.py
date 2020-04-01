'''
Autotest layer module.
'''
from PyQt5.QtWidgets import QWidget

class AutoTestLayerWidget(QWidget):
    '''
    Autotestest layer class.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.__dict_test__ = dict()  # auto_test layer

    def autotest_add(self, obj, str_name):
        ''' Add target object for testing.
        '''
        self.__dict_test__[str_name] = obj

    def autotest_get(self, str_name):
        ''' Get target object.
        '''
        return self.__dict_test__[str_name]

    def autotest_get_list(self, str_glob):
        ''' Get the testing target object group.
        '''
        lst_target = list()
        for key in self.__dict_test__:
            if str_glob in key:
                lst_target.append(self.__dict_test__[key])
        return lst_target

    def get_test_dict(self):
        ''' Get test dictionary.
        '''
        return self.__dict_test__

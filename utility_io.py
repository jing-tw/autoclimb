'''
Utiilty for I/O.
'''
import math
import pandas as pd

class UserData:
    ''' Management the user data.
    '''
    def __init__(self, filename):
        self.filename = filename

    def get_meta_data(self):
        '''Return the meta data for the file.
        '''
        b_ok, lst_dict_data, msg = util_read_data_xlsx(self.filename, 'meta')
        if not b_ok:
            print(msg)
            return 0, None, msg
        lst_dict_data = UserData.__remove_invalid_raw__(lst_dict_data)
        return 1, lst_dict_data, msg

    

    def get_team(self):
        '''Return the team infomation.
        '''
        b_ok, team_data, msg = util_read_data_xlsx(self.filename, 'team')
        if not b_ok:
            print(msg)
            return 0, None, msg
        return 1, team_data[0], msg

    def get_member_list(self):
        '''Return the member list.
        '''
        b_ok, lst_dict_data, msg = util_read_data_xlsx(self.filename, 'member')
        if not b_ok:
            print(msg)
            return 0, None
        lst_dict_data = UserData.__remove_invalid_raw__(lst_dict_data)
        b_ok, msg = self.__check_fmt__(lst_dict_data)
        if not b_ok:
            print(msg)
            return 0, None
        return 1, lst_dict_data

    def get_stay_data(self):
        '''Return the contact person information.
        '''
        b_ok, lst_dict_data, msg = util_read_data_xlsx(self.filename, 'stay')
        if not b_ok:
            print(msg)
            return 0, None
        return 1, lst_dict_data

    @staticmethod
    def __remove_invalid_raw__(lst_dict_data):
        lst_dict_data_new = list()

        for dict_data in lst_dict_data:
            if not UserData.__has_nan_value__(dict_data):
                lst_dict_data_new.append(dict_data)

        return lst_dict_data_new

    @staticmethod
    def __has_nan_value__(dict_data):
        for key in dict_data.keys():
            # if str(key).startswith('Unnamed'):
            #     continue
            data = dict_data[key]
            if (type(data) == int or type(data) == float):
                if math.isnan(data):
                    return True
        return False
    
    @staticmethod
    def __check_fmt__(lst_dict_data):
        '''
        Check the member data format.
        '''
        for dict_data in lst_dict_data:
            b_ok, msg = UserData.__check_fmt_mobile__(dict_data)
            if not b_ok:
                return 0, msg
        return 1, 'ok'

    @staticmethod
    def __check_fmt_mobile__(dict_data):
        if len(dict_data['id_mobile']) != 10:
            return 0, '[Format Error] id_mobile != 10.\nDetail:\nvalue = {}'.format(dict_data['id_mobile'])
        return 1, 'ok'


def util_read_data_xlsx(filename, sheet):
    ''' Utility to data from Excel file.
    '''
    try:
        if filename.split('.')[-1] == 'xlsx':
            data_frame = pd.read_excel(filename, sheet, dtype='str', engine='openpyxl')
        else:
            return 0, None, 'Error: The file extension does not xlsx.'

        lst_dict_data = list()
        for i in data_frame.index:
            dict_data = dict()
            for key in data_frame.columns:
                if str(key).startswith('Unnamed'):
                    continue
                dict_data[key] = data_frame[key][i]
            lst_dict_data.append(dict_data)

        return 1, lst_dict_data, 'ok'
    except Exception as err:
        if 'No sheet named' in format(err):
            return 0, None, 'Error: No sheet named {} in the file.'.format(sheet)
        raise err

def utl_read_data(filename, team_default, lst_meta_default):
    ''' Utility to reasd member data from file.
    '''
    print('read file ', filename)
    def ret_error(title):
        print('Error: ', title)
        return False, None, None

    obj_data = UserData(filename)

    b_ok, lst_meta, msg = obj_data.get_meta_data()
    if not b_ok:
        if 'No sheet named' in msg:
            print('Auto-Fix: 發現舊資料檔格式, 登山隊相關資訊使用預設值代替. (建議使用新格式, 紀錄你的登山隊資料. 參考: sample_9_people.xlsx)')
            lst_meta = lst_meta_default
        else:
            return ret_error(' get_meta_data failure')

    b_ok, team, msg = obj_data.get_team()
    if not b_ok:
        if 'No sheet named' in msg:
            print('Auto-Fix: 發現舊資料檔格式, 登山隊相關資訊使用預設值代替. (建議使用新格式, 紀錄你的登山隊資料. 參考: sample_9_people.xlsx)')
            team = team_default
        else:
            return ret_error(' get_team failure')

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

    return True, team, lst_mem, lst_stay, lst_meta

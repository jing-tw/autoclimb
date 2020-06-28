'''
Utiilty for I/O.
'''
import pandas as pd

class UserData:
    ''' Management the user data.
    '''
    def __init__(self, filename):
        self.filename = filename

    def get_team(self):
        b_ok, team_data = util_read_data_xlsx(self.filename, 'team')
        if not b_ok:
            return 0, None
        return 1, team_data[0]

    def get_member_list(self):
        '''Return the member list.
        '''
        #return util_read_data_xlsx(self.filename, 'member')
        b_ok, lst_dict_data = util_read_data_xlsx(self.filename, 'member')
        if not b_ok:
            return 0, None
        b_ok, msg = self.__check_fmt__(lst_dict_data)
        if not b_ok:
            print(msg)
            return 0, None
        return 1, lst_dict_data

    def get_stay_data(self):
        '''Return the contact person information.
        '''
        # return util_read_data_xlsx(self.filename, 'stay')
        b_ok, lst_dict_data = util_read_data_xlsx(self.filename, 'stay')
        if not b_ok:
            return 0, None
        # b_ok, msg = self.__check_fmt__(lst_dict_data)
        # if not b_ok:
        #     print(msg)
        #     return 0, None
        return 1, lst_dict_data

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
    ''' Utility to read member data from Excel file.
    '''
    if filename.split('.')[-1] == 'xlsx':
        data_frame = pd.read_excel(filename, sheet, dtype='str')
    else:
        return False, None

    lst_dict_data = list()
    for i in data_frame.index:
        dict_data = dict()
        for key in data_frame.columns:
            dict_data[key] = data_frame[key][i]
        lst_dict_data.append(dict_data)

    return True, lst_dict_data

def utl_read_data(filename):
    ''' Utility to read member data from file.
    '''
    print('read file ', filename)
    def ret_error(title):
        print('Error: ', title)
        return False, None, None

    obj_data = UserData(filename)

    b_ok, team = obj_data.get_team()
    if not b_ok:
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

    return True, team, lst_mem, lst_stay

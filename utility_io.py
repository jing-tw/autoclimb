'''
Utiilty for I/O.
'''
import pandas as pd

class UserData:
    ''' Management the user data.
    '''
    def __init__(self, filename):
        self.filename = filename

    def get_member_list(self):
        '''Return the member list.
        '''
        return util_read_data_xlsx(self.filename, 'member')

    def get_stay_data(self):
        '''Return the contact person information.
        '''
        return util_read_data_xlsx(self.filename, 'stay')

def util_read_data_xlsx(filename, sheet):
    ''' Utility to read member data from Excel file.
    '''
    if filename.split('.')[-1] == 'xlsx':
        data_frame = pd.read_excel(filename, sheet, dtype='str')
    else:
        return False, None

    list_data = []
    for i in data_frame.index:
        dict_data = {}
        for key in data_frame.columns:
            dict_data[key] = data_frame[key][i]
        list_data.append(dict_data)

    return True, list_data

def utl_read_data(filename):
    ''' Utility to read member data from file.
    '''
    print('read file ', filename)
    def ret_error(title):
        print('Error: ', title)
        return False, None, None

    obj_data = UserData(filename)
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
    return True, lst_mem, lst_stay

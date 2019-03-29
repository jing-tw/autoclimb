
import argparse

from park_auto import ParkAuto


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


def init_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--park', type=int, default = 2, help="National Park (0: YUSHAN NATIONAL PARK, 1: TAROKO NATIONAL PARK, 2: SHEI-PA NATIONAL PARK")
    parser.add_argument('-list', '--memberlist', default = 'sample.xlsx', help='sample.xlsx')

    args = parser.parse_args()
    #print("args.park =", args.park)
    return 1, {'park':args.park, 'memberlist':args.memberlist}


def main():
    bValid, dict_arg = init_arg()

    lst_mem = read_member_list(dict_arg['memberlist'])

    obj_auto = ParkAuto(dict_arg['park'], lst_mem)
    obj_auto.run()
    

if __name__ == '__main__':
    main()

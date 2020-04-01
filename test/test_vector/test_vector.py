class TestVector():
    @classmethod
    def get_item_rd_list(cls, int_item_id_start=100, int_item_num_test1=5):
            lst_item_rd = list()
            int_item_id = int_item_id_start
            for i in range(0, int_item_num_test1): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 1', 'level_2:str':'class 1-1', 'level_3:str':'class 1-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            int_item_id +=1
            lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 1', 'level_2:str':'class 1-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 1', 'level_2:str':'class 1-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 1', 'level_2:str':'class 1-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 1', 'level_2:str':'class 1-4', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 2', 'level_2:str':'class 2-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 2', 'level_2:str':'class 2-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 2', 'level_2:str':'class 2-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 3', 'level_2:str':'class 3-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 3', 'level_2:str':'class 3-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 3', 'level_2:str':'class 3-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 3', 'level_2:str':'class 3-4', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 4', 'level_2:str':'class 4-1', 'level_3:str':'class 4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 4', 'level_2:str':'class 4-1', 'level_3:str':'class 4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 4', 'level_2:str':'class 4-1', 'level_3:str':'class 4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'class 4', 'level_2:str':'class 4-1', 'level_3:str':'class 4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})

            return lst_item_rd

    @classmethod
    def get_item_rd_list2(cls, int_item_id_start, int_item_num_test1):
            lst_item_rd = list()
            int_item_id = int_item_id_start
            for i in range(0, int_item_num_test1): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-1', 'level_3:str':'類別＿1-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            int_item_id +=1
            lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 10 items with full 2 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-4', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿2', 'level_2:str':'類別＿2-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿2', 'level_2:str':'類別＿2-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿2', 'level_2:str':'類別＿2-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿3', 'level_2:str':'類別＿3-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 10): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿3', 'level_2:str':'類別＿3-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 14): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿3', 'level_2:str':'類別＿3-3', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): 
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿3', 'level_2:str':'類別＿3-4', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿4', 'level_2:str':'類別＿4-1', 'level_3:str':'類別＿4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿4', 'level_2:str':'類別＿4-1', 'level_3:str':'類別＿4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿4', 'level_2:str':'類別＿4-1', 'level_3:str':'類別＿4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            for i in range(0, 5): # 5 items with full 3 classes
                int_item_id +=1
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿4', 'level_2:str':'類別＿4-1', 'level_3:str':'類別＿4-1-1', '品項號碼:str':'1', '品項:str':'{}'.format(str(i)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})

            return lst_item_rd

    @classmethod
    def get_item_rd_small(cls, int_item_id_start=1, int_item_num_test1=2):
            lst_item_rd = list()
            int_item_id = int_item_id_start
            for i in range(0, int_item_num_test1): # 5 items with full 3 classes
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-1', 'level_3:str':'類別＿1-1-1', '品項號碼:str':'1', '品項:str':'品項 {}'.format(str(int_item_id)), '單價:float': 0, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
                int_item_id +=1
            lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-1', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'品項 {}'.format(str(int_item_id)), '單價:float': 1, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
            int_item_id +=1
            for i in range(0, 3): # 10 items with full 2 classes
                lst_item_rd.append({'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'品項 {}'.format(str(int_item_id)), '單價:float': 2, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''})
                int_item_id +=1
            
            return lst_item_rd

    @classmethod
    def get_item_rd_single(cls, int_item_id):
        return {'id:str':str(int_item_id), 'level_1:str':'類別＿1', 'level_2:str':'類別＿1-2', 'level_3:str':'', '品項號碼:str':'1', '品項:str':'品項 {}'.format(str(int_item_id)), '單價:float': 2, '折扣方式:int': 3, 'Discount:int': 0,  '是否販賣:int': 1, '計價方式:str': '重',  '折扣群組:str': '1', '順序:int': 0,  '品項說明:str': '', 'pic_path:str': ''}
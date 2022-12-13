import sqlite3, os.path, sys, base64
from bs4 import BeautifulSoup

#Tạo đường dẫn file
if getattr(sys, 'frozen', False):
    working_dir = os.path.dirname(os.path.abspath(sys.executable))
else:
    working_dir = os.path.dirname(os.path.abspath(__file__))

class dataConnection(object):
    def __init__(self):
        self.con = sqlite3.connect(working_dir + '\database.db')
        self.cur = self.con.cursor()

    def create_xml1_table(self):
        tags= ["MA_LK","STT","MA_BN","HO_TEN","NGAY_SINH","GIOI_TINH","DIA_CHI","MA_THE","MA_DKBD","GT_THE_TU","GT_THE_DEN","MIEN_CUNG_CT","TEN_BENH","MA_BENH","MA_BENHKHAC","MA_LYDO_VVIEN","MA_NOI_CHUYEN","MA_TAI_NAN","NGAY_VAO","NGAY_RA","SO_NGAY_DTRI","KET_QUA_DTRI","TINH_TRANG_RV","NGAY_TTOAN","T_THUOC","T_VTYT","T_TONGCHI","T_BNTT","T_BNCCT","T_BHTT","T_NGUONKHAC","T_NGOAIDS","NAM_QT","THANG_QT","MA_LOAI_KCB","MA_KHOA","MA_CSKCB","MA_KHUVUC","MA_PTTT_QT","CAN_NANG"]
        stm = ''
        for tag in tags:
            stm = stm + tag.lower() + " TEXT,"
        stm = 'CREATE TABLE "xml1" ("id" INTEGER, ' + stm + 'PRIMARY KEY("id" AUTOINCREMENT));'
        self.cur.execute(stm)
    
    def create_xml2_table(self):
        tags= ['MA_LK','STT','MA_THUOC','MA_NHOM','TEN_THUOC','DON_VI_TINH','HAM_LUONG','DUONG_DUNG','LIEU_DUNG','SO_DANG_KY','TT_THAU','PHAM_VI','TYLE_TT','SO_LUONG','DON_GIA','THANH_TIEN','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_BAC_SI','MA_BENH','NGAY_YL','MA_PTTT']
        stm = ''
        for tag in tags:
            stm = stm + tag.lower() + " TEXT,"
        stm = 'CREATE TABLE "xml2" ("id" INTEGER, ' + stm + 'PRIMARY KEY("id" AUTOINCREMENT));'
        self.cur.execute(stm)
    
    def create_xml3_table(self):
        tags = ['MA_LK','STT','MA_DICH_VU','MA_VAT_TU','MA_NHOM','GOI_VTYT','TEN_VAT_TU','TEN_DICH_VU','DON_VI_TINH','PHAM_VI','SO_LUONG','DON_GIA','TT_THAU','TYLE_TT','THANH_TIEN','T_TRANTT','MUC_HUONG','T_NGUONKHAC','T_BNTT','T_BHTT','T_BNCCT','T_NGOAIDS','MA_KHOA','MA_GIUONG','MA_BAC_SI','MA_BENH','NGAY_YL','NGAY_KQ','MA_PTTT']
        stm = ''
        for tag in tags:
            stm = stm + tag.lower() + " TEXT,"
        stm = 'CREATE TABLE "xml3" ("id" INTEGER, ' + stm + 'PRIMARY KEY("id" AUTOINCREMENT));'
        self.cur.execute(stm)
    
    def create_xml4_table(self):
        tags = ['MA_LK','STT','MA_DICH_VU','MA_CHI_SO','TEN_CHI_SO','GIA_TRI','MA_MAY','MO_TA','KET_LUAN','NGAY_KQ']
        stm = ''
        for tag in tags:
            stm = stm + tag.lower() + " TEXT,"
        stm = 'CREATE TABLE "xml4" ("id" INTEGER, ' + stm + 'PRIMARY KEY("id" AUTOINCREMENT));'
        self.cur.execute(stm)

    # GET XML
    # Get xml1 data
    def get_xml1(self):
        return self.cur.execute("SELECT * FROM xml1").fetchall()
    # Get xml1 data
    def get_xml2(self, ma_lk):
        return self.cur.execute(f"SELECT * FROM xml2 WHERE ma_lk = '{ma_lk}'").fetchall()
    # Get xml1 data
    def get_xml3(self, ma_lk):
        return self.cur.execute(f"SELECT * FROM xml3 WHERE ma_lk = '{ma_lk}'").fetchall()
    # Get xml1 data
    def get_xml4(self, ma_lk):
        return self.cur.execute(f"SELECT * FROM xml4 WHERE ma_lk = '{ma_lk}'").fetchall()
    # Get xml1 data
    def get_xml5(self, ma_lk):
        return self.cur.execute(f"SELECT * FROM xml5 WHERE ma_lk = '{ma_lk}'").fetchall()


    def delete_xml1_table(self):
        stm = "DELETE FROM xml1"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))

    def insert_xml1_table(self, data):
        data_decode = base64.b64decode(data)
        data_xml = BeautifulSoup(data_decode, "xml")
        data_xml = data_xml.find('TONG_HOP')
        column_list = ''
        value_list = ''
        for i, ele in enumerate(data_xml):
            if (ele.name != None):
                column_list = column_list + f'{str(ele.name).lower()},'
                value_list = value_list + f'"{str(ele.text)}",'
        column_list = column_list[:-1] 
        value_list = value_list[:-1]  

        stm = f"INSERT INTO xml1 (id,{column_list}) VALUES (null,{value_list});"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))

    def delete_xml2_table(self):
        stm = "DELETE FROM xml2"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))
    
    def insert_xml2_table(self, data):
        data_decode = base64.b64decode(data)
        data_xml = BeautifulSoup(data_decode, "xml")
        ctthuoc_list = data_xml.find_all('CHI_TIET_THUOC')
        for ctthuoc in ctthuoc_list:
            column_list = ''
            value_list = ''
            for ele in ctthuoc:
                if (ele.name != None):
                    column_list = column_list + f'{str(ele.name).lower()},'
                    value_list = value_list + f'"{str(ele.text)}",'
            column_list = column_list[:-1] 
            value_list = value_list[:-1]  
            stm = f"INSERT INTO xml2 (id,{column_list}) VALUES (null,{value_list});"
            try:
                self.cur.execute(stm)
                self.con.commit()
            except Exception as e:
                print(str(e))
    
    def delete_xml3_table(self):
        stm = "DELETE FROM xml3"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))
    
    def insert_xml3_table(self, data):
        data_decode = base64.b64decode(data)
        data_xml = BeautifulSoup(data_decode, "xml")
        ct_dvkt_list = data_xml.find_all('CHI_TIET_DVKT')
        for ct_dvkt in ct_dvkt_list:
            column_list = ''
            value_list = ''
            for ele in ct_dvkt:
                if (ele.name != None):
                    column_list = column_list + f'{str(ele.name).lower()},'
                    value_list = value_list + f'"{str(ele.text)}",'
            column_list = column_list[:-1] 
            value_list = value_list[:-1]  
            stm = f"INSERT INTO xml3 (id,{column_list}) VALUES (null,{value_list});"
            try:
                self.cur.execute(stm)
                self.con.commit()
            except Exception as e:
                print(str(e))
    
    def delete_xml4_table(self):
        stm = "DELETE FROM xml4"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))

    def insert_xml4_table(self, data):
        data_decode = base64.b64decode(data)
        data_xml = BeautifulSoup(data_decode, "xml")
        ct_cls_list = data_xml.find_all('CHI_TIET_CLS')
        for ct_cls in ct_cls_list:
            column_list = ''
            value_list = ''
            for ele in ct_cls:
                if (ele.name != None):
                    column_list = column_list + f'{str(ele.name).lower()},'
                    value_list = value_list + f'"{str(ele.text)}",'
            column_list = column_list[:-1] 
            value_list = value_list[:-1]  
            stm = f"INSERT INTO xml4 (id,{column_list}) VALUES (null,{value_list});"
            try:
                self.cur.execute(stm)
                self.con.commit()
            except Exception as e:
                print(str(e))

    def delete_xml5_table(self):
        stm = "DELETE FROM xml5"
        try:
            self.cur.execute(stm)
            self.con.commit()
        except Exception as e:
            print(str(e))
    
    def insert_xml5_table(self, data):
        data_decode = base64.b64decode(data)
        data_xml = BeautifulSoup(data_decode, "xml")
        ct_cls_list = data_xml.find_all('CHI_TIET_CLS')
        for ct_cls in ct_cls_list:
            column_list = ''
            value_list = ''
            for ele in ct_cls:
                if (ele.name != None):
                    column_list = column_list + f'{str(ele.name).lower()},'
                    value_list = value_list + f'"{str(ele.text)}",'
            column_list = column_list[:-1] 
            value_list = value_list[:-1]  
            stm = f"INSERT INTO xml5 (id,{column_list}) VALUES (null,{value_list});"
            try:
                self.cur.execute(stm)
                self.con.commit()
            except Exception as e:
                print(str(e))
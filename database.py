import sqlite3, os.path, sys

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




